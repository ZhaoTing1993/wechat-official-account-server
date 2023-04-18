# wechat-official-account-server
微信公众号后台

## quick-start


* 创建instance目录;

* 在config.py中配置自己的公众号secret等信息，复制到/instance/config.py

* 启动 run.py

## service

使用自己微信号关注公众号，并发送消息；

支持以下股票命令:
```js
/s s {code} # 订阅一个股票
/s a {code} {cost} {volome}  # 添加或更新自己的股票持仓
/s d {code} # 删除一个股票
/s q # 查询自己的股票持仓
```

## app

### app/wxctl.py
网络请求入口

### app/command_handler.py
支持的指令

### app/stock
股票相关操作类

### app/db
db相关操作类