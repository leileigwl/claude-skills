# qwen3-next-bench 页面模板设计语言（内容无关版）

本指南不涉及具体文案与内容，仅定义页面“种类/功能”的模板与可复用的设计规范，便于用同一设计语言自动或半自动生成新页面。所有示例均可直接映射到 Tailwind v3 原子类与现有的背景组件。

## 全局设计令牌（Design Tokens）
- 颜色系统（RGB/Alpha）
  - 背景舞台：使用全幅柔和网格/径向渐变背景（由背景组件输出）。可见度低，不与前景争夺对比。
  - 品牌渐变：从蓝紫 → 品红 → 翠绿的高饱和渐变，用于标题、强调文本与重点分隔。
    - 示例停靠：`indigo-500 -> fuchsia-500 -> emerald-400`
  - 前景表面：半透明白底玻璃态，配合模糊与细边框。
    - 表面底色：`bg-white/70 ~ /80`
    - 边框描边：`border border-slate-200/30`
    - 背景模糊：`backdrop-blur-md ~ lg`
  - 文本颜色：
    - 强文本：`text-slate-900`
    - 次文本：`text-slate-600 ~ 700`
    - 反白文本（深色背景上）：`text-slate-50`
    - 渐变文本：`text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 via-fuchsia-400 to-emerald-400`
  - 状态色：
    - 成功：`emerald-500`
    - 信息：`sky-500`
    - 警告：`amber-500`
    - 危险：`rose-500`

- 字体与排版
  - 字体族：中英文通用无衬线（如 Inter/系统 UI/中文黑体），数字采用等宽风格（`tabular-nums`）。
  - 层级与字号（移动端按 1–2 级缩小）：
    - H1：`text-6xl ~ 8xl`，`font-black`，`tracking-tight`，行高 `leading-tight`
    - H2：`text-4xl ~ 5xl`，`font-extrabold`，`leading-tight`
    - H3：`text-2xl ~ 3xl`，`font-bold`，`leading-snug`
    - 正文：`text-lg`（必要时 `text-base`），`leading-relaxed`
    - 辅助：`text-sm`，`text-slate-600`
    - 代码：等宽字体，`text-sm ~ base`，深色块内 `text-slate-100`

- 布局与间距
  - 容器：居中、最大宽度 `max-w-5xl ~ 6xl`，`mx-auto`，外边距/内边距 `px-6 md:px-8 lg:px-12 py-12 lg:py-16`。
  - 栅格：12 列心智，常用卡片网格为 `grid-cols-1 sm:grid-cols-2 lg:grid-cols-3` 或 `auto-fit minmax(280~360px)`。
  - 圆角半径：`rounded-3xl ~ 4xl`（约 24–32px）。
  - 阴影与高程：`shadow-xl ~ 2xl`，可选柔光环 `ring-1 ring-white/30`。
  - 边框：1px 细边，`border-slate-200/30`。

- 动效与节奏
  - 背景渐变缓慢流动（12–20s），元素轻微悬浮（1–3px 振幅），交互过渡 200–300ms。
  - 兼容 `prefers-reduced-motion`，在减少动效模式下静止或改为淡入淡出。

- 响应式断点
  - `sm 640`、`md 768`、`lg 1024`、`xl 1280`、`2xl 1536`。
  - 小屏：缩小字号、减少列数、增加垂直间距；大屏：保持最大宽度与居中，不全宽铺开。

- 无障碍与可用性
  - 对比度：正文与背景的对比度建议 ≥ 4.5:1。
  - 焦点可见：交互元素需 `focus-visible:ring`。
  - 触达尺寸：点击目标 ≥ 40×40px。
  - 文本块不超过 80 字/行，中文适当分段。

## 基础组件模式（可组合）
- 玻璃态卡片（Surface/Card）
  - `bg-white/70 backdrop-blur-md border border-slate-200/30 rounded-3xl shadow-xl`
  - 可加 `p-6 md:p-8` 作为默认内边距。

- 渐变标题（Gradient Heading）
  - 容器：`inline-block`
  - 类：`text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 via-fuchsia-400 to-emerald-400`
  - 层级：与 H1/H2 对齐。

