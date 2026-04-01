---
name: leileigwl-blog
description: "博客日记发布工具。帮助用户快速记录日记并自动部署到博客。触发方式：写日记、写博客、今日日记、记录日记。"
---

# leileigwl-blog Skill

博客日记发布工具。帮助用户快速记录日记并自动部署到博客。

## 触发方式
- `/diary` - 记录今日日记
- `/newpost` - 创建技术文章

## 功能说明

### /diary 命令
记录每日日记，包含以下内容：
1. 今天做了什么
2. 今天学到了什么
3. 今天的感悟
4. 明天的计划
5. 配图（可选）

### 流程

1. **询问用户**：依次询问日记内容
2. **自动获取封面图**：从 Unsplash 或 Pexels 自动下载合适的壁纸作为封面图，保存到 `public/images/blog/{日期}-cover.jpg`
3. **创建文章**：在 `src/content/posts/` 创建 `{日期}.md` 文件
4. **保存内容图片**：用户粘贴的图片保存到 `public/images/blog/{日期}.png`（作为文章内容配图）
5. **Git 操作**：
   - `git add .`
   - `git commit -m "docs: 添加日记 {日期}"`
   - `git push origin main`
6. **自动部署**：GitHub Actions 自动触发 Vercel 部署
7. **自动退出**：完成后告知用户「日记已发布！会话即将退出，下次使用 /diary 即可」，然后执行 `/exit` 退出会话

## 自动封面图规则

- **多样化策略**：使用图床 API 随机获取高质量图片，根据日记内容主题选择分类
- **无需用户指定**：自动从免费图库获取

### 封面图 API（优先级排序）

#### 1. Unsplash API（推荐）
```bash
# 随机获取一张图片，指定主题
curl -sL "https://source.unsplash.com/1600x900/?{关键词}" -o cover.jpg

# 常用关键词（按日记主题选择）：
# 开发类: coding,developer,programming,laptop,computer,technology
# 自然类: nature,mountain,forest,ocean,sky,sunset,landscape
# 城市类: city,urban,architecture,building,street,night
# 生活类: coffee,book,reading,workspace,minimal,desk
# 艺术类: art,creative,design,abstract,colorful
```

#### 2. Picsum Photos（备用）
```bash
# 随机获取指定尺寸图片
curl -sL "https://picsum.photos/1600/900?random={随机数}" -o cover.jpg

# 示例：使用日期作为随机种子
curl -sL "https://picsum.photos/1600/900?random=20260331" -o cover.jpg
```

#### 3. Lorem Flickr（多主题）
```bash
# 按关键词搜索
curl -sL "https://loremflickr.com/1600/900/{关键词}" -o cover.jpg

# 支持的关键词：nature,city,cat,dog,business,technology,food,travel
```

#### 4. Bing 每日壁纸（特殊场景）
```bash
# 获取 Bing 每日一图
curl -sL "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1" | jq -r '.images[0].url' | xargs -I {} curl -sL "https://www.bing.com{}" -o cover.jpg
```

### 主题关键词映射表

| 日记主题 | Unsplash 关键词 | Lorem Flickr 关键词 |
|---------|----------------|-------------------|
| 💻 开发/编程/AI | `coding,developer,programming` | `technology,computer` |
| 📱 产品/创业/工作 | `startup,business,workspace` | `business,office` |
| 📚 学习/读书/笔记 | `book,reading,study,library` | `book,education` |
| 🏔️ 自然/风景/旅行 | `nature,mountain,landscape` | `nature,travel` |
| 🌊 海边/日落/放松 | `ocean,sunset,beach,sky` | `sea,sunset` |
| 🏙️ 城市/夜景/建筑 | `city,urban,night,architecture` | `city,building` |
| ☕ 生活/咖啡/日常 | `coffee,cafe,minimal,cozy` | `coffee,food` |
| 🎨 设计/艺术/创意 | `art,design,creative,abstract` | `art,design` |
| 🐱 动物/宠物/可爱 | `cat,dog,pet,cute` | `cat,dog,animal` |
| 🌸 花卉/植物/清新 | `flower,plant,green,nature` | `flower,garden` |

### 选择逻辑
1. 分析日记内容关键词，确定主题分类
2. 从映射表获取对应的关键词
3. **随机选择一个关键词**（同一天不同调用会得到不同图片）
4. 按优先级尝试 API：Unsplash → Picsum → Lorem Flickr → Bing
5. 下载失败时自动降级到下一个 API

### 完整示例命令
```bash
# 根据日记主题生成封面图
TOPIC="coding"  # 根据内容动态确定
DATE="2026-03-31"

# 方式1: Unsplash（推荐）
curl -sL "https://source.unsplash.com/1600x900/?${TOPIC}?sig=${DATE}" -o "/path/to/public/images/blog/${DATE}-cover.jpg"

# 方式2: Picsum（纯随机）
curl -sL "https://picsum.photos/1600/900?random=${DATE}" -o "/path/to/public/images/blog/${DATE}-cover.jpg"

# 方式3: Lorem Flickr
curl -sL "https://loremflickr.com/1600/900/${TOPIC}" -o "/path/to/public/images/blog/${DATE}-cover.jpg"
```

- **注意**：如 API 失败，降级使用预设的 Unsplash 直链
- **保存路径**：`public/images/blog/{日期}-cover.jpg`
- **frontmatter**：`image: '/images/blog/{日期}-cover.jpg'`

## 日记模板

```markdown
---
title: {YYYY.MM.DD}
published: {YYYY-MM-DD}
description: '{简短描述}'
image: '/images/blog/{日期}.jpg'
tags: [日记]
category: '生活'
draft: false
---

## 今天做了什么
- {内容}

## 今天学到了什么
- {内容}

## 今天的感悟
- {内容}

## 明天的计划
- {内容}

![配图](/images/blog/{日期}.jpg)
```

## 注意事项

1. 图片必须保存到 `public/images/blog/` 目录
2. frontmatter 中的 `image` 字段用于显示封面图
3. 推送后等待 1-2 分钟即可在 210214.xyz 查看更新