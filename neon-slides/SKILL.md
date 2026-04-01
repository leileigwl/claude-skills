---
name: neon-slides
description: >-
  Generate neon-styled HTML slides from JSON data. Supports 10 layout types:
  title, content, metrics, flow, timeline, split, quote, code, table, ending.
  Features glassmorphism cards, gradient animations, particle effects, SVG
  backgrounds. Direct HTML output without PPTX conversion.
disable-model-invocation: false
user-invocable: true
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash
---

# Neon Slides Skill

Generate beautiful neon-styled HTML presentation slides from structured JSON data.

## When to Trigger

Auto-trigger when user mentions:
- "生成 PPT" / "生成幻灯片" / "生成演示"
- "neon slides" / "霓虹风格 PPT"
- HTML slides (not PPTX)
- Daily summary slides, project presentations

## Reference Project

**Location**: `~/Code/Daily/20260326/视频制作sop/workflow/tools/ppt-generator/`

This skill is based on a Vue 3 + Vite slide generator with:
- Neon gradient animations
- Glassmorphism card design
- 16:9 aspect ratio (CSS `aspect-ratio: 16/9`)
- SVG animated backgrounds
- Particle effects

## JSON Data Structure

```json
{
  "title": "Presentation Title",
  "author": "Author Name",
  "slides": [
    // Array of slide objects with different layouts
  ]
}
```

## Layout Types (10 total)

### 1. Title Layout
```json
{
  "layout": "title",
  "headline": "Main Title",
  "subhead": "Subtitle text",
  "tag": "TAG LABEL"
}
```
- Full-screen title with gradient badge
- Animated divider line
- Large headline with subtle glow

### 2. Content Layout
```json
{
  "layout": "content",
  "headline": "Section Title",
  "emphasis": "Highlight Keyword",
  "body": [
    "Bullet point 1",
    "Bullet point 2",
    "Bullet point 3"
  ]
}
```
- Glassmorphism bullet cards
- Diamond markers with accent color
- Keyword highlighting with `：` colon separator
- `emphasis` shows gradient-animated keyword before headline

### 3. Metrics Layout (Big Numbers)
```json
{
  "layout": "metrics",
  "headline": "Data Overview",
  "metrics": [
    { "value": "5", "label": "Projects" },
    { "value": "3", "label": "Tech Stack" }
  ],
  "summary": "Optional summary text"
}
```
- Animated counting numbers
- Glass cards with gradient bottom border
- Grid layout (max 4 columns)
- Compact spacing: `space-y-6`, `gap-4`

### 4. Flow Layout (Process Steps)
```json
{
  "layout": "flow",
  "headline": "Workflow Title",
  "emphasis": "Optional Keyword",
  "steps": [
    "Step 1 description",
    "Step 2 → outcome",
    "Step 3 description"
  ]
}
```
- Numbered steps with colored badges
- Arrow `→` highlighting for flow indicators
- Each step in glass card

### 5. Timeline Layout
```json
{
  "layout": "timeline",
  "headline": "Title — Subtitle",
  "emphasis": "Optional Keyword",
  "events": [
    { "time": "V1", "title": "Event Name", "desc": "Description" },
    { "time": "V2", "title": "Event Name", "desc": "Description" }
  ]
}
```
- Vertical timeline with gradient line
- Dot markers with accent color glow
- Glass cards for each event
- Use `—` in headline for title/subtitle split

### 6. Split Layout (Comparison)
```json
{
  "layout": "split",
  "headline": "Title：Subtitle",
  "left": "Left content\n\nParagraphs",
  "right": "Right content\n\nParagraphs"
}
```
- Two-column comparison
- Left: standard glass card (❌ icon)
- Right: accent glass card (✅ icon)
- Use `：` or `—` in headline for title split

### 7. Quote Layout
```json
{
  "layout": "quote",
  "tag": "INSIGHT",
  "quote": "Quote text here",
  "source": "Optional source attribution"
}
```
- Large decorative quote mark
- Centered italic text
- Gradient badge and divider