- Pill 按钮/标签（Pill Button/Tag）
  - 基态：`inline-flex items-center gap-2 px-4 py-2 rounded-full bg-white/60 border border-white/40 backdrop-blur-md shadow-sm`
  - 悬停：`hover:bg-white/70 hover:shadow`
  - 选中：`bg-gradient-to-r from-indigo-500/20 to-emerald-400/20 text-slate-900`

- 指标卡（Stat Card）
  - 容器：玻璃态卡片 + `flex flex-col gap-2`
  - 数值：`text-4xl ~ 6xl font-black tracking-tight`
  - 标签：`text-sm text-slate-600`

- 代码/面板（Code/Panel）
  - 容器：`bg-slate-900/80 text-slate-100 rounded-2xl border border-white/10 shadow-xl`
  - 内部：`font-mono text-sm leading-relaxed p-4 md:p-6`

- 选项卡（Tabs）
  - Tab 列：`flex flex-wrap gap-2`
  - 项：Pill 按钮风格；激活项加底部高亮线或渐变底色。

## 页面模板（按功能复用）

1) 封面 / Hero
- 目的：建立主视觉与主题基调，突出 1–2 条关键信息。
- 布局：
  - 上/中 置大标题（H1），下方简短副标题（H3/正文）。
  - 居中主容器（最大宽 `max-w-6xl`），留足四周安全边距（`py-16 px-8+`）。
- 组件：渐变标题 + 玻璃态信息卡 + 主要 CTA（单个按钮）。
- 颜色：标题可用品牌渐变；其余正文使用深色文本；卡片保持白雾感。
- 字号：H1 `text-7xl±1`，副标题 `text-2xl ~ 3xl`，正文 `text-lg`。
- 交互：轻浮动/渐显；CTA 悬停加亮。
- 响应式：小屏将 H1 降至 `text-5xl`，栅格改单列。

2) 目录 / 大纲
- 目的：提供页面/章节索引与节奏概览。
- 布局：
  - 标题（H2）+ 垂直列表或 2 列卡片列表。
  - 列表项使用等高 Pill 卡片，编号或进度点可选。
- 组件：Pill 列表项（可点击），可加当前节点高亮。
- 颜色：整体中性；当前项加品牌色或渐变描边。
- 字号：H2 `text-4xl ~ 5xl`，项标题 `text-xl`，描述 `text-sm ~ base`。
- 交互：悬停加投影/描边，选中项填充渐变淡色。

3) 配置 / 参数（Tab + Panel）
- 目的：展示多维度设置、环境或参数切换。
- 布局：
  - 顶部 Tab 列（Pill），下方面板区可为卡片格栅或代码块。
  - 常用 4–6 个 Tab；内容区支持文本、标签栈、代码片段。
- 组件：Tabs + 卡片/代码面板。
- 颜色：Tab 选中使用品牌渐变淡色，未选中半透明白底。
- 字号：Tab 文本 `text-sm ~ base`，面板标题 `text-xl ~ 2xl`。
- 交互：切换面板时淡入，Tab 有焦点环。

4) 指标 / 统计（Stats Grid）
- 目的：以并列卡片展示关键数据点（KPI、里程碑）。
- 布局：
  - 3 列或 2 列网格；每张卡片“数值大、标签小、描述简”。
  - 网格间距 `gap-6 ~ 8`，卡片内距 `p-6 ~ 8`。
- 组件：指标卡（数值、单位、标签、说明）。
- 颜色：数值可配渐变描边或色带；描述文本保持次要色。
- 字号：数值 `text-5xl ~ 6xl`，标签 `text-sm`，说明 `text-sm ~ base`。
- 交互：悬停卡片略抬升/加光泽。

5) 可视化 / 嵌入（Embed/Chart）
- 目的：承载图表、地图或外部交互（通过 iframe/组件）。
- 布局：
  - 标题 + 宽屏内容框（建议 4:3 或 16:9）。
  - 内容框采用深色或玻璃态容器，有足够内边距。
- 组件：可嵌入 iframe、Plot、Canvas/WebGL。
- 颜色：深色面板 `bg-slate-900/80` 与浅色文字对比明显。
- 字号：标题 `text-3xl ~ 4xl`，辅助说明 `text-sm ~ base`。
- 交互：加载淡入，Hover 提示（若可用）。

