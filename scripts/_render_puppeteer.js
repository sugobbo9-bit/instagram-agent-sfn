
const puppeteer = require('puppeteer');
const fs = require('fs');
const path = require('path');

(async () => {
  const slides = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const outDir = process.argv[3];
  
  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox']
  });
  
  for (let i = 0; i < slides.length; i++) {
    const page = await browser.newPage();
    await page.setViewport({ width: 1080, height: 1350, deviceScaleFactor: 2 });
    await page.setContent(slides[i].html, { waitUntil: 'networkidle0' });
    const outPath = path.join(outDir, `slide_${String(i+1).padStart(2,'0')}.png`);
    await page.screenshot({ path: outPath, type: 'png' });
    await page.close();
    console.log('rendered: ' + outPath);
  }
  
  await browser.close();
})().catch(e => { console.error(e); process.exit(1); });
