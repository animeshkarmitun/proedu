const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: 1280, height: 900 } });
  const page = await context.newPage();

  const baseUrl = 'http://localhost:8888';
  const outDir = path.join(__dirname, 'screenshots');

  await page.goto(`${baseUrl}/index.htm`, { waitUntil: 'networkidle' });

  // 1. Full page
  await page.screenshot({ path: path.join(outDir, '20-after-full.png'), fullPage: true });
  console.log('Screenshot: 20-after-full.png');

  // 2. Header
  await page.screenshot({ path: path.join(outDir, '21-after-header.png'), clip: { x: 0, y: 0, width: 1280, height: 150 } });
  console.log('Screenshot: 21-after-header.png');

  // 3. Hero
  await page.screenshot({ path: path.join(outDir, '22-after-hero.png'), clip: { x: 0, y: 150, width: 1280, height: 650 } });
  console.log('Screenshot: 22-after-hero.png');

  // 4. Mission
  await page.evaluate(() => window.scrollTo(0, 700));
  await page.waitForTimeout(400);
  await page.screenshot({ path: path.join(outDir, '23-after-mission.png'), clip: { x: 0, y: 0, width: 1280, height: 700 } });
  console.log('Screenshot: 23-after-mission.png');

  // 5. Vision
  await page.evaluate(() => window.scrollTo(0, 1500));
  await page.waitForTimeout(400);
  await page.screenshot({ path: path.join(outDir, '24-after-vision.png'), clip: { x: 0, y: 0, width: 1280, height: 700 } });
  console.log('Screenshot: 24-after-vision.png');

  // 6. Services
  await page.evaluate(() => window.scrollTo(0, 2400));
  await page.waitForTimeout(400);
  await page.screenshot({ path: path.join(outDir, '25-after-services.png'), clip: { x: 0, y: 0, width: 1280, height: 900 } });
  console.log('Screenshot: 25-after-services.png');

  // 7. Footer
  await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight));
  await page.waitForTimeout(400);
  await page.screenshot({ path: path.join(outDir, '26-after-footer.png'), clip: { x: 0, y: 0, width: 1280, height: 900 } });
  console.log('Screenshot: 26-after-footer.png');

  await browser.close();
  console.log('All verification screenshots saved!');
})();