6) 清单 / 建议（Checklist/Guides）
- 目的：以要点/任务形式传达指南、注意事项、最佳实践。
- 布局：
  - 2–3 列卡片或单列分组；每项“标题 + 次说明”。
  - 可用状态色标记（成功/警告/危险）。
- 组件：卡片列表 + 状态徽记/图标（可选）。
- 颜色：中性底色 + 状态色条或角标；避免大面积纯色块。
- 字号：项标题 `text-lg ~ xl`，说明 `text-sm`。
- 交互：项 Hover 略抬升，选中/完成有视觉反馈。

7) 对比 / 选择（Compare/Decision）
- 目的：并列对比多个选项（方案、版本、配置）。
- 布局：
  - 2–4 列对比卡片；顶部为名称，主体为特性列表。
  - 支持“推荐”卡高亮（描边/阴影增强）。
- 组件：特性清单（打勾/禁用）、价格/指标位（可选）。
- 颜色：推荐卡用品牌渐变描边或淡色填充突出。
- 字号：名称 `text-2xl`，特性 `text-sm ~ base`。
- 交互：Hover 提升，焦点环清晰。

8) 问答 / FAQ
- 目的：组织常见问题与简明回答。
- 布局：
  - 手风琴或卡片分组；每项“问题（粗体）+ 回答（中性）”。
  - 列表密度适中，便于快速扫读。
- 组件：可折叠项（可选），或静态卡片。
- 颜色：保持中性，问题可用较深色，回答次要色。
- 字号：问题 `text-lg ~ xl font-semibold`，回答 `text-base`。
- 交互：折叠动画平滑；键盘可访问。

9) 行动 / 结束（CTA/End）
- 目的：引导下一步操作或总结性动作。
- 布局：
  - 居中大标题 + 简短文案 + 主按钮 + 次按钮。
  - 可附加说明/链接区域。
- 组件：CTA 按钮（主/次）、联系方式/链接。
- 颜色：主按钮用品牌渐变（文本反白），次按钮玻璃态。
- 字号：标题 `text-4xl ~ 5xl`，正文 `text-base ~ lg`。
- 交互：清晰的 hover/active/focus 状态，按钮阴影可略强。

10) 分隔 / 章节页（Divider/Section）
- 目的：在长序列中分割章节，调整节奏。
- 布局：大号渐变标题 + 简要摘要；可选装饰线/渐变带。
- 组件：渐变标题、轻量说明卡。
- 颜色：品牌渐变用于标题或横向分隔。
- 字号：标题 `text-6xl`，摘要 `text-lg`。

## 组合与变体建议
- 组合：封面 + 目录 +（配置/指标/可视化/清单/对比）× N + CTA。
- 变体：
  - 深色内容容器：在深色背景内嵌浅色卡片（或反之），保持对比。
  - 紧凑/舒展：通过 `gap / px / py` 调整密度以匹配信息量。
  - 轻重标题：通过是否使用渐变标题来控制视觉权重。

## 实施速记（类簇示例）
- 页面外层容器：`container mx-auto max-w-6xl px-6 md:px-8 lg:px-12 py-12 lg:py-16`
- 玻璃态卡片：`bg-white/70 backdrop-blur-md border border-slate-200/30 rounded-3xl shadow-xl p-6 md:p-8`
- 渐变标题：`text-7xl font-black tracking-tight text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 via-fuchsia-400 to-emerald-400`
- 指标数值：`text-6xl font-black tracking-tight`
- Tab 容器：`flex flex-wrap items-center gap-2`
- Tab 项（激活）：`rounded-full bg-gradient-to-r from-indigo-500/20 to-emerald-400/20 border border-white/40 px-4 py-2`
- 深色面板：`bg-slate-900/80 text-slate-100 rounded-2xl border border-white/10 shadow-xl p-6`

## 提示词（供模型生成时参考）
- 「柔和渐变背景、玻璃态卡片、蓝紫—品红—翠绿品牌渐变标题」
- 「中心对齐、超大圆角、留白充足、单行大字号」
- 「卡片化信息层级、Pill 状态按钮、细边与轻阴影」
- 「缓慢渐变流动、元素轻悬浮、平滑过渡、可降级动效」
- 「内容无关模板：封面、目录、配置、指标、可视化、清单、对比、FAQ、CTA、分隔」

以上模板与令牌可直接套用于任意主题内容，在不改变视觉语言的前提下快速生成一致的页面。
