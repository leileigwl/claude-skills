# 如何使用 Vite + TypeScript + Tailwind 初始化 Vue 3 项目

## 1. 安装 Node.js

### macOS
下载并安装 nvm：
```bash
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
```

加载 nvm：
```bash
. "$HOME/.nvm/nvm.sh"
```

下载并安装 Node.js 22：
```bash
nvm install 22
```

验证 Node.js 版本：
```bash
node -v # 应输出 "v22.19.0"
```

验证 npm 版本：
```bash
npm -v # 应输出 "10.9.3"
```

### Windows
下载并安装 Chocolatey：
```powershell
powershell -c "irm https://community.chocolatey.org/install.ps1|iex"
```

下载并安装 Node.js 22：
```bash
choco install nodejs --version="22.19.0"
```

验证 Node.js 版本：
```bash
node -v # 应输出 "v22.19.0"
```

验证 npm 版本：
```bash
npm -v # 应输出 "10.9.3"
```

## 2. 创建项目
```bash
npm create vue@latest
```
选择选项：
- Framework: Vue
- Add TypeScript: Yes
- Add JSX Support: No
- Add Router: Yes
- Add Pinia: Yes
- Add Vitest: No
- Add End-to-End Testing: No
- Add ESLint: No
- Add Prettier: No

（Vite 已默认集成，无需额外安装）

## 3. 安装 Tailwind CSS
```bash
npm install -D tailwindcss postcss autoprefixer
npx tailwindcss init
```

## 4. 配置 Tailwind
在 `tailwind.config.js` 中添加：
```js
module.exports = {
  content: ["./index.html", "./src/**/*.{vue,js,ts,jsx,tsx}"],
  theme: {
    extend: {}
  },
  plugins: []
}
```

在 `src/main.ts` 中导入：
```ts
import './style.css'
```

## 5. 启动开发服务器
```bash
npm run dev
```

项目已就绪，可在 `http://localhost:5173` 访问。