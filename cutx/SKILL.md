---
name: cutx
description: 自动口播视频剪辑。检测静音、填充词、重复内容、说错字"重来"等，自动裁剪。触发词：裁剪视频、剪辑视频、cutx、去重来。
origin: user
---

# CutX 视频自动裁剪

自动检测口播视频中的冗余内容并裁剪。

## 触发场景
- 用户说"裁剪视频"、"剪辑视频"
- 用户说"帮我处理这个视频"、"去掉重来"
- 用户提到 CutX

## 配置文件
- `~/.cutx.env` - ASR 和 LLM 凭据

## 工具路径
```
/Users/leileigwl/Code/Tool/chonglai-video-cutter/cutx/cutx.py
```

## 使用方式

### 1. 只检测（预览）
```bash
python3 /Users/leileigwl/Code/Tool/chonglai-video-cutter/cutx/cutx.py "视频路径.mp4" --detect-only
```

### 2. 检测 + 裁剪
```bash
python3 /Users/leileigwl/Code/Tool/chonglai-video-cutter/cutx/cutx.py "视频路径.mp4" -y
```

### 3. 保留部分静音
```bash
python3 /Users/leileigwl/Code/Tool/chonglai-video-cutter/cutx/cutx.py "视频路径.mp4" --keep-silence 0.3 -y
```

## 检测内容

| 类型 | 说明 |
|------|------|
| 静音 | 超过 0.8 秒的无声段 |
| 填充词 | 纯"嗯"、"啊"、"呃"等 |
| 重复 | 与上一句相似度 >85% |
| 说错字 | 包含"重来"等触发词的段落 |

## 偏好设置
- 时间格式：分钟格式（00:53.070）
- 填充词：只删纯废话，保留有连接作用的
- 裁剪后自动验证：转写成文字，检查是否有残留

## 工作流程

1. 用户提供视频路径
2. 先运行 `--detect-only` 预览检测结果
3. 展示检测报告，询问用户是否执行
4. 用户确认后，执行裁剪
5. 裁剪完成，输出新视频路径
6. （可选）转写验证是否有残留

## 输出示例

```
总时长: 5:29 | 检测到 8 处可裁剪 | 总计 0:32

[00:12.340 - 00:14.560] 静音 2.2秒
[01:23.100 - 01:23.800] 填充词: 嗯...
[02:45.000 - 02:58.300] 说错字: 这个不对重来...
```