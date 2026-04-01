const { chromium } = require('playwright');
const path = require('path');

(async () => {
  // 使用用户数据目录保留登录状态
  const userDataDir = path.join(process.env.HOME, 'Library', 'Application Support', 'Google', 'Chrome');

  console.log('启动浏览器...');
  console.log('注意：请确保你已经手动登录微博、小红书等平台');

  const browser = await chromium.launchPersistentContext('/tmp/chrome-debug-profile', {
    headless: false,
    viewport: { width: 1400, height: 1000 },
    channel: 'chrome',
    args: ['--disable-blink-features=AutomationControlled']
  });

  const page = browser.pages()[0] || await browser.newPage();

  // === 微博发布 ===
  console.log('\n=== 微博 ===');
  await page.goto('https://weibo.com', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(3000);

  // 检查登录状态
  let weiboLoggedIn = false;
  try {
    await page.waitForSelector('[class*="publish"]', { timeout: 5000 });
    weiboLoggedIn = true;
  } catch (e) {
    console.log('微博可能未登录，请手动登录');
  }

  if (weiboLoggedIn) {
    console.log('微博已登录');

    // 找到发布框
    const textarea = await page.locator('textarea, [contenteditable="true"]').first();
    if (await textarea.count() > 0) {
      await textarea.click();
      await page.waitForTimeout(500);
      await textarea.fill(`我做了一个让 AI 记住你的工具。

Memory Local — 你的 AI 第二大脑。

它会从你的所有历史对话中学习你的思维模式、工作习惯、纠正过的错误。下次对话自动加载，AI 越用越懂你。

开源免费：github.com/leileigwl/memory_local`);

      console.log('微博内容已填入！');
      console.log('请手动点击发布按钮...');
    }
  }

  await page.waitForTimeout(5000);

  // === 小红书发布 ===
  console.log('\n=== 小红书 ===');
  await page.goto('https://www.xiaohongshu.com', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(3000);

  // 检查登录状态 - 小红书有创建按钮表示已登录
  try {
    const createBtn = page.locator('[class*="create"], [class*="publish"]').first();
    if (await createBtn.count() > 0) {
      console.log('小红书已登录');
      console.log('小红书需要上传图片才能发布，请手动操作...');
    } else {
      console.log('小红书可能未登录');
    }
  } catch (e) {
    console.log('小红书操作出错');
  }

  console.log('\n========================================');
  console.log('脚本执行完毕，浏览器保持打开状态');
  console.log('请在浏览器中完成剩余发布操作');
  console.log('按 Ctrl+C 关闭脚本');
  console.log('========================================\n');

  // 保持浏览器打开
  await new Promise(() => {});
})();