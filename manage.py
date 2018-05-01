import os
from app import create_app, db
from app.models import User, Comment
from flask_script import Manager
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand

app = create_app("default")
manager = Manager(app)

def make_shell_context():
    return dict(app=app,db=db, User=User, Comment=Comment)
manager.add_command("shell",Shell(make_context=make_shell_context))
manager.add_command("db",MigrateCommand)

if __name__=="__main__":
    manager.run()