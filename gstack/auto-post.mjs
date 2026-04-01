import { chromium } from 'playwright';
import path from 'path';

(async () => {
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

  // 找到发布框
  const textarea = await page.locator('textarea, [contenteditable="true"]').first();
  if (await textarea.count() > 0) {
    await textarea.click();
    await page.waitForTimeout(500);
    await textarea.fill(`我做了一个让 AI 记住你的工具。

Memory Local — 你的 AI 第二大脑。

它会从你的所有历史对话中学习你的思维模式、工作习惯、纠正过的错误。下次对话自动加载，AI 越用越懂你。

开源免费：github.com/leileigwl/memory_local`);

    console.log('✅ 微博内容已填入！请手动点击发布按钮');
  } else {
    console.log('❌ 未找到发布框，可能未登录');
  }

  await page.waitForTimeout(5000);

  // === 小红书发布 ===
  console.log('\n=== 小红书 ===');
  await page.goto('https://www.xiaohongshu.com', { waitUntil: 'domcontentloaded' });
  await page.waitForTimeout(3000);

  console.log('小红书需要上传图片才能发布，请手动操作...');

  console.log('\n========================================');
  console.log('浏览器保持打开，请在浏览器中完成发布');
  console.log('按 Ctrl+C 关闭脚本');
  console.log('========================================\n');

  // 保持浏览器打开
  await new Promise(() => {});
})();