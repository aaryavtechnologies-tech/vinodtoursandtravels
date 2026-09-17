const {chromium}=require('playwright');
const fs=require('fs');
(async()=>{
 const b=await chromium.launch({headless:true}); const p=await b.newPage();const issues=[];
 const pages=fs.readdirSync('dist').filter(x=>x.endsWith('.html'));
 p.on('pageerror',e=>issues.push({error:e.message}));
 for(const width of [320,390,768,1024,1440]) {
  await p.setViewportSize({width,height:1000});
  for(const file of pages) {
   await p.goto('http://127.0.0.1:8765/'+file);
   await p.locator('img[loading=lazy]').evaluateAll(xs=>xs.forEach(x=>x.loading='eager'));
   await p.evaluate(async()=>{await document.fonts.ready;await Promise.all([...document.images].filter(x=>x.src).map(x=>x.decode().catch(()=>{})))});
   const errors=await p.evaluate(()=>({broken:[...document.images].filter(x=>x.getAttribute('src')&&!x.naturalWidth).map(x=>x.getAttribute('src')),overflow:[...document.querySelectorAll('body *')].filter(x=>{const r=x.getBoundingClientRect();const s=getComputedStyle(x);return r.width&&s.visibility!=='hidden'&&(r.right>innerWidth+2||r.left< -2)&&!x.closest('.skip-link,dialog')}).slice(0,8).map(x=>x.tagName+'.'+x.className)}));
   if(errors.broken.length||errors.overflow.length)issues.push({width,file,...errors});
   if(file==='index.html'&&[390,1440].includes(width)) {
    await p.screenshot({path:`reference/home-${width}.png`});
    await p.locator('.company-section').screenshot({path:`reference/company-${width}.png`});
    await p.locator('.journey-section').screenshot({path:`reference/journey-${width}.png`});
   }
  }
 }
 await p.setViewportSize({width:390,height:844});await p.goto('http://127.0.0.1:8765/');
 await p.locator('.navbar-toggler').click();if(await p.locator('.navbar-toggler').getAttribute('aria-expanded')!=='true')throw Error('Menu did not open');
 await p.locator('.dropdown-toggle').nth(1).click();await p.getByRole('link',{name:'Lansdowne',exact:true}).first().click();if(!p.url().includes('lansdowne'))throw Error('Destination menu');
 await p.goto('http://127.0.0.1:8765/');await p.locator('.company-photo-frame').click();if(!await p.locator('.photo-dialog').isVisible())throw Error('Gallery not open');await p.locator('.gallery-next').click();await p.keyboard.press('Escape');if(await p.locator('.photo-dialog').isVisible())throw Error('Gallery did not close');
 await p.goto('http://127.0.0.1:8765/plan-my-trip.html');
 for(const [id,value] of Object.entries({name:'Layout test',phone:'9876543210',pickup:'Kotdwara',destination:'Lansdowne',date:'2027-01-15'}))await p.locator('#'+id).fill(value);
 await p.locator('button[type=submit]').click();const href=await p.locator('.success-message a').getAttribute('href');if(!href.includes('918076069722')||!decodeURIComponent(href).includes('Kotdwara'))throw Error('Enquiry link');
 await p.goto('http://127.0.0.1:8765/faq.html');await p.locator('summary').first().click();if(!await p.locator('details').first().getAttribute('open').then(x=>x!==null))throw Error('FAQ');
 await p.goto('http://127.0.0.1:8765/');
 const content=await p.evaluate(()=>({heading:document.querySelector('h1').textContent,sections:[...document.querySelectorAll('main>section')].map(x=>x.id),unillustrated:document.querySelectorAll('.destination-card:not(:has(img))').length,vehicles:[...document.querySelectorAll('.vehicle-section img')].map(x=>({src:x.getAttribute('src'),fit:getComputedStyle(x).objectFit}))}));
 if(!content.heading.includes('Delhi, Jaipur')||content.unillustrated)throw Error('Featured tours or package images missing');
 if(!(content.sections.indexOf('heritage-tours')<content.sections.indexOf('mountain-city-tours')&&content.sections.indexOf('mountain-city-tours')<content.sections.indexOf('uttarakhand-tours')))throw Error('Package order incorrect');
 for(const n of [40,41,42,43])if(!content.vehicles.some(v=>v.src.endsWith(`travel-${n}.jpeg`)&&v.fit==='contain'))throw Error('Full vehicle photo missing');
 await p.locator('.vehicle-section [data-gallery-src]').first().click();if(!await p.locator('.photo-dialog').isVisible())throw Error('Vehicle gallery failed');
 if(!(await p.locator('.photo-dialog>img').getAttribute('src')).endsWith('travel-40.jpeg'))throw Error('Wrong vehicle opened');
 console.log(JSON.stringify({pages:pages.length,widths:[320,390,768,1024,1440],issues,interactions:'passed',packageOrder:'passed',vehiclePhotos:'passed'},null,2));fs.writeFileSync('reference/ui-results.json',JSON.stringify(issues,null,2));process.exitCode = issues.length ? 1 : 0; await b.close();
})().catch(e=>{console.error(e);process.exit(1)});

