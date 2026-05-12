const { chromium } = require('playwright');
const path = require('path');

(async () => {
  const browser = await chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport: { width: 1280, height: 900 } });
  const pages = [
    { url: 'australia.html', name: 'australia' },
    { url: 'visa.html', name: 'visa' },
    { url: 'travel.html', name: 'travel' },
  ];

  const outDir = path.join(__dirname, 'screenshots');

  for (const p of pages) {
    const page = await context.newPage();
    await page.goto(`http://localhost:8888/${p.url}`, { waitUntil: 'networkidle' });
    
    // Header screenshot
    await page.screenshot({ path: path.join(outDir, `30-${p.name}-header.png`), clip: { x: 0, y: 0, width: 1280, height: 150 } });
    console.log(`Screenshot: 30-${p.name}-header.png`);
    
    // Footer screenshot (scroll to bottom)
    await page.evaluate(() => window.scrollTo(0, document.body.scrollHeight - 900));
    await page.waitForTimeout(500);
    await page.screenshot({ path: path.join(outDir, `31-${p.name}-footer.png`), clip: { x: 0, y: 0, width: 1280, height: 950 } });
    console.log(`Screenshot: 31-${p.name}-footer.png`);
    
    await page.close();
  }

  await browser.close();
  console.log('All page verification screenshots saved!');
})();
