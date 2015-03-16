# 用户管理

用户管理接口提供面向管理员的用户数据CURD操作。

## 1. 说明

用户管理接口主要面向DeepinID的OA以及passport(u.linuxdeeepin.com)提供用户添加删除等基本用户管理的接口。

对于passport， 主要使用create user接口和update user接口来注册和更新用户信息。特别注意的是，前端不可以根据用户的输入来作为本文所涉及接口的输入，否则会导致严重的用户信息泄漏。


## 2. 权限

**Access-Token**: 具有admin权限的token。

Access-Token要求作为http请求的头部参数。每一个请求中都必须携带该参数。

对于使用该接口的应用，token会在服务器上进行配置，并定期更新。

## 3. API

### 3.1 Create User

**POST https://api.linuxdeepin.com/admin/user**

#### 3.1.1 Param

##### Header Param

**Access-Token**: 拥有admin权限的token。

##### Body Param

| ParamName                  | Required      | Description                    |
| -------------------------- |---------------|------------------------------- |
| **username**               | true          | 用户名                          |
| **password**               | true          | 密码                            |
| **email**                  | true          | 邮箱                            |
| **nickname**               | false         | 呢称                            |

#### 3.1.2 Return

| ParamName      | Description         |
|--------------- |---------------------|
| **uid**        | 用户标识             |

#### 3.1.3 Example

**Request:**

````json
POST https://api.linuxdeepin.com/admin/user

Header:
Access-Token: "789fdiaudfjewe8728323hj2k39239adf8amvn09fdajkj"
Content-Type: application/json

Body:
{
	"username": "test",
	"password": "php_encrypt(21231432)",
	"email": "test@test.com",
	"nickname": "Test"
}
````

** Respone:**

```` json
{
  "error_code": 200
  "error_msg": "",
  "data": {
    "uid": 9
  }
}
````

### 3.2 Delete User

**DELETE https://api.linuxdeepin.com/admin/user/id/:id**

#### 3.2.1 Param

| ParamName                  | Required      | Description                   |
| -------------------------- |:-------------:| :---------------------------- |
| **:id**                   | true          | uid|


#### 3.2.2 Return

| ParamName         | Description          |
|:------------------|:---------------------|
| **error_code**    | 200表示操作成功    |

##### 3.2.3 Example

** Request**

```` json
DELETE https://api.linuxdeepin.com/admin/user/id/10

Header:
Access-Token: "789fdiaudfjewe8728323hj2k39239adf8amvn09fdajkj"
````
** Respone**
```` json
{
  "error_code": 200,
  "error_msg": "",
  "data": null
}
````


### 3.3 Update User

**PUT https://api.linuxdeepin.com/admin/user/id/:id**

#### 3.3.1 Param

| ParamName                  | Required      | Description                   |
| -------------------------- |:-------------:| :---------------------------- |
| **:id**                    | true          | uid                           |
| **username**               | true          | 用户名                        |
| **password**               | false         | 密码                          |
| **email**                  | false         | 邮箱                          |
| **nickname**               | false         | 呢称                          |

#### 3.2.2 Return

| ParamName      | Description          |
|:-------------- |---------------------|
| **data**     | 修改后的用户信息，只返回本次修改的部分和uid  |

##### 3.2.3 Example

** Request**

```` json
PUT https://api.linuxdeepin.com/admin/user/id/10

Header:
Access-Token: "789fdiaudfjewe8728323hj2k39239adf8amvn09fdajkj"
Content-Type: application/json

Body:
{
	"password": "php_encrypt(change21231432)",
	"email": "testChange@test.com",
}
````

** Respone**

````json
{
   "error_code": 200,
   "error_msg": "",
   "data":
   {
	   "email": "testChange@test.com",
	   "password": "php_encrypt(change21231432)",
	   "uid": 10
   }
}
````



### 3.4 Query User

** GET https://api.linuxdeepin.com/admin/user/id/:id **

