# Board

## 目的
该项目计划使用[“极验”](http://www.geetest.com)实现一个限制spam的留言板

## 需求说明
* 对于正常登录的用户，不显示“极验验证码”和校验；对于异常登录、留言的用户显示“极验验证码”，并进行校验
* P.S. 异常登录、留言是指单一IP或者单一用户进行高频登录、留言操作

## 目前效果图展示
图上展示了每位用户留言的浏览器ID（由fingerprintjs生成），系统根据这样的”用户ID“和用户访问的IP地址来限制用户的spam行为
[![效果图.jpg](https://i.loli.net/2018/05/10/5af43a4a5c1bf.jpg)](https://i.loli.net/2018/05/10/5af43a4a5c1bf.jpg)

## 数据库设计
- **users**

| 字段名         | 类型           | 说明                          |
| ------------- | ------------- | -----------------------------|
| id            | INT       | 用户ID                            |
| username          | VARCHAR(36)    | 用户昵称                |
| created_at    | DATETIME          | 创建时间                       |
| updated_at    | DATETIME          | 更新时间                       |
| password_hash     | VARCHAR(128)          | 用户密码                |

- **comments**

| 字段名         | 类型           | 说明                          |
| ------------- | ------------- | -----------------------------|
| id            | INT       | -                            |
| content   | TEXT    | 留言内容                   |
| user_id       | INT       | 用户ID                       |
| browser_id       | VARCHAR(48)       | 客户端浏览器ID                       |
| created_at    | DATETIME          | 创建时间                       |
| updated_at    | DATETIME          | 更新时间                       |

## 运行说明
* 环境：Python3.5 & Ubuntu 16.04
* 运行： 
    * 运行前需创建一个叫board的mysql数据库
    * 安装依赖
        > pipenv install
    * 激活虚拟环境
        > pipenv shell
    * 创建数据库表
        > python manage.py shell
        > \>\>from manage import db
        \>\> db.create_all()\>\> quit()
    * 运行
        > python manage.py runserver   

## 需要解决的问题
* 加入“极验”进行验证码验证