# 登录状态同步接口

## 通讯协议

通信协议设计中，同步登录状态完全不需要携带任何用户相关信息，仅仅需要通知相关站点设置一个标记性的cookie，所以即使使用GET方法也不会威胁到协议的安全性。但是考虑到后续扩展过程中需要传递参数，为保证数据安全，对传递的参数使用AES进行加密，加密密钥为client_secret的奇数位，避免算法漏洞导致client_secret泄漏。
假设传递参数为：

```html
method=synclogin&expire=123457823`
```
client_srcret为`12345678123456781234567812345678`, 则ASE加密密钥为`1357135713571357`, 对参数进行ASE加密并进行base64编码得到结果为：

```html
bWV0aG9kPXN5bmNsb2dpbiZleHBpcmU9MTIzNDU3ODIz
```

[参考代码](http://play.golang.org/p/UA41WhvOCb)


## 状态接口

### 1 通用参数

在状态同步接口中，需要传递以下通用参数

| 参数名称         | 必选  | 类型    | 描述       |
|------------------|-------|--------|-------------|
| **method** | true | string | synclogin/synclogout/userdelete |
| **client_id** | true | string | 申请应用时分配的AppKey |
| **crypto** | true | string | 加密参数 |

### 2 SyncLogin接口

#### 2.1 API Endpoint

GET https://client-host/interface

#### 2.2 crypto参数

** crypto中需要传递的参数为**

| 参数名称         | 必选  | 类型    | 描述       |
|------------------|-------|--------|-------------|
| **verfiy_method** | true | string | synclogin， 需要与method参数保持一致 |
| **expire** | true |  string | 请求过期时间 |

#### 2.3 示例

```html
GET https://client-host/interface?method=synclogin&client_id=7391sda&crypto=dmVyZml5X21ldGhvZD1zeW5jbG9naW4mZXhwaXJlPTEyMzQ1NzgyMw
```
解密后参数为：
```html
GET https://client-host/interface?method=synclogin&client_id=7391sda&verfiy_method=synclogin&expire=123457823
```

### 3 SyncLogout接口

#### 3.1 API Endpoint

GET https://client-host/interface

#### 3.2 crypto参数

** crypto中需要传递的参数为**

| 参数名称         | 必选  | 类型    | 描述       |
|------------------|-------|--------|-------------|
| **verfiy_method** | true | string | synclogout， 需要与method参数保持一致 |
| **expire** | true |  string | 请求过期时间 |

#### 3.3 示例

```html
GET https://client-host/interface?method=synclogout&client_id=7391sda&crypto=dmVyZml5X21ldGhvZD1zeW5jbG9nb3V0JmV4cGlyZT0xMjM0NTc4MjM
```
解密后参数为：
```html
GET https://client-host/interface?method=synclogout&client_id=7391sda&verfiy_method=synclogout&expire=123457823
```

### 4 UserDelete接口

#### 4.1 API Endpoint

POST https://client-host/interface

#### 4.2 crypto参数

** crypto中需要传递的参数为**

| 参数名称         | 必选  | 类型    | 描述       |
|------------------|-------|--------|-------------|
| **verfiy_method** | true | string | userdelete， 需要与method参数保持一致 |
| **username** | true |  string | 用户名 |
| **expire** | true |  string | 请求过期时间 |

#### 4.3 示例

```html
POST https://client-host/interface
method=userdelete&client_id=7391sda&crypto=dmVyZml5X21ldGhvZD11c2VyZGVsZXRlJnVzZXJuYW1lPXRlc3QmZXhwaXJlPTEyMzQ1NzgyMw
```
解密后参数为：
```html
POST https://client-host/interface
method=userdelete&client_id=7391sda&verfiy_method=userdelete&username=test&expire=123457823
```
