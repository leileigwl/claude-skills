# Bark 通知 Skill

发送 iOS 推送通知到用户手机，用于任务完成提醒。

## 使用方法

```bash
# 发送通知
/bark 标题 内容
```

## API 信息

- 服务地址: https://api.day.app
- API Key: eZaBH7G68ymd94DEy7z6fc

## 实现说明

使用 HTTP GET 请求发送通知：
```
https://api.day.app/{key}/{title}/{body}
```

## 可选参数

- `sound`: 自定义铃声 (如 alarm, bell, glass 等)
- `group`: 分组名称
- `icon`: 自定义图标 URL
- `url`: 点击跳转链接