 在src/presentations/ai-skill-tree内完成这个ppt项目

风格上请参考同级目录的 qwen3-next-bench

# 整体要求：
- 参考design-language-template 使用翻页组件库，但样式可以自己设计
- 首先完成Index.vue，并且把它加入路由 ./src/router/index.vue
- 其次把它添加到 Home.vue里，放在AI邪修PPT的目录里
- 采用和design-language-template同样的命名规则
- 只使用共享组件
- 所有的页面应该使用背景组件的功能（不要带背景色）



# Page 1 标题页
参考 qwen3-next-bench 的title 页，用多行文本来显示标题和副标题
主标题：你不是在学做PPT
副标题：你是在点亮AI的隐藏技能树
其中AI的隐藏技能树，需要用彩色文字加大加粗处理（标题页风格）


# Page 2 

简述AI做PPT的三个痛点
- 质量随机
- 同质化，依赖模板
- 不好修改

# Page 3
AI做PPT的本质就是做网页
但更底层的能力是Coding和In Context Learning

# Page 4
顶层标题：能驱动AI各层能力的人群划分
下方用SVG画一个巨大的等边三角形
三角形分三层：
- 第一层：有1个用户图标的svg代表一个人（svg:上边圆形下边半圆表示用户）
- 第二层：有3个用户图标
- 第三层：有9个用户图标

在三角形的左侧有左对齐的三行文字分别对应三层，它们分别是
- Coding&In Context Learning
- Tools
- Chatbot

# Page 5
巨大红色标题：别怕
下方是黑色副标题：驱动AI的代码能力（不等号）让你写代码

其中（不等号）让你写代码需要比同一行的字大一号，并且更粗
（不等号）要用符号表示

# Page 6
这一页展示用AI做PPT的流程
在顶部有四个流程，请你用四个连接剪头的图来表示
-  1.写页面规划
-  2.发给chatbot(codex or claude code)
-  3.观察效果反馈给chatbot
-  4.把错误复制给chabot
上面区域不要占用很大
下方是三张图的轮播循环
slide-5-1.png
slide-5-2.png
slide-5-3.png
轮播效果应该是水平顺时针旋转
显示的图最大，不显示的图转到后面（用变小来模拟渐远效果）
可以用纯样式实现不要用threejs

点击流程的1，2转到slide-5-1.png
点击流程的3，转到slide-5-2
流程4，5-3

# Page 7
参考 qwen3-next-bench/slide-3-env.vue

## 环境
nodejs(最新版)
```
# Download and install Chocolatey:
powershell -c "irm https://community.chocolatey.org/install.ps1|iex"
# Download and install Node.js:
choco install nodejs --version="22.19.0"
# Verify the Node.js version:
node -v # Should print "v22.19.0".
# Verify npm version:
npm -v # Should print "10.9.3".
```
## 使用框架
- vue3（我提供的工程）
- react
## 使用工具
- Cursor（订阅）
- Codex （ChatGPT 订阅，我自己使用的）
- Claude Code（配合 kimi-k2-0905或者GLM4.5）
- Claude Code+本地模型
## 模型使用场景
- 整体框架生成：订阅模型（claude,gpt5）
- 页面修改：可以用Claude Code+国产模型（kimi,glm)
- 特别小的修改：可以用本地部署的模型配合Claude Code
## 示例工程
```
git clone https://github.com/xiaotianfotos/vue_ppt
cd vue_ppt
npm install
npm run dev
```

# Page 8
标题 红色的大字 DEMO

# page 9
标题：目录结构就是AI的知识库
左侧只保留标题与一句提示，右侧展示 ai-skill-tree 目录的结构图，不要底部信息块。

# Page 10
标题：一个页面一个文件
副标题：改一个文件开一个会话、上下文小、更有效修改

# Page 12
标题：模板设计先行
副标题：学习(copy)好的设计，截图给codex，让它生成模板，然后用模板（目录）指点AI生成ppt

# Page 12
标题：组件复用
副标题：更多的功能可以让AI生成组件（例如背景，多语言化），放在shared里给未来的文稿用

# Page 13
标题：删除而不是重做
副标题：直接删除重做，不要改

# Page 14
标题：忘掉软件工程（邪修AI）
副标题：即用即抛、抽卡式生成、不看代码只看效果

# Page 15
标题：学习一些前端知识
副标题：只是为了更好指导AI（你需要知道一些术语）

# Page 16
标题： 学会一种思维：用AI+代码解决一切问题
副标题：代码不再是程序员专属工具了

# Page 17
标题：如果有用，点赞+关注
副标题：这只是AI邪修系列的开始



