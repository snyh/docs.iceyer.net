# 接入应用管理

@(Linux Deepin)[deepinid]

## 权限

**scope**: base


## API

### Create App

**https://apis.linuxdeepin.com/apps/create**


#### Param


| ParamName        | Required      | Description  |
| ---------------- |:-------------:| :------------|
| **app_name**     | true          | 应用名称      |
| **redirect_uri** | true          | 回调地址      |


#### Return

| ParamName      | Description          |
|:-------------- |:---------------------|
| **app_id**     | client_id            |
| **app_secret** | client_secret        |


<!-- create time: 2014-12-03 09:35:06  -->
