const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: 1280, height: 900 } });
  const pages = [
    { url: 'visa.html', name: 'visa' },
    { url: 'travel.html', name: 'travel' },
    { url: 'support.html', name: 'support' },
    { url: 'counseling.html', name: 'counseling' },
  ];

  const outDir = path.join(__dirname, 'screenshots');

  for (const p of pages) {
    const page = await context.newPage();
    await page.goto(`http://localhost:8888/${p.url}`, { waitUntil: 'networkidle' });
    
    // Banner/title screenshot
    await page.screenshot({ path: path.join(outDir, `40-${p.name}-banner.png`), clip: { x: 0, y: 300, width: 1280, height: 400 } });
    console.log(`Screenshot: 40-${p.name}-banner.png`);
    
    // Content screenshot
    await page.evaluate(() => window.scrollTo(0, 450));
    await page.waitForTimeout(300);
    await page.screenshot({ path: path.join(outDir, `41-${p.name}-content.png`), clip: { x: 0, y: 0, width: 1280, height: 700 } });
    console.log(`Screenshot: 41-${p.name}-content.png`);
    
    await page.close();
  }

  await browser.close();
  console.log('All service page verification screenshots saved!');
})();
