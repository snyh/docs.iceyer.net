# 用户管理

@(Linux Deepin)[deepinid]

## 1. 权限

**scope**: admin

## 2 安全说明

**\*建议通过POST方法传递参数， 参数均放在body中**


<!--
**\*加密方式 通过RES加密， 密钥见附件**

Body内容通过公钥加密:

`body： username=deepin&password=123456`

`encypt_body: y78dsuyew7129187dhauds`

重新生产body

`new_body: encrypt=y78dsuyew7129187dhauds`

phps使用如下函数进行加解密:
````
bool openssl_public_encrypt ( string $data , string &$crypted , mixed $key [, int $padding = OPENSSL_PKCS1_PADDING ] )
bool openssl_private_decrypt ( string $data , string &$decrypted , mixed $key [, int $padding = OPENSSL_PKCS1_PADDING ] 
````
-->

## 3. API

### 3.1 Register User

**https://deepinid-deepin.rhcloud.com/admin/register_user**

#### Param

| ParamName                  | Required      | Description                    |
| -------------------------- |:-------------:| :----------------------------- |
| **access_token**           | true          | 授权令牌                       |
| **username**               | true          | 用户名                         |
| **password**               | true          | 密码                           |
| **email**                  | true          | 邮箱                           |
| **nickname**               | false         | 呢称                           |

#### Return

| ParamName      | Description          |
|:-------------- |:---------------------|
| **uid**        | 用户标识           |

##### example

```` json
{"uid":10}
````

### 3.2 Delete User

**https://deepinid-deepin.rhcloud.com/admin/delete_user**

#### Param

| ParamName                  | Required      | Description                   |
| -------------------------- |:-------------:| :---------------------------- |
| **access_token**           | true          | 授权令牌                       |
| **uids**                   | true          | 使用','分隔的uid列表。如：uid=1,2,3|


#### Return

| ParamName         | Description          |
|:------------------|:---------------------|
| **deleted_uids**  | 成功删除的uid列表    |
| **deleted_uids**  | 删除失败的uid列表    |

##### example

```` json
{"deleted_uids":[1,2,3,4],"failed_uids":null}
````


### 3.3 Update User

**https://deepinid-deepin.rhcloud.com/admin/update_user**

#### Param

| ParamName                  | Required      | Description                   |
| -------------------------- |:-------------:| :---------------------------- |
| **access_token**           | true          | 授权令牌                      |
| **uid**                    | true          | uid                           |
| **username**               | true          | 用户名                        |
| **password**               | false         | 密码                          |
| **email**                  | false         | 邮箱                          |
| **nickname**               | false         | 呢称                          |

#### Return

| ParamName      | Description          |
|:-------------- |:---------------------|
| **result**     | true/false           |

##### example

```` json
{"result":true}
````

### 3.4 Query User

**https://deepinid-deepin.rhcloud.com/admin/query_user**

#### Param

| ParamName                  | Required      | Description                   |
| -------------------------- |:-------------:| :---------------------------- |
| **access_token**           | true          | 授权令牌                      |
| **uid**                    | true          | uid                           |


<!--
 | **password**               | false         | 密码                          |
| **email**                  | false         | 邮箱                          |
| **nickname**               | false         | 呢称                          |

uid, password, email, nickname至少填写一个，否则返回空
-->

#### Return

| ParamName      | Description           |
|:-------------- |:----------------------|
| **username**   | 用户名                |
| **email**      | 邮箱                  |
| **nickname**   | 呢称                  |

##### example

```` json
{"email":"test@deepin.com","nickname":"Deepin","username":"deepin"}
````

<!--

### 3.5 List User

**https://deepinid-deepin.rhcloud.com/admin/list_user**

#### Param

| ParamName                  | Required      | Description                   |
| -------------------------- |:-------------:| :---------------------------- |
| **access_token**           | true          | 授权令牌                      |
| **uid_begin**              | true          | uid                           |
| **uid_count                | true          | 要查询的uid数目               |

#### Return

```` json
{
    "users":[
        {"uid":1234,"email":"deepin@deepin.com","nickname":"Deepin","username":"deepin"}, 
        {"uid":4567,"email":"iceyer@iceyer.com","nickname":"Iceyer","username":"iceyer"},
    ]
}

````

| ParamName      | Description           |
|:-------------- |:----------------------|
| **uid**        | uid                   |
| **username**   | 用户名                |
| **password**   | 密码                  |
| **email**      | 邮箱                  |
| **nickname**   | 呢称                  |

-->


<!-- create time: 2014-12-03 09:50:22  -->