#### 3.4.1 Param

| ParamName                  | Required      | Description                   |
| -------------------------- |---------------|-------------------------------|
| **:id**                    | true          | uid                           |


#### 3.4.2 Return

| ParamName      | Description           |
|:-------------- |:----------------------|
| **username**   | 用户名                |
| **email**      | 邮箱                  |
| **nickname**   | 呢称                  |


#### 3.4.3 Example

** Request**

```` http
GET https://api.linuxdeepin.com/admin/user/id/10

Header:
Access-Token: "789fdiaudfjewe8728323hj2k39239adf8amvn09fdajkj"
````

** Respone**

````json
{
   "error_code": 200,
   "error_msg": "",
   "data":
   {
	   "avatar": "",
	   "email": "testChange@test.com",
	   "nickname": "TestChange",
	   "profile_image": "",
	   "scope": "",
	   "uid": 10,
	   "username": "test"
   }
}
````

### 3.5 Query User by username

** GET https://api.linuxdeepin.com/admin/user/name/:username **

#### 3.5.1 Param

| ParamName                  | Required      | Description                   |
| -------------------------- |---------------|------------------------------ |
| **:username**              | true          | 用户名                         |


#### 3.5.2 Return

参见 [3.4.2](#34-query-user)

#### 3.5.3 Example

** Request**

```` http
GET https://api.linuxdeepin.com/admin/user/username/test

Header:
Access-Token: "789fdiaudfjewe8728323hj2k39239adf8amvn09fdajkj"
````

** Respone**

````json
{
   "error_code": 200,
   "error_msg": "",
   "data":
   {
	   "avatar": "",
	   "email": "testChange@test.com",
	   "nickname": "TestChange",
	   "profile_image": "",
	   "scope": "",
	   "uid": 10,
	   "username": "test"
   }
}
````

### 3.6 List User

** GET https://api.linuxdeepin.com/admin/user/idlist**

#### 3.6.1 Param

| ParamName                  | Required      | Description                   |
| -------------------------- |---------------| ----------------------------- |
| **list**                   | true          | uid list, list=[1,2,3]        |

#### 3.6.2 Return
| ParamName      | Description           |
|:-------------- |:----------------------|
| **data**        | map[uid]userinfo,返回一个uid与用户信息的map，用户信息具体参数参见[3.4.2](#34-query-user)    |

#### 3.6.3 Example

** Request**
```` json
GET https://api.linuxdeepin.com/admin/user/idlist

Header:
Access-Token: "789fdiaudfjewe8728323hj2k39239adf8amvn09fdajkj"
````

** Respone**

```` json
{
   "error_code": 200,
   "error_msg": "",
   "data":
   {
       "8":
       {
           "uid": 8,
           "username": "user8",
           "password": "password",
           "nickname": "Iceyer",
           "email": "me8@iceyer.net",
           "scope": "",
           "avatar": "",
           "profile_image": ""
       }
   }
}
````

### 3.7 Delete Muti User 

** DELETE https://api.linuxdeepin.com/admin/user/idlist**


#### 3.7.1 Param

| ParamName                  | Required      | Description                   |
| -------------------------- |---------------| ----------------------------- |
| **list**                   | true          | uid list, json format       |

#### 3.7.2 Return
| ParamName      | Description           |
|----------------|----------------------|
| **deleted_uids** | 成功删除的uid列表   |
| **failed_uids** | 删除失败的uid列表   |

#### 3.7.3 Example

** Request**
```` json
DELETE https://api.linuxdeepin.com/admin/user/idlist

Header:
Access-Token: "789fdiaudfjewe8728323hj2k39239adf8amvn09fdajkj"
Content-Type: application/json

Body:
{
"list":[8]
}
````

** Respone**

```` json
{
   "error_code": 200,
   "error_msg": "",
   "data":
   {
	   "deleted_uids": [8],
	   "failed_uids": null
   }
}
````