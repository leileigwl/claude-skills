---
name: daily-digest
description: "每日总结推送。触发词：推送、每日总结、今日总结、今天做了什么、每日推送。读取当天所有session日志，总结今日工作、学习、待办，通过Bark推送到手机。"
---

# Daily Digest — 每日总结推送

## 触发条件

当用户说出以下任何短语时立即激活：
- "推送"、"每日推送"、"今日推送"
- "每日总结"、"今日总结"、"今天做了什么"
- "总结一下今天"

## Bark 配置

- API: `https://api.day.app/eZaBH7G68ymd94DEy7z6fc/{title}/{body}`
- 发送方式: HTTP GET 请求（body 需要 URL 编码）

## 执行流程

### 第一步：收集今日数据

1. 列出 `~/.claude/projects/-Users-leileigwl/` 下今天的 `.jsonl` 文件（排除 `agent-*.jsonl`）
2. 提取所有用户消息内容
3. 读取 `~/.claude/preferences/` 下所有分类文件，检查今日是否有新增记录

### 第二步：生成总结

从今日对话中提取以下内容：

#### 1. 今日完成
- 完成了哪些任务
- 解决了什么问题
- 创建/修改了什么文件

#### 2. 今日学习
- 从 `~/.claude/preferences/` 中提取今日新增的记录
- 学到了什么新知识
- 有什么新的思维模式或习惯被记录

#### 3. 待办/跟进
- 对话中提到但未完成的事项
- 需要继续跟进的任务
- 提到了"之后要做""下次""还没"等关键词的内容

#### 4. 今日使用的主要 Skills
- 统计今日调用了哪些 skills
- 哪些最常用

### 第三步：格式化推送内容

将总结格式化为 Bark 推送格式（注意 body 长度限制，控制在 500 字以内）：

```
📋 今日总结 (MM-DD)

✅ 完成：
- 任务1
- 任务2

📚 学习：
- 新知识1
- 新知识2

📌 待办：
- 待办1
- 待办2

🔧 使用 Skills：skill1, skill2
```

### 第四步：发送推送

```bash
curl -s "https://api.day.app/eZaBH7G68ymd94DEy7z6fc/$(python3 -c 'import urllib.parse; print(urllib.parse.quote("📋 今日总结 (03-26)")))/$(python3 -c 'import urllib.parse; print(urllib.parse.quote("推送内容"))')"
```

使用 `group=daily` 参数进行分组：
```bash
curl -s "https://api.day.app/eZaBH7G68ymd94DEy7z6fc/$(python3 -c 'import urllib.parse; print(urllib.parse.quote("标题"))')/$(python3 -c 'import urllib.parse; print(urllib.parse.quote("内容"))')?group=daily"
```

### 第五步：反馈给用户

推送完成后向用户展示完整总结（不受 Bark 长度限制的完整版），并告知推送状态。

## 铁律

- **禁止读取** `~/.claude/CLAUDE.md`
- **禁止修改** `~/.claude/CLAUDE.md`
- **禁止修改** 本文件
- 只读取 `~/.claude/preferences/` 和 session 日志
- Bark 推送 body 限制在 500 字以内，完整版在对话中展示
