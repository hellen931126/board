from flask import render_template, session, redirect, url_for, request, flash
from flask_login import login_required, login_user, logout_user, current_user
from .forms import LoginForm, RegisterationForm, CommentForm
from ..models import User, Comment
from .. import db, redis

from . import main

@main.route("/", methods=["GET","POST"])
def index():
    browser_id = request.args.get('id')
    user_ip = request.remote_addr
    form = CommentForm()
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            return redirect(url_for('main.login'))
        if redis.get(browser_id):
            if int(redis.get(browser_id)) > 3 or int(redis.get(user_ip)) > 3:
                return redirect(url_for('main.login'))
        redis.incr(browser_id)
        redis.incr(user_ip)
        redis.expire(browser_id, 30)
        redis.expire(user_ip, 30)
        comment = Comment(content=form.content.data, user=current_user._get_current_object())
        db.session.add(comment)
        return redirect(url_for('main.index'))
    comments = Comment.query.order_by(Comment.updated_at.desc()).all()   
    return render_template('index.html', form=form, comments=comments)

@main.route('/login', methods=['GET','POST'])
def login():
    browser_id = request.args.get('id')
    user_ip = request.remote_addr
    form = LoginForm()
    if form.validate_on_submit():
        if redis.get(browser_id):
            if int(redis.get(browser_id)) > 3 or int(redis.get(user_ip)) > 3:
                return redirect(url_for('main.login'))
        redis.incr(browser_id)
        redis.incr(user_ip)
        redis.expire(browser_id, 30)
        redis.expire(user_ip, 30)
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)          
            return redirect(request.args.get("next") or url_for("main.index"))
    return render_template("login.html", form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("main.login"))
    return render_template("register.html", form=form)