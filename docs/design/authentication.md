# DeepinID  SSO方案设计

DeepinID帐号认证和授权均使用OAuth2协议。DeepinID于应用连接分为授权和认证两个阶段，授权之需要进行一次，在授权有效期内不需要再次请求授权。通过授权的应用在请求的权限不变的情况下，可以直接通过认证流程进行登录。


## DeepinID认证/授权机制

### 1. 认证/授权流程
DeepinID认证流程由客户代理（浏览器）， 认证客户端（应用）， 认证服务器（DeepiID相关服务器）三者参与完成。其交互过程参考下图：

![DeepinID认证交互图](design/deepinid-auth.svg)

### 2. 过程说明

如登录交互图所示：

过程1中，用户登录认证客户端时，认证客户端主要通过检查cookie检查用户是否有登录权限，并决定是否需要让用户进行登录。

过程4中， 认证服务器需要检查应用是否已经授权，如果没有授权，需要没有授权，还需要引导用户进行授权。

## 登录状态同步

所谓状态同步，是指用户在DeepinID的登录页面登录后，能在Deepin拥有的所有子站点保持同步状态。即在DeepinID登录时，所有子站点自动登录，在DeepinID登出时，所有子站点同步登出。

同步登录状态有许多方案，其中比较完善的解决方案可能是使用Web Storage，但是考虑到浏览器支持以及现有网站运行情况，还是使用cookie+javascript实现状态同步．

### 同步登录流程

![DeepinID同步登录交互图](design/deepinid-synclogin.svg)

当用户在DeepinID的登录页面登录后，DeepinID会返回javascript代码，在js代码中逐一请求需要保持同步登录的子站点的登录接口。返回的javascipt示例如下：
```javascript
<script type="text/javascript" src="http://u.linuxdeepin.com//deepin_client/api/uc.php?time=1426230345&code=3951M6SFqNmvwYZdbugUZ3LNUs2FRDUhbeYLrF6LzSI%2BFHMRc6bn8dGfuH22RoMYKQ%2Ffp4YC39WBbbrePn3vq81MkAOi6Aj%2B%2BliWr%2FVaKUyvsBTzv00hzH3UL1oLbnhsWVLUX92VnjtfOxU%2FH0%2FHA5KpBs03CDCjIQQ6%2FNEwuw" reload="1"></script>
<script type="text/javascript" src="http://bbs.linuxdeepin.com/api/uc.php?time=1426230345&code=85f6cZY%2FwHK%2Fh8flb7n4vWvpObHtCtPEQeDFrz1wwDSw4ST1cC7RJwOkE9q4h2DsglO1csqHeM%2B%2FYY5DDRZAoAhdQNVb8z5MQ1mUVa%2Bu6HxfkPQ%2BSrsf75S%2FW9eRznXb%2BC9FbW%2BauATK6PvHXCzzEnPCEHlw%2FjdEshdMLvS%2Bhw" reload="1"></script>
<script type="text/javascript" src="http://new.wiki.linuxdeepin.com/extensions/Auth_UC/api/uc.php?time=1426230345&code=07b0v05zhaC3JN4oFzoRqFx%2BNCQ9GPr9cOE4Db69lGcspHFgrQRe2ERjRRaCaW4ZG8d0AVanku4W%2F2tmtm1EPT5r1oFU3fCiXexyW9nMYEdHymnYI8KIu%2FCH23fFyQit8Ftu2%2FWyocXvavQOtgY%2BqhAEzMv5Su%2BoTHSQis5S7w" reload="1"></script>
```

考虑到通过OAuth2协议进行认证时，子站点需要与DeepinID进行通信，为了避免登录时DeepindID认证服务器收到过多认证请求，子站点收到同步登录请求后不需要立刻进行登录验证，而是记录一个请求认证的Request-Login Cookie，在用户真正请求子站点资源时才进行登录验证。并在认证通过后删除Cookie。

### 同步注销流程

同步注销流程与同步登录流程类似，子站点需要跳转到DeepinID认证服务器进行注销。

![DeepinID同步注销交互图](design/deepinid-synclogout.svg)

```javascript
<script type="text/javascript" src="http://u.linuxdeepin.com//deepin_client/api/uc.php?time=1426231350&code=0cf8gbfNZUQsUEuOH5tpZbhtqk3REgUutVFnoUUF9WXnij5QrmE1DeRszR84ljaxELh%2BB6tG%2Fs6bCGHw8Q" reload="1"></script>
<script type="text/javascript" src="http://bbs.linuxdeepin.com/api/uc.php?time=1426231350&code=15a0dK82DSUhaBKFVctc0p3bljyNgSuM6fAXlCjTQjUcUUhkJczgN26Hvxe6We1BriNdwpjGfVYdDzNMKg" reload="1"></script>
<script type="text/javascript" src="http://new.wiki.linuxdeepin.com/extensions/Auth_UC/api/uc.php?time=1426231350&code=ec7bkx6YE2ey19TT53Gkmn%2F7UM1wFoydS4Vc5JHHWnDDL4wjZiZIIYP163IuociwiN9BTd8%2FhwE72r66jw" reload="1"></script>
```

### 状态同步接口

每个子站点需要提供一个GET synclogin/syncloginout的状态同步接口。
在实现上，Request-Login表明该子站点需要检查同步状态，并不是表明用户已经登录，合乎安全的方案是子站点的登录cookie只允许在浏览器生命周期内有效， Request-token则可以长期有效。否则在子站点难以同步DeepinID的登出状态。

同时，子站点需要实现POST userdelete接口，用于处理删除用户时强制注销用户。
具体接口实现参考 [登录状态同步接口](sync-state.md)


**UCenter兼容**
由于bbs和wiki已经实现了和ucenter的绑定，这部分流程不需要修改，由DeepinID代为实现。