### 8. Code Layout
```json
{
  "layout": "code",
  "headline": "Code Example",
  "language": "Python",
  "code": "def hello():\n    print('world')"
}
```
- Terminal-style code block
- macOS window dots (red/yellow/green)
- Green syntax highlighting
- Glass container with blur

### 9. Table Layout
```json
{
  "layout": "table",
  "headline": "Table Title",
  "columns": ["Col1", "Col2", "Col3"],
  "rows": [
    ["Row1-1", "Row1-2", "Row1-3"],
    ["Row2-1", "Row2-2", "Row2-3"]
  ],
  "highlight": [1]  // Column indices to highlight
}
```
- Glass container table
- Accent-colored headers
- Optional column highlighting

### 10. Ending Layout
```json
{
  "layout": "ending",
  "tag": "THANK YOU",
  "headline": "End Title",
  "subhead": "Subtitle or summary"
}
```
- Final slide design
- Gradient animated headline
- Centered badge and divider

## Color Palette (8 Colors)

Auto-selected per slide based on headline hash:
- `#818cf8` - Indigo
- `#fb923c` - Orange
- `#34d399` - Emerald
- `#f43f5e` - Rose
- `#38bdf8` - Sky
- `#fbbf24` - Amber
- `#a855f7` - Purple
- `#f472b6` - Pink

## Key Styling Features

### Glassmorphism Cards
```css
.glass-card {
  background: rgba(255, 255, 255, 0.03);
  backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 20px;
}
```

### Gradient Animation
```css
.accent-gradient-text {
  background: linear-gradient(120deg, #818cf8, #d946ef, #34d399, #38bdf8, #818cf8);
  background-size: 300% 100%;
  animation: gradient-shift 6s ease-in-out infinite;
}
```

### SVG Animated Background
Three gradient circles with slow movement animation (20-30s duration).

### Particle Effects
15 floating particles with color variety and blur glow.

## Text Highlighting Rules

### Colon Pattern (`：`)
```
"关键词：描述内容"
→ Key: accent color, bold
→ Separator: 30% white
→ Description: 55% white, smaller
```

### Bracket Pattern (`「」`)
```
"这是「重点」内容"
→ Brackets + content: accent color, semi-bold
```

### Arrow Pattern (`→`)
```
"步骤 → 结果"
→ Arrow: accent color
→ Before: accent, bold
→ After: 55% white, smaller
```

## Workflow

### Step 1: Gather Content
Ask user for:
- Presentation topic/title
- Key points to cover
- Any specific metrics/timeline/comparison data

### Step 2: Create JSON
Generate structured JSON with appropriate layouts:
- Start with `title` layout
- Use `content` for main points
- Use `metrics` for data overview
- Use `flow` or `timeline` for processes
- Use `split` for comparisons
- End with `ending` layout

### Step 3: Generate HTML
Create standalone HTML file:
- Include all CSS inline
- SVG background embedded
- 16:9 aspect ratio
- Responsive design

### Step 4: Output
Save to user's project directory as `{topic}-slides.html`

## Example: Daily Summary

```json
{
  "title": "Daily Summary",
  "slides": [
    { "layout": "title", "headline": "2026.03.28", "subhead": "Project Updates", "tag": "DAILY" },
    { "layout": "metrics", "headline": "Today's Progress", "metrics": [
      { "value": "3", "label": "Completed" },
      { "value": "2", "label": "In Progress" }
    ]},
    { "layout": "content", "headline": "Key Tasks", "body": [
      "Task 1：Completed feature X",
      "Task 2：Fixed bug in module Y"
    ]},
    { "layout": "ending", "headline": "Tomorrow", "subhead": "Continue with Z", "tag": "END" }
  ]
}
```

## Tips

- Keep slides concise (3-5 bullet points per content slide)
- Use metrics for quick data overview
- Timeline works well for version history/iterations
- Split layout for before/after or problem/solution
- One accent color per slide (auto-selected)
- Reserve gradient animation for emphasis keywords only
