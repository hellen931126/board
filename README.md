# Board

## 目的
该项目计划使用[“极验”](http://www.geetest.com)实现一个限制spam的留言板

## 需求说明
* 对于正常登录的用户，不显示“极验验证码”和校验；对于异常登录、留言的用户显示“极验验证码”，并进行校验
* P.S. 异常登录、留言是指单一IP或者单一用户进行高频登录、留言操作

## 数据库设计
- **users**

| 字段名         | 类型           | 说明                          |
| ------------- | ------------- | -----------------------------|
| id            | INT       | -                            |
| uuid          | VARCHAR(36)    | 用户UUID                         |
| username          | VARCHAR(36)    | 用户昵称                |
| avatar        | TEXT    | 用户头像                |
| password     | VARCHAR(20)          | 用户密码                |
| created_at    | DATETIME          | 创建时间                       |
| updated_at    | DATETIME          | 更新时间                       |

- **comments**

| 字段名         | 类型           | 说明                          |
| ------------- | ------------- | -----------------------------|
| id            | INT       | -                            |
| uuid     | VARCHAR(36)    | 留言UUID                      |
| content   | TEXT    | 留言内容                   |
| user_uuid          | VARCHAR(36)    | 用户UUID                       |
| created_at    | DATETIME          | 创建时间                       |
| updated_at    | DATETIME          | 更新时间                       |



