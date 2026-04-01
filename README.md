# Claude Code Skills

个人 Claude Code skills 备份仓库。

---

## 📦 Skills 清单（19 个）

### 💼 商业工具 (dbs 系列 - 6个)

| Skill | 触发词 | 用途 |
|-------|--------|------|
| **dbs** | `/dbs`、`商业`、`帮我看看` | 商业工具箱入口，自动路由到合适的诊断工具 |
| **dbs-diagnosis** | `/问诊`、`商业模式` | 商业模式诊断（问诊/体检两种模式） |
| **dbs-benchmark** | `/对标`、`找对标` | 五重过滤法对标分析 |
| **dbs-content** | `/内容诊断` | 内容创作诊断 |
| **dbs-deconstruct** | `/拆概念` | 概念拆解（维特根斯坦+奥派经济学） |
| **dbs-unblock** | `/自检`、`执行力` | 执行力诊断（阿德勒心理学框架） |

### 🛠️ 开发工具 (gstack - 27个子技能)

| Skill | 用途 |
|-------|------|
| **autoplan** | 自动审查管道 |
| **benchmark** | 性能基准测试 |
| **browse** | 无头浏览器 QA |
| **canary** | 部署后监控 |
| **careful** | 破坏性命令警告 |
| **codex** | OpenAI Codex 包装 |
| **cso** | 安全审计 (CSO模式) |
| **design-consultation** | 设计系统咨询 |
| **design-review** | 视觉 QA |
| **document-release** | 文档更新 |
| **freeze** | 限制编辑目录 |
| **gstack-upgrade** | 升级 gstack |
| **guard** | 全安全模式 |
| **investigate** | 系统调试 |
| **land-and-deploy** | 合并部署 |
| **office-hours** | YC 办公时间模拟 |
| **plan-ceo-review** | CEO 审查 |
| **plan-design-review** | 设计审查 |
| **plan-eng-review** | 工程审查 |
| **qa** | QA 测试修复 |
| **qa-only** | QA 报告 |
| **retro** | 周回顾 |
| **review** | PR 审查 |
| **setup-browser-cookies** | 导入 cookies |
| **setup-deploy** | 配置部署 |
| **ship** | 发布流程 |
| **unfreeze** | 解除冻结 |

### 🔧 独立工具 (13个)

| Skill | 触发词 | 用途 |
|-------|--------|------|
| **bark** | `/bark` | Bark 通知推送 |
| **daily-digest** | `推送`、`每日总结` | 每日工作总结推送到手机 |
| **last30days** | `/last30days` | 30天深度研究（Reddit/X/YouTube等10+源） |
| **leileigwl-blog** | `写日记`、`写博客` | 博客日记发布工具 |
| **memory-recorder** | `记录`、`学习习惯` | 自动学习用户偏好，写入 preferences |
| **neon-slides** | `生成PPT`、`neon slides` | 霓虹风格 HTML 幻灯片 |
| **notebooklm-skill** | `/notebooklm` | NotebookLM 搜索查询 |
| **slide** | `做个PPT`、`生成幻灯片` | Markdown 大纲转 HTML 幻灯片 |
| **solar-config** | `/solar-config`、`光伏配置` | 光伏储能系统配置诊断 |
| **tavily** | `/tavily` | Tavily 搜索 API |
| **web-access** | `搜索`、`抓取网页` | 网页搜索、抓取、登录操作 |
| **wewrite** | `公众号`、`微信推文` | 微信公众号内容全流程助手 |
| **claude-api** | Claude API | Claude API/SDK 开发助手 |

---

## 📁 目录结构

```
skills/
├── bark/                  # Bark 通知
├── daily-digest/          # 每日总结推送
├── dbs/                   # 商业工具入口
├── dbs-benchmark/         # 对标分析
├── dbs-content/           # 内容诊断
├── dbs-deconstruct/       # 概念拆解
├── dbs-diagnosis/         # 商业诊断
├── dbs-unblock/           # 执行力诊断
├── gstack/                # 开发工具集（27个子技能）
├── last30days/            # 30天研究
├── leileigwl-blog/        # 博客日记
├── memory-recorder/       # 偏好记忆
├── neon-slides/           # 霓虹幻灯片
├── notebooklm-skill/      # NotebookLM
├── slide/                 # Markdown幻灯片
├── solar-config/          # 光伏配置
├── tavily/                # Tavily搜索
├── web-access/            # 网页访问
└── wewrite/               # 微信公众号
```

---

## 🔗 来源

| Skill | 来源 |
|-------|------|
| gstack | https://github.com/anthropics/gstack |
| dbs 系列 | dontbesilent 商业框架 |
| neon-slides | 自建 |
| slide | 自建 |
| memory-recorder | 自建 |
| daily-digest | 自建 |
| notebooklm-skill | ClawHub |
| last30days | ClawHub |

---

## 📅 备份日期

- 2026-04-01: 初始备份，清理后保留 19 个核心 skills

---

## 使用说明

这些 skills 通过 Claude Code 的 Skill 工具调用。每个 skill 有 `SKILL.md` 文件定义触发词和行为。

```bash
# 本地路径
~/.claude/skills/
```
