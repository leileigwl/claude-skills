# presentations_by_ai

一个聚焦“用 AI 做 PPT”的经验分享。这里汇集了我在分享中的全部素材：从思维框架、提示词示例到可直接运行的前端模板，让你能边学边做，快速点亮 AI 演示文稿的隐藏技能树。
更多内容也会同步更新在我的 B 站主页：https://space.bilibili.com/28554995

## 项目内容
- **Vue 3 演示项目**：`vue_ppt/` 内提供基于 Vite + TypeScript + Tailwind CSS 的多页演示（当前主打 `AI Skill Tree`），涵盖页面规划、组件拆分、交互动画等最佳实践。
- **提示词与教程**：`docs/` 下的文档记录了如何与 Codex、Claude 等模型协作生成 PPT，包括整体规划、设计语言、提示词模版等。
- **素材工具箱**：`python/` 目录内提供贴图生成脚本与示例，方便扩展图像类素材。

## 快速开始
```bash
cd vue_ppt
npm install
npm run dev
```
打开浏览器访问 `http://localhost:5173`，即可查看并实时编辑演示文稿。


## 如何使用
- **跟着流程学习**：从 `docs/totorials/1 Skill Tree` 里的提示词与大纲入手，了解如何驱动模型完成整份 PPT。
- **修改/扩展页面**：`src/presentations/ai-skill-tree/` 中每个页面对应一个 `.vue` 文件，直接编辑即可；保持“一页一文件”的习惯，能让对话上下文更清晰。
- **复用模板组件**：项目鼓励把通用功能沉淀到 `shared` 目录（背景、布局、轮播组件等），用结构化的代码提示模型生成更稳定的结果。
- **结合工具链**：配合 Cursor、Codex、Claude Code 等工具迭代；文档中也给出了不同模型/工具的适配场景，按需选择。

## 后续计划

如果大家感兴趣，就继续在这个项目中更新一些新的邪修AI的方法论。当然肯定还是在B站的视频里。

欢迎关注B站主页 https://space.bilibili.com/28554995
