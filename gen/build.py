#!/usr/bin/env python3
"""JR Refrigeration site generator. Run: python3 gen/build.py  (writes into repo root)."""
import os, html, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAIN = "https://jrrefrigerationac.com"
PHONE = "(210) 946-0246"; TEL = "+12109460246"
FORM_EMAIL = "gr3742780@gmail.com"
YEAR = datetime.date.today().year

def t(en, es=None):
    """Bilingual span: English shown, Spanish swapped in by the toggle."""
    if not es: return en
    return f'<span data-es="{html.escape(es, quote=True)}">{en}</span>'

# ---------------------------------------------------------------- CSS
CSS = r"""
:root{--navy:#0a2342;--navy2:#123a6b;--blue:#1565d8;--blue2:#0f4fb0;--sky:#e8f1fd;--red:#d7263d;--red2:#b51e31;--gold:#ffb703;--ink:#172033;--muted:#5b6b7f;--line:#e3e8ef;--bg:#f6f8fb;--white:#fff;--r:14px;--sh:0 10px 30px rgba(10,35,66,.10);--sh2:0 18px 50px rgba(10,35,66,.16)}
*{box-sizing:border-box}html{scroll-behavior:smooth}
body{margin:0;font-family:Inter,system-ui,-apple-system,"Segoe UI",Roboto,Arial,sans-serif;color:var(--ink);background:var(--white);line-height:1.6;-webkit-font-smoothing:antialiased}
h1,h2,h3,h4{font-family:Montserrat,Inter,sans-serif;line-height:1.15;margin:0 0 .5em;color:var(--navy);letter-spacing:-.01em}
h1{font-size:clamp(2rem,4.2vw,3.3rem);font-weight:800}h2{font-size:clamp(1.6rem,3vw,2.4rem);font-weight:800}h3{font-size:1.2rem;font-weight:700}
p{margin:0 0 1em}a{color:var(--blue)}img{max-width:100%;height:auto;display:block}
.wrap{max-width:1180px;margin:0 auto;padding:0 20px}
.eyebrow{display:inline-block;font-weight:700;font-size:.8rem;letter-spacing:.14em;text-transform:uppercase;color:var(--blue);margin-bottom:10px}
.lead{font-size:1.12rem;color:var(--muted)}
.btn{display:inline-flex;align-items:center;justify-content:center;gap:8px;padding:14px 24px;border-radius:10px;font-weight:700;text-decoration:none;border:2px solid transparent;cursor:pointer;font-size:1rem;transition:.18s;font-family:inherit;line-height:1.2}
.btn-red{background:var(--red);color:#fff}.btn-red:hover{background:var(--red2);transform:translateY(-1px)}
.btn-blue{background:var(--blue);color:#fff}.btn-blue:hover{background:var(--blue2);transform:translateY(-1px)}
.btn-white{background:#fff;color:var(--navy)}.btn-white:hover{background:var(--sky)}
.btn-ghost{background:transparent;color:#fff;border-color:rgba(255,255,255,.5)}.btn-ghost:hover{border-color:#fff;background:rgba(255,255,255,.08)}
.btn-lg{padding:17px 30px;font-size:1.08rem}
.ico{width:1.2em;height:1.2em;fill:currentColor;flex:none}
/* top bar + header */
.topbar{background:var(--navy);color:#cfe0ff;font-size:.86rem}
.topbar .wrap{display:flex;justify-content:space-between;align-items:center;gap:12px;min-height:36px}
.topbar a{color:#fff;text-decoration:none;font-weight:600}
.topbar .left{display:flex;gap:18px;align-items:center}
header.site{position:sticky;top:0;z-index:50;background:#fff;box-shadow:0 2px 14px rgba(10,35,66,.08)}
header.site .wrap{display:flex;align-items:center;gap:20px;min-height:76px}
.logo{display:flex;align-items:center;gap:10px;text-decoration:none;color:var(--navy)}
.logo .mark{width:44px;height:44px;border-radius:10px;background:linear-gradient(135deg,var(--navy),var(--blue));display:grid;place-items:center;color:#fff;font-family:Montserrat;font-weight:900;font-size:1.15rem;letter-spacing:-.04em}
.logo .name{font-family:Montserrat;font-weight:900;font-size:1.25rem;line-height:1;letter-spacing:-.02em}
.logo .name small{display:block;font-size:.62rem;font-weight:700;letter-spacing:.16em;color:var(--red);margin-top:3px}
nav.main{margin-left:auto;display:flex;gap:4px;align-items:center}
nav.main a{color:var(--ink);text-decoration:none;font-weight:600;padding:10px 12px;border-radius:8px;font-size:.95rem}
nav.main a:hover,nav.main a.active{background:var(--sky);color:var(--blue2)}
.hdr-cta{display:flex;align-items:center;gap:10px}
.hdr-phone{display:flex;flex-direction:column;align-items:flex-end;text-decoration:none;color:var(--navy);line-height:1.1}
.hdr-phone small{font-size:.7rem;color:var(--muted);font-weight:600;text-transform:uppercase;letter-spacing:.08em}
.hdr-phone b{font-family:Montserrat;font-size:1.2rem;font-weight:800;white-space:nowrap}
.lang{border:1.5px solid var(--line);background:#fff;border-radius:999px;padding:6px 12px;font-weight:700;font-size:.8rem;cursor:pointer;color:var(--navy);font-family:inherit}
.lang:hover{border-color:var(--blue)}
.burger{display:none;background:none;border:0;width:44px;height:44px;cursor:pointer;color:var(--navy)}
.burger .ico{width:28px;height:28px}
/* hero */
.hero{position:relative;color:#fff;background:var(--navy);overflow:hidden}
.hero .bg{position:absolute;inset:0;background-size:cover;background-position:center;opacity:.55}
.hero .shade{position:absolute;inset:0;background:linear-gradient(100deg,rgba(10,35,66,.97) 0%,rgba(10,35,66,.86) 42%,rgba(10,35,66,.38) 100%)}
.hero .wrap{position:relative;display:grid;grid-template-columns:1.15fr .85fr;gap:48px;padding:72px 20px;align-items:center}
.hero h1{color:#fff;margin-bottom:16px}.hero h1 em{font-style:normal;color:var(--gold)}
.hero .lead{color:#dbe7fb;font-size:1.18rem;max-width:560px}
.hero ul.checks{list-style:none;padding:0;margin:22px 0 28px;display:grid;gap:10px}
.hero ul.checks li{display:flex;gap:10px;align-items:flex-start;font-weight:600}
.hero ul.checks .ico{color:var(--gold);margin-top:3px}
.hero .actions{display:flex;gap:12px;flex-wrap:wrap;align-items:center}
.hero .mini{font-size:.9rem;color:#cfe0ff;margin-top:14px}
.form-card{background:#fff;color:var(--ink);border-radius:18px;padding:28px;box-shadow:var(--sh2)}
.form-card h3{font-size:1.35rem;margin-bottom:4px}
.form-card .sub{color:var(--muted);font-size:.92rem;margin-bottom:16px}
.form-card label{display:block;font-size:.82rem;font-weight:700;color:var(--navy);margin:12px 0 5px}
.form-card input,.form-card select,.form-card textarea{width:100%;padding:12px 13px;border:1.5px solid var(--line);border-radius:10px;font:inherit;font-size:.98rem;background:#fbfcfe;transition:.15s}
.form-card input:focus,.form-card select:focus,.form-card textarea:focus{outline:none;border-color:var(--blue);box-shadow:0 0 0 3px rgba(21,101,216,.15);background:#fff}
.form-card .row{display:grid;grid-template-columns:1fr 1fr;gap:12px}
.form-card .btn{width:100%;margin-top:16px}
.form-card .fine{font-size:.76rem;color:var(--muted);margin:10px 0 0;text-align:center}
.hp{position:absolute;left:-9999px;opacity:0;height:0;width:0}
/* trust strip */
.trust{background:var(--sky);border-bottom:1px solid var(--line)}
.trust .wrap{display:grid;grid-template-columns:repeat(4,1fr);gap:18px;padding:22px 20px}
.trust .item{display:flex;gap:12px;align-items:center}
.trust .item .ico{width:34px;height:34px;color:var(--blue);flex:none}
.trust .item b{display:block;color:var(--navy);font-family:Montserrat;font-size:.98rem}
.trust .item span{font-size:.85rem;color:var(--muted)}
/* sections */
section{padding:72px 0}section.alt{background:var(--bg)}
.sec-head{max-width:720px;margin-bottom:38px}.sec-head.center{text-align:center;margin-left:auto;margin-right:auto}
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}.grid2{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}
.card{background:#fff;border:1px solid var(--line);border-radius:var(--r);padding:26px;transition:.2s;position:relative;display:flex;flex-direction:column}
.card:hover{box-shadow:var(--sh);transform:translateY(-3px);border-color:#cfdcf2}
.card .icon{width:54px;height:54px;border-radius:12px;background:var(--sky);display:grid;place-items:center;color:var(--blue);margin-bottom:16px}
.card .icon .ico{width:28px;height:28px}
.card p{color:var(--muted);font-size:.96rem;flex:1}
.card .more{font-weight:700;text-decoration:none;display:inline-flex;gap:6px;align-items:center;color:var(--blue)}
.card a.cover{position:absolute;inset:0}
.photo{border-radius:var(--r);overflow:hidden;box-shadow:var(--sh)}
.photo img{width:100%;height:100%;object-fit:cover;aspect-ratio:4/3}
ul.ticks{list-style:none;padding:0;margin:18px 0}ul.ticks li{display:flex;gap:10px;margin:9px 0;align-items:flex-start}ul.ticks .ico{color:var(--blue);margin-top:4px;width:20px;height:20px}
.steps{display:grid;grid-template-columns:repeat(3,1fr);gap:22px;counter-reset:s}
.step{background:#fff;border-radius:var(--r);padding:28px;border:1px solid var(--line);position:relative}
.step .n{width:42px;height:42px;border-radius:50%;background:var(--navy);color:var(--gold);font-family:Montserrat;font-weight:800;display:grid;place-items:center;margin-bottom:14px;font-size:1.1rem}
.step p{color:var(--muted);margin:0}
.band{background:linear-gradient(120deg,var(--red) 0%,#a4152a 100%);color:#fff;text-align:center;padding:60px 0}
.band h2{color:#fff}.band .big{font-family:Montserrat;font-weight:900;font-size:clamp(1.6rem,4vw,2.6rem);color:var(--gold);margin:8px 0}
.band p{color:#ffe3e7;max-width:640px;margin:0 auto 1em}
.band.blue{background:linear-gradient(120deg,var(--navy) 0%,var(--blue) 100%)}.band.blue p{color:#dbe7fb}
.map{border-radius:var(--r);overflow:hidden;box-shadow:var(--sh);border:1px solid var(--line)}
.map iframe{width:100%;height:380px;border:0;display:block}
.cities{display:grid;grid-template-columns:repeat(3,1fr);gap:8px 18px;list-style:none;padding:0;margin:16px 0 0}
.cities li{display:flex;gap:8px;align-items:center;font-weight:600;color:var(--navy)}
.cities .ico{color:var(--red);width:16px;height:16px}
.faq{max-width:820px;margin:0 auto}
.faq details{border:1px solid var(--line);border-radius:12px;background:#fff;margin-bottom:10px;padding:0 20px}
.faq summary{cursor:pointer;font-weight:700;color:var(--navy);padding:16px 0;list-style:none;display:flex;justify-content:space-between;align-items:center;gap:12px;font-family:Montserrat}
.faq summary::-webkit-details-marker{display:none}.faq summary::after{content:"+";font-size:1.4rem;color:var(--blue);font-weight:400}
.faq details[open] summary::after{content:"–"}.faq details p{color:var(--muted);padding-bottom:16px;margin:0}
.cta-final .wrap{display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center}
.cta-final h2{color:#fff}.cta-final{background:var(--navy);color:#dbe7fb}
/* page hero (subpages) */
.phero{background:var(--navy);color:#fff;position:relative;overflow:hidden}
.phero .bg{position:absolute;inset:0;background-size:cover;background-position:center;opacity:.5}
.phero .shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(10,35,66,.96),rgba(10,35,66,.45))}
.phero .wrap{position:relative;padding:60px 20px}.phero h1{color:#fff}.phero .lead{color:#dbe7fb;max-width:640px}
.crumbs{font-size:.85rem;color:#9fb8de;margin-bottom:14px}.crumbs a{color:#cfe0ff;text-decoration:none}
.content{display:grid;grid-template-columns:1fr 380px;gap:48px;align-items:start}
.content .main h2{margin-top:1.4em}.content .main h2:first-child{margin-top:0}
.side{position:sticky;top:96px}.side .form-card{padding:24px}
.callout{background:var(--sky);border-left:5px solid var(--blue);padding:18px 20px;border-radius:0 12px 12px 0;margin:22px 0}
.tags{display:flex;flex-wrap:wrap;gap:8px;margin:14px 0}.tags span{background:var(--sky);color:var(--navy2);font-weight:700;padding:6px 12px;border-radius:999px;font-size:.85rem}
/* footer */
footer.site{background:#071a33;color:#aebdd6;padding:56px 0 100px;font-size:.93rem}
footer.site .cols{display:grid;grid-template-columns:1.4fr 1fr 1fr 1.2fr;gap:36px}
footer.site h4{color:#fff;font-size:.95rem;margin-bottom:12px;letter-spacing:.06em;text-transform:uppercase}
footer.site a{color:#dbe7fb;text-decoration:none}footer.site a:hover{color:var(--gold)}
footer.site ul{list-style:none;padding:0;margin:0}footer.site li{margin:7px 0}
footer.site .phone{font-family:Montserrat;font-weight:800;font-size:1.3rem;color:#fff;display:block;margin:6px 0}
footer.site .bottom{border-top:1px solid rgba(255,255,255,.1);margin-top:36px;padding-top:18px;display:flex;justify-content:space-between;gap:12px;flex-wrap:wrap;font-size:.8rem;color:#7f93b8}
/* sticky mobile bar */
.mbar{display:none;position:fixed;bottom:0;left:0;right:0;z-index:60;background:#fff;border-top:1px solid var(--line);padding:10px 12px;gap:10px;box-shadow:0 -6px 20px rgba(10,35,66,.12)}
.mbar .btn{flex:1;padding:13px 10px}
/* responsive */
@media(max-width:1180px){nav.main a{padding:8px 7px;font-size:.86rem}.hdr-cta .btn{display:none}.logo .name{font-size:1.05rem}.hdr-phone b{font-size:1.05rem}header.site .wrap{gap:12px}}
@media(max-width:1000px){.hero .wrap{grid-template-columns:1fr;gap:34px;padding:52px 20px}.trust .wrap{grid-template-columns:1fr 1fr}.grid3{grid-template-columns:1fr 1fr}.steps{grid-template-columns:1fr}.content{grid-template-columns:1fr}.side{position:static}footer.site .cols{grid-template-columns:1fr 1fr}.cta-final .wrap{grid-template-columns:1fr}}
@media(max-width:980px){nav.main{display:none;position:absolute;top:76px;left:0;right:0;background:#fff;flex-direction:column;align-items:stretch;padding:10px 16px 16px;box-shadow:0 14px 30px rgba(10,35,66,.15)}nav.main.open{display:flex}nav.main a{padding:13px 10px;border-bottom:1px solid var(--line)}.burger{display:block}.hdr-phone{display:none}.topbar .left span.sec{display:none}}
@media(max-width:640px){.grid3,.grid2,.trust .wrap,.cities,footer.site .cols{grid-template-columns:1fr}.form-card .row{grid-template-columns:1fr}section{padding:52px 0}.mbar{display:flex}.hdr-cta .btn{display:none}.topbar .wrap{justify-content:center}.topbar .left{display:none}}
"""

# ---------------------------------------------------------------- JS
JS = r"""
(function(){
  var KEY='jr_lang';
  function setLang(l){
    document.querySelectorAll('[data-es]').forEach(function(el){
      if(!el.dataset.en) el.dataset.en=el.innerHTML;
      el.innerHTML = l==='es' ? el.dataset.es : el.dataset.en;
    });
    document.querySelectorAll('[data-es-ph]').forEach(function(el){
      if(!el.dataset.enPh) el.dataset.enPh=el.placeholder||'';
      el.placeholder = l==='es' ? el.dataset.esPh : el.dataset.enPh;
    });
    document.documentElement.lang = l;
    document.querySelectorAll('.lang').forEach(function(b){ b.textContent = l==='es' ? 'English' : 'Español'; });
    try{ localStorage.setItem(KEY,l); }catch(e){}
  }
  var saved='en'; try{ saved=localStorage.getItem(KEY)||'en'; }catch(e){}
  if(saved==='es') setLang('es');
  document.querySelectorAll('.lang').forEach(function(b){
    b.addEventListener('click',function(){ setLang(document.documentElement.lang==='es'?'en':'es'); });
  });
  var bg=document.querySelector('.burger'), nav=document.querySelector('nav.main');
  if(bg&&nav) bg.addEventListener('click',function(){ nav.classList.toggle('open'); });
  document.querySelectorAll('form[data-lead]').forEach(function(f){
    f.addEventListener('submit',function(){ var b=f.querySelector('button[type=submit]'); if(b){ b.disabled=true; b.textContent='Sending…'; } });
  });
  if(location.protocol==='http:'&&location.hostname.indexOf('localhost')<0&&location.hostname!=='127.0.0.1'){ location.replace('https://'+location.host+location.pathname+location.search); }
})();
"""

# ---------------------------------------------------------------- icons
I = {
 "phone": '<svg class="ico" viewBox="0 0 24 24"><path d="M6.6 10.8a15.1 15.1 0 0 0 6.6 6.6l2.2-2.2a1 1 0 0 1 1-.25c1.1.37 2.3.57 3.6.57a1 1 0 0 1 1 1V20a1 1 0 0 1-1 1A17 17 0 0 1 3 4a1 1 0 0 1 1-1h3.5a1 1 0 0 1 1 1c0 1.25.2 2.45.57 3.57a1 1 0 0 1-.25 1L6.6 10.8z"/></svg>',
 "check": '<svg class="ico" viewBox="0 0 24 24"><path d="M9 16.2 4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4z"/></svg>',
 "shield": '<svg class="ico" viewBox="0 0 24 24"><path d="M12 2 4 5v6c0 5.5 3.4 10.7 8 12 4.6-1.3 8-6.5 8-12V5l-8-3zm-1.2 14.4-3.5-3.5 1.4-1.4 2.1 2.1 4.9-4.9 1.4 1.4-6.3 6.3z"/></svg>',
 "snow": '<svg class="ico" viewBox="0 0 24 24"><path d="M11 2h2v4.3l2.1-1.3 1 1.7-3.1 1.9v2.7l2.4-1.4v-3.6l2 .1-.1 2.4 3.7-2.1 1 1.7-3.7 2.1 2.1 1.2-1 1.7-3.1-1.8-2.4 1.4 2.4 1.4 3.1-1.8 1 1.7-2.1 1.2 3.7 2.1-1 1.7-3.7-2.1.1 2.4-2 .1v-3.6l-2.4-1.4v2.7l3.1 1.9-1 1.7L13 17.7V22h-2v-4.3l-2.1 1.3-1-1.7 3.1-1.9v-2.7l-2.4 1.4v3.6l-2-.1.1-2.4-3.7 2.1-1-1.7 3.7-2.1-2.1-1.2 1-1.7 3.1 1.8L10.1 12 7.7 10.6 4.6 12.4l-1-1.7 2.1-1.2L2 7.4l1-1.7 3.7 2.1-.1-2.4 2-.1v3.6l2.4 1.4V7.6L7.9 5.7l1-1.7L11 5.3V2z"/></svg>',
 "flame": '<svg class="ico" viewBox="0 0 24 24"><path d="M13.5 2s.8 3.2-1.5 5.8C9.8 10.3 8 11.5 8 14.5a4 4 0 0 0 8 0c0-1.3-.6-2.3-1.3-3 .1 1.2-.6 2-1.4 2.2.9-2.8-.3-5.1-1.7-6.4 3.3-.7 5.9 2.3 5.9 6.2a7 7 0 1 1-14 0C3.5 8.5 9 7.5 9 3.5c1.8.4 3.3 1.5 4.5 3V2z"/></svg>',
 "swap": '<svg class="ico" viewBox="0 0 24 24"><path d="M7 7h11l-2.3-2.3L17 3.5 21.5 8 17 12.5l-1.3-1.2L18 9H7V7zm10 10H6l2.3 2.3L7 20.5 2.5 16 7 11.5l1.3 1.2L6 15h11v2z"/></svg>',
 "wall": '<svg class="ico" viewBox="0 0 24 24"><path d="M3 5h18a1 1 0 0 1 1 1v7a2 2 0 0 1-2 2H4a2 2 0 0 1-2-2V6a1 1 0 0 1 1-1zm1 2v6h16V7H4zm2 9h12v1.5H6V16zm2 3h8v1.5H8V19z"/></svg>',
 "building": '<svg class="ico" viewBox="0 0 24 24"><path d="M3 21V5a2 2 0 0 1 2-2h8a2 2 0 0 1 2 2v4h4a2 2 0 0 1 2 2v10h-6v-4h-4v4H3zm4-13h2V6H7v2zm4 0h2V6h-2v2zm-4 4h2v-2H7v2zm4 0h2v-2h-2v2zm-4 4h2v-2H7v2zm4 0h2v-2h-2v2zm6 0h2v-2h-2v2zm0-4h2v-2h-2v2z"/></svg>',
 "home": '<svg class="ico" viewBox="0 0 24 24"><path d="M12 3 2 12h3v8h5v-5h4v5h5v-8h3L12 3z"/></svg>',
 "pin": '<svg class="ico" viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-7 7c0 5.2 7 13 7 13s7-7.8 7-13a7 7 0 0 0-7-7zm0 9.5A2.5 2.5 0 1 1 12 6a2.5 2.5 0 0 1 0 5.5z"/></svg>',
 "chat": '<svg class="ico" viewBox="0 0 24 24"><path d="M4 3h16a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H8l-5 4V5a2 2 0 0 1 1-2zm3 5v2h10V8H7zm0 4v2h7v-2H7z"/></svg>',
 "cash": '<svg class="ico" viewBox="0 0 24 24"><path d="M2 6h20v12H2V6zm2 2v8h16V8H4zm8 1a3 3 0 1 1 0 6 3 3 0 0 1 0-6zM5 9h2v2H5V9zm12 4h2v2h-2v-2z"/></svg>',
 "cert": '<svg class="ico" viewBox="0 0 24 24"><path d="M4 3h16a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1h-5l-3 4-3-4H4a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1zm2 4v2h12V7H6zm0 4v2h8v-2H6z"/></svg>',
 "arrow": '<svg class="ico" viewBox="0 0 24 24"><path d="M5 11h11.2l-4.6-4.6L13 5l7 7-7 7-1.4-1.4 4.6-4.6H5z"/></svg>',
 "menu": '<svg class="ico" viewBox="0 0 24 24"><path d="M3 6h18v2H3zm0 5h18v2H3zm0 5h18v2H3z"/></svg>',
}

# ---------------------------------------------------------------- data
SERVICES = [
 dict(slug="ac-installation", icon="snow",
   title=("New A/C System Installation","Instalación de Sistema Nuevo de A/C"),
   blurb=("Complete new central air conditioning systems, 3 to 5 tons, sized right for your home.","Sistemas nuevos de aire acondicionado central, de 3 a 5 toneladas, del tamaño correcto para su casa."),
   h1=("New Air Conditioning System Installation","Instalación de Sistema Nuevo de Aire Acondicionado"),
   lead=("A new, properly sized central A/C system installed by local technicians, backed by a 10-year parts and 2-year labor warranty.","Un sistema nuevo de aire central, del tamaño correcto, instalado por técnicos locales y respaldado con 10 años de garantía en partes y 2 años en mano de obra."),
   img="images/ac-install.jpg",
   body=[
    ("What's included","Qué incluye",
     "Every new system installation includes the indoor unit with heating and the outdoor condensing unit, installed and connected by our team. We handle the removal of your old equipment, set the new system, charge and test it, and walk you through the thermostat before we leave.",
     "Cada instalación de sistema nuevo incluye la máquina de adentro con calefacción y la máquina de afuera, instaladas y conectadas por nuestro equipo. Retiramos su equipo viejo, colocamos el sistema nuevo, lo cargamos y lo probamos, y le explicamos el termostato antes de irnos."),
    ("The right size for your home","El tamaño correcto para su casa",
     "An undersized unit runs nonstop and never catches up in July. An oversized one short-cycles, leaves the air humid, and wears out early. We install 3, 3.5, 4 and 5 ton systems and match the size to your square footage, insulation and sun exposure so the system cools evenly and lasts.",
     "Una unidad muy chica trabaja sin parar y nunca alcanza en julio. Una muy grande se apaga y prende seguido, deja el aire húmedo y se desgasta antes. Instalamos sistemas de 3, 3.5, 4 y 5 toneladas y escogemos el tamaño según sus pies cuadrados, aislamiento y sol para que enfríe parejo y dure."),
    ("Warranty you can hold in your hand","Una garantía que puede tener en la mano",
     "When the job is done you receive your warranty certificate and your invoice. Parts are covered for 10 years and our labor for 2 years. Keep the certificate with your home records; it is what you show if anything ever needs service.",
     "Al terminar el trabajo recibe su certificado de garantía y su factura. Las partes están cubiertas por 10 años y nuestra mano de obra por 2 años. Guarde el certificado con los papeles de su casa; es lo que muestra si algo necesita servicio."),
   ],
   ticks=[("Indoor unit with heating + outdoor unit","Máquina de adentro con calefacción + máquina de afuera"),("3, 3.5, 4 and 5 ton systems","Sistemas de 3, 3.5, 4 y 5 toneladas"),("Old equipment removed","Retiramos el equipo viejo"),("10-year parts / 2-year labor warranty","Garantía 10 años partes / 2 años mano de obra"),("Warranty certificate and invoice delivered","Se entrega certificado de garantía y factura")],
   faq=[("How long does a new system installation take?","¿Cuánto tarda la instalación de un sistema nuevo?","Most residential replacements are completed in one day. We confirm the schedule when we give you the quote.","La mayoría de los reemplazos residenciales se terminan en un día. Confirmamos la fecha cuando le damos la cotización."),
        ("Do you give a price before starting?","¿Dan el precio antes de empezar?","Yes. You get a clear quote up front, and we offer a cash price. Ask us when you call.","Sí. Le damos una cotización clara antes de empezar, y ofrecemos precio de contado. Pregúntenos cuando llame."),
        ("Which areas do you install in?","¿En qué áreas instalan?","The whole Rio Grande Valley, from Mission to Brownsville. Our advertised pricing applies to the Valley only.","Todo el Valle del Río Grande, de Mission a Brownsville. Nuestros precios anunciados son solo para el Valle.")]),
 dict(slug="ac-replacement", icon="swap", img2="images/replacement.jpg",
   title=("A/C System Replacement","Reemplazo de Sistema de A/C"),
   blurb=("Replace a worn-out system with a new indoor unit with heating and a new outdoor unit.","Reemplace un sistema gastado con máquina de adentro con calefacción y máquina de afuera nuevas."),
   h1=("Air Conditioning System Replacement","Reemplazo de Sistema de Aire Acondicionado"),
   lead=("Stop paying to repair a tired system. We replace both the indoor and outdoor units so you get full efficiency and a full warranty.","Deje de pagar reparaciones a un sistema cansado. Reemplazamos la máquina de adentro y la de afuera para que tenga eficiencia completa y garantía completa."),
   img="images/replacement.jpg",
   body=[
    ("When replacement beats repair","Cuándo conviene reemplazar en vez de reparar",
     "If your system is over 10 to 12 years old, needs refrigerant every summer, or the repair quote is a big share of a new system's cost, replacement is usually the better money. A new system cools faster, runs quieter and uses less electricity every month.",
     "Si su sistema tiene más de 10 a 12 años, necesita gas cada verano, o la reparación cuesta una buena parte de un sistema nuevo, reemplazar suele ser mejor negocio. Un sistema nuevo enfría más rápido, hace menos ruido y gasta menos luz cada mes."),
    ("We replace the complete system","Reemplazamos el sistema completo",
     "Mixing a new outdoor unit with an old indoor coil cuts efficiency and can void manufacturer coverage. Our replacement includes the indoor unit with heating and the outdoor unit, matched as a set, so the system performs the way it was designed to.",
     "Combinar una máquina de afuera nueva con un serpentín viejo adentro baja la eficiencia y puede anular la cobertura del fabricante. Nuestro reemplazo incluye la máquina de adentro con calefacción y la de afuera, como juego, para que el sistema rinda como fue diseñado."),
    ("Clean job, clear paperwork","Trabajo limpio, papeles claros",
     "We remove and haul off the old equipment, protect your floors, and leave the area clean. You receive your warranty certificate and invoice the same day.",
     "Retiramos y nos llevamos el equipo viejo, protegemos sus pisos y dejamos el área limpia. Recibe su certificado de garantía y su factura el mismo día."),
   ],
   ticks=[("Indoor + outdoor unit replaced together","Máquina de adentro y de afuera reemplazadas juntas"),("Old system hauled away","Nos llevamos el sistema viejo"),("Lower monthly electric use","Menos consumo de luz al mes"),("10-year parts / 2-year labor warranty","Garantía 10 años partes / 2 años mano de obra"),("Cash price available","Precio de contado disponible")],
   faq=[("Can you replace just the outside unit?","¿Pueden cambiar solo la máquina de afuera?","We recommend replacing both so the system is matched and fully covered. Call us and we will look at your setup and give you honest options.","Recomendamos cambiar las dos para que el sistema esté a juego y con cobertura completa. Llámenos, revisamos su equipo y le damos opciones honestas."),
        ("Will I be without A/C for long?","¿Voy a estar sin aire mucho tiempo?","Most replacements are done in one day. We schedule so your home is cooling again the same evening.","La mayoría de los reemplazos se hacen en un día. Programamos para que su casa esté enfriando otra vez esa misma noche.")]),
 dict(slug="mini-splits", icon="wall", img2="images/mini-unit.jpg",
   title=("Mini Split Installation","Instalación de Mini Splits"),
   blurb=("Ductless mini splits for rooms, additions, garages, shops and offices.","Mini splits sin ductos para cuartos, ampliaciones, garajes, talleres y oficinas."),
   h1=("Mini Split Air Conditioner Installation","Instalación de Mini Splits"),
   lead=("Cool one room, a garage, a casita or a whole small building without ductwork. We install and warranty ductless mini split systems across the Valley.","Enfríe un cuarto, un garaje, una casita o un edificio chico sin ductos. Instalamos y garantizamos mini splits en todo el Valle."),
   img="images/mini-room.jpg",
   body=[
    ("Where mini splits make sense","Dónde conviene un mini split",
     "Rooms that never get cool, garage conversions, home offices, workshops, rental units and small businesses. A mini split gives that space its own thermostat without tearing into walls or ceilings for ducts.",
     "Cuartos que nunca enfrían, garajes convertidos, oficinas en casa, talleres, rentas y negocios chicos. Un mini split le da a ese espacio su propio termostato sin abrir paredes o techos para ductos."),
    ("Quiet, efficient, and heats too","Silencioso, eficiente, y también calienta",
     "Modern mini splits are some of the most efficient systems available and run almost silently. Most models are heat pumps, so the same unit keeps the room warm on cold Valley mornings.",
     "Los mini splits modernos son de los sistemas más eficientes que hay y casi no hacen ruido. La mayoría son bomba de calor, así que la misma unidad calienta el cuarto en las mañanas frías del Valle."),
    ("Professional installation","Instalación profesional",
     "We mount the indoor head, set the outdoor unit on a pad or bracket, run the line set cleanly, pull a proper vacuum and charge the system to spec. Same warranty as our central systems: 10 years parts, 2 years labor.",
     "Montamos la unidad de adentro, colocamos la de afuera en base o soporte, pasamos la tubería limpia, hacemos vacío correcto y cargamos el sistema según especificación. Misma garantía que nuestros sistemas centrales: 10 años partes, 2 años mano de obra."),
   ],
   ticks=[("Single-zone and multi-zone systems","Sistemas de una zona y multi-zona"),("No ductwork needed","No necesita ductos"),("Cooling and heating in one unit","Enfría y calienta en una sola unidad"),("Clean line set and condensate routing","Tubería y drenaje limpios"),("10-year parts / 2-year labor warranty","Garantía 10 años partes / 2 años mano de obra")],
   faq=[("How many rooms can one outdoor unit handle?","¿Cuántos cuartos puede manejar una unidad de afuera?","Multi-zone systems run two to four indoor heads from one outdoor unit. We will size it for your rooms.","Los sistemas multi-zona manejan de dos a cuatro unidades de adentro con una de afuera. Lo calculamos para sus cuartos."),
        ("Do mini splits work for businesses?","¿Los mini splits sirven para negocios?","Yes. They are a popular choice for small shops, offices and server rooms. See our commercial page or call us.","Sí. Son muy usados en tiendas chicas, oficinas y cuartos de servidores. Vea nuestra página comercial o llámenos.")]),
 dict(slug="heating", icon="flame",
   title=("Heating","Calefacción"),
   blurb=("Heating installed with every new system so your home stays warm on cold Valley nights.","Calefacción instalada con cada sistema nuevo para que su casa esté caliente en las noches frías del Valle."),
   h1=("Heating Installation & Service","Instalación y Servicio de Calefacción"),
   lead=("Every indoor unit we install comes with heating. When a norther blows through, your home is ready.","Cada máquina de adentro que instalamos viene con calefacción. Cuando llega un norte, su casa está lista."),
   img="images/heating.jpg",
   body=[
    ("Heating built into your system","Calefacción integrada en su sistema",
     "Our new system installations and replacements include an indoor unit with heating. One system, one thermostat, cooling in summer and heat in winter, all under the same warranty.",
     "Nuestras instalaciones y reemplazos incluyen máquina de adentro con calefacción. Un sistema, un termostato, aire en verano y calor en invierno, todo con la misma garantía."),
    ("Heat pumps and mini splits","Bombas de calor y mini splits",
     "For the Valley's mild winters a heat pump or mini split is often the most economical way to heat. It moves heat instead of making it, so it costs less to run than resistance heat on most days.",
     "Para los inviernos suaves del Valle, una bomba de calor o un mini split suele ser la forma más económica de calentar. Mueve el calor en vez de producirlo, así que cuesta menos operar que la calefacción de resistencia la mayoría de los días."),
    ("Get it checked before the first cold front","Revíselo antes del primer frente frío",
     "If your heat has not been on since last winter, call us before you need it. A quick check is cheaper than an emergency call on the coldest night of the year.",
     "Si su calefacción no se ha prendido desde el invierno pasado, llámenos antes de que la necesite. Una revisión rápida es más barata que una emergencia en la noche más fría del año."),
   ],
   ticks=[("Indoor unit with heating on every new system","Máquina de adentro con calefacción en cada sistema nuevo"),("Heat pump and mini split heating","Calefacción por bomba de calor y mini split"),("Residential and commercial","Residencial y comercial"),("Same 10-year / 2-year warranty","Misma garantía 10 años / 2 años")],
   faq=[("Does the warranty cover the heating part too?","¿La garantía cubre también la calefacción?","Yes. The indoor unit with heating is part of the system and carries the same 10-year parts and 2-year labor warranty.","Sí. La máquina de adentro con calefacción es parte del sistema y lleva la misma garantía de 10 años en partes y 2 en mano de obra.")]),
 dict(slug="commercial", icon="building",
   title=("Commercial HVAC","HVAC Comercial"),
   blurb=("Air conditioning and heating for shops, restaurants, offices and warehouses.","Aire acondicionado y calefacción para tiendas, restaurantes, oficinas y bodegas."),
   h1=("Commercial Air Conditioning & Heating","Aire Acondicionado y Calefacción Comercial"),
   lead=("Keep customers comfortable and employees productive. We install and service systems for businesses across the Rio Grande Valley.","Mantenga a sus clientes cómodos y a sus empleados productivos. Instalamos y damos servicio a sistemas para negocios en todo el Valle del Río Grande."),
   img="images/commercial.jpg",
   body=[
    ("Businesses we serve","Negocios que atendemos",
     "Retail stores, restaurants and kitchens, offices, clinics, churches, warehouses and shops. We size equipment for the real load of your space, including people, lighting and kitchen heat.",
     "Tiendas, restaurantes y cocinas, oficinas, clínicas, iglesias, bodegas y talleres. Calculamos el equipo para la carga real de su local, incluyendo gente, iluminación y calor de cocina."),
    ("Minimal disruption","Mínima interrupción",
     "We schedule around your business hours when possible and work clean so you can keep the doors open. Tell us your constraints when you call and we will plan the job around them.",
     "Programamos fuera de su horario cuando se puede y trabajamos limpio para que pueda seguir abierto. Díganos sus limitaciones cuando llame y planeamos el trabajo alrededor de ellas."),
    ("Mini splits for small commercial spaces","Mini splits para locales chicos",
     "For small shops, offices and server rooms, ductless mini splits are fast to install and inexpensive to run. We install single and multi-zone systems.",
     "Para tiendas chicas, oficinas y cuartos de servidores, los mini splits son rápidos de instalar y baratos de operar. Instalamos sistemas de una y varias zonas."),
   ],
   ticks=[("Split systems and mini splits for business","Sistemas split y mini splits para negocios"),("Installation and replacement","Instalación y reemplazo"),("Scheduling around your hours","Programación según su horario"),("Warranty certificate and invoice for your records","Certificado de garantía y factura para sus registros")],
   faq=[("Do you work with property managers and landlords?","¿Trabajan con administradores de propiedades y arrendadores?","Yes. We can handle multiple units and keep the paperwork organized per property.","Sí. Podemos atender varias unidades y mantener los papeles organizados por propiedad.")]),
]
CITIES = ["Mission","McAllen","Edinburg","Pharr","San Juan","Alamo","Donna","Weslaco","Mercedes","La Feria","Harlingen","San Benito","Los Fresnos","Brownsville","Rio Grande City","Palmview","Alton","Hidalgo","Progreso","Raymondville","Port Isabel"]
SERVICE_OPTIONS = [("New A/C system","Sistema nuevo de A/C"),("System replacement","Reemplazo de sistema"),("Mini split","Mini split"),("Heating","Calefacción"),("Commercial","Comercial"),("Other","Otro")]

# ---------------------------------------------------------------- components
def lead_form(compact=False, title=("Get Your Free Quote","Pida su Cotización Gratis"), sub=("Tell us what you need. We call you back fast.","Díganos qué necesita. Le llamamos rápido.")):
    opts = "".join(f'<option>{t(en,es)}</option>' for en,es in SERVICE_OPTIONS)
    return f'''<div class="form-card">
  <h3>{t(*title)}</h3><p class="sub">{t(*sub)}</p>
  <form data-lead action="https://formsubmit.co/{FORM_EMAIL}" method="POST">
    <input type="hidden" name="_subject" value="New quote request - jrrefrigerationac.com">
    <input type="hidden" name="_captcha" value="false"><input type="hidden" name="_template" value="table">
    <input type="hidden" name="_next" value="{DOMAIN}/thank-you/">
    <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off">
    <div class="row"><div><label>{t("Name","Nombre")} *</label><input type="text" name="name" required autocomplete="name"></div>
    <div><label>{t("Phone","Teléfono")} *</label><input type="tel" name="phone" required autocomplete="tel"></div></div>
    <div class="row"><div><label>Email</label><input type="email" name="email" autocomplete="email"></div>
    <div><label>{t("City","Ciudad")}</label><input type="text" name="city" autocomplete="address-level2"></div></div>
    <label>{t("What do you need?","¿Qué necesita?")}</label><select name="service">{opts}</select>
    <label>{t("Details","Detalles")}</label><textarea name="message" rows="{2 if compact else 3}" data-es-ph="Tamaño de la casa, edad del sistema, qué está pasando…" placeholder="Home size, age of system, what's going on…"></textarea>
    <button type="submit" class="btn btn-red btn-lg">{t("Request My Free Quote","Pedir Cotización Gratis")}</button>
    <p class="fine">{t("No spam. We only use this to contact you about your request.","Sin spam. Solo usamos esto para contactarle sobre su solicitud.")}</p>
  </form></div>'''

def header(active=""):
    links = [("/", "Home","Inicio"), ("/services/ac-installation/","New Systems","Sistemas Nuevos"), ("/services/mini-splits/","Mini Splits","Mini Splits"), ("/services/heating/","Heating","Calefacción"), ("/services/commercial/","Commercial","Comercial"), ("/service-area/","Service Area","Área de Servicio"), ("/about/","About","Nosotros"), ("/contact/","Contact","Contacto")]
    nav = "".join(f'<a href="{h}"{" class=\"active\"" if h==active else ""}>{t(en,es)}</a>' for h,en,es in links)
    return f'''<div class="topbar"><div class="wrap"><div class="left"><span>{t("Serving the Rio Grande Valley, Mission to Brownsville","Sirviendo al Valle del Río Grande, de Mission a Brownsville")}</span><span class="sec">&bull;</span><span class="sec">{t("Residential &amp; Commercial","Residencial y Comercial")}</span><span class="sec">&bull;</span><span class="sec">Se habla español</span></div><a href="tel:{TEL}">{t("Call","Llame")} {PHONE}</a></div></div>
<header class="site"><div class="wrap">
  <a class="logo" href="/" aria-label="JR Refrigeration home"><span class="mark">JR</span><span class="name">JR REFRIGERATION<small>AIR CONDITIONING &amp; HEATING</small></span></a>
  <nav class="main" aria-label="Main">{nav}</nav>
  <div class="hdr-cta"><button class="lang" type="button" aria-label="Cambiar idioma">Español</button><a class="hdr-phone" href="tel:{TEL}"><small>{t("Call or text","Llame o mande texto")}</small><b>{PHONE}</b></a><a class="btn btn-red" href="/contact/">{t("Free Quote","Cotización Gratis")}</a><button class="burger" type="button" aria-label="Menu">{I["menu"]}</button></div>
</div></header>'''

def footer():
    svc = "".join(f'<li><a href="/services/{s["slug"]}/">{t(*s["title"])}</a></li>' for s in SERVICES)
    return f'''<footer class="site"><div class="wrap">
<div class="cols">
 <div><a class="logo" href="/" style="color:#fff"><span class="mark">JR</span><span class="name" style="color:#fff">JR REFRIGERATION<small>AIR CONDITIONING &amp; HEATING</small></span></a>
  <p style="margin-top:14px">{t("Residential and commercial air conditioning and heating. New systems, replacements and mini splits across the Rio Grande Valley, Texas.","Aire acondicionado y calefacción residencial y comercial. Sistemas nuevos, reemplazos y mini splits en todo el Valle del Río Grande, Texas.")}</p>
  <a class="phone" href="tel:{TEL}">{PHONE}</a><span>Se habla español</span></div>
 <div><h4>{t("Services","Servicios")}</h4><ul>{svc}</ul></div>
 <div><h4>{t("Company","Empresa")}</h4><ul><li><a href="/about/">{t("About JR Refrigeration","Sobre JR Refrigeration")}</a></li><li><a href="/service-area/">{t("Service Area","Área de Servicio")}</a></li><li><a href="/contact/">{t("Contact / Free Quote","Contacto / Cotización")}</a></li><li><a href="/privacy/">{t("Privacy","Privacidad")}</a></li></ul></div>
 <div><h4>{t("Warranty","Garantía")}</h4><p><b style="color:#fff">{t("10 years parts &bull; 2 years labor","10 años partes &bull; 2 años mano de obra")}</b><br>{t("Warranty certificate and invoice delivered with every installation.","Certificado de garantía y factura entregados con cada instalación.")}</p><p style="font-size:.82rem">{t("Advertised pricing applies to the Rio Grande Valley area only.","Los precios anunciados son solo para el área del Valle del Río Grande.")}</p></div>
</div>
<div class="bottom"><span>&copy; {YEAR} JR Refrigeration &bull; Air Conditioning &amp; Heating Services &bull; Rio Grande Valley, TX</span><span>Photos: U.S. Air Force (public domain); "Mini-Split AC" by HelpAtMyHome, CC BY 2.0; Unsplash</span></div>
</div></footer>
<div class="mbar"><a class="btn btn-blue" href="tel:{TEL}">{I["phone"]} {t("Call Now","Llamar")}</a><a class="btn btn-red" href="/contact/">{t("Free Quote","Cotización")}</a></div>
<script src="/js/main.js" defer></script>'''

def page(title, desc, body, path="/", active="/", schema=True, og_img="images/hero.jpg"):
    ld = ""
    if schema:
        ld = f'''<script type="application/ld+json">{{"@context":"https://schema.org","@type":"HVACBusiness","name":"JR Refrigeration","alternateName":"JR Refrigeration Air Conditioning & Heating Services","url":"{DOMAIN}/","telephone":"{TEL}","image":"{DOMAIN}/{og_img}","priceRange":"$$","areaServed":[{",".join(f'{{"@type":"City","name":"{c}, TX"}}' for c in CITIES[:15])}],"address":{{"@type":"PostalAddress","addressRegion":"TX","addressCountry":"US"}},"knowsLanguage":["en","es"],"makesOffer":[{",".join(f'{{"@type":"Offer","itemOffered":{{"@type":"Service","name":"{s["title"][0]}","url":"{DOMAIN}/services/{s["slug"]}/"}}}}' for s in SERVICES)}]}}</script>'''
    return f'''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(title)}</title><meta name="description" content="{html.escape(desc, quote=True)}">
<link rel="canonical" href="{DOMAIN}{path}">
<meta property="og:title" content="{html.escape(title, quote=True)}"><meta property="og:description" content="{html.escape(desc, quote=True)}"><meta property="og:image" content="{DOMAIN}/{og_img}"><meta property="og:url" content="{DOMAIN}{path}"><meta property="og:type" content="website">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Montserrat:wght@700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/style.css">{ld}
</head><body>
{header(active)}
<main>{body}</main>
{footer()}
</body></html>'''

def faq_block(items):
    return '<div class="faq">' + "".join(f'<details><summary>{t(q,qs)}</summary><p>{t(a,as_)}</p></details>' for q,qs,a,as_ in items) + '</div>'

def cta_final():
    return f'''<section class="cta-final"><div class="wrap">
  <div><span class="eyebrow" style="color:var(--gold)">{t("Ready when you are","Listos cuando usted diga")}</span><h2>{t("Get a new system installed by people who answer the phone.","Instale un sistema nuevo con gente que sí contesta el teléfono.")}</h2>
  <p>{t("Call or text us, or send the form and we will call you back. Ask about our cash price.","Llame o mande texto, o envíe el formulario y le llamamos. Pregunte por nuestro precio de contado.")}</p>
  <a class="btn btn-white btn-lg" href="tel:{TEL}">{I["phone"]} {PHONE}</a></div>
  {lead_form(compact=True)}
</div></section>'''

# ---------------------------------------------------------------- pages
def home():
    cards = "".join(f'''<div class="card"><div class="icon">{I[s["icon"]]}</div><h3>{t(*s["title"])}</h3><p>{t(*s["blurb"])}</p><span class="more">{t("Learn more","Ver más")} {I["arrow"]}</span><a class="cover" href="/services/{s["slug"]}/" aria-label="{s["title"][0]}"></a></div>''' for s in SERVICES)
    cards += f'''<div class="card"><div class="icon">{I["pin"]}</div><h3>{t("Service Area","Área de Servicio")}</h3><p>{t("Mission, McAllen, Edinburg, Pharr, Weslaco, Harlingen, Brownsville and every town in between.","Mission, McAllen, Edinburg, Pharr, Weslaco, Harlingen, Brownsville y todos los pueblos entre ellos.")}</p><span class="more">{t("See all cities","Ver ciudades")} {I["arrow"]}</span><a class="cover" href="/service-area/" aria-label="Service area"></a></div>'''
    cities = "".join(f'<li>{I["pin"]}{c}</li>' for c in CITIES[:15])
    faqs = [("Do you charge for a quote?","¿Cobran por la cotización?","No. Quotes are free. Call, text, or send the form and we will set a time.","No. Las cotizaciones son gratis. Llame, mande texto o envíe el formulario y agendamos."),
            ("What does the warranty cover?","¿Qué cubre la garantía?","10 years on parts and 2 years on our labor. You receive the warranty certificate and your invoice when the installation is complete.","10 años en partes y 2 años en nuestra mano de obra. Recibe el certificado de garantía y su factura al terminar la instalación."),
            ("Do you install mini splits?","¿Instalan mini splits?","Yes, single-zone and multi-zone, for homes and businesses.","Sí, de una zona y multi-zona, para casas y negocios."),
            ("Do you speak Spanish?","¿Hablan español?","Yes. Call us in English or Spanish.","Sí. Llámenos en inglés o en español."),
            ("Which sizes do you install?","¿Qué tamaños instalan?","3, 3.5, 4 and 5 ton central systems, plus mini splits for single rooms and small buildings.","Sistemas centrales de 3, 3.5, 4 y 5 toneladas, además de mini splits para cuartos y edificios chicos.")]
    body = f'''
<section class="hero"><div class="bg" style="background-image:url(/images/hero.jpg)"></div><div class="shade"></div>
<div class="wrap">
 <div>
  <span class="eyebrow" style="color:var(--gold)">{t("Air Conditioning &amp; Heating &bull; Rio Grande Valley","Aire Acondicionado y Calefacción &bull; Valle del Río Grande")}</span>
  <h1>{t("Get a <em>new A/C system</em> installed right, with a warranty you can hold.","Instale un <em>sistema nuevo de A/C</em> bien hecho, con una garantía que puede tener en la mano.")}</h1>
  <p class="lead">{t("New systems, replacements and mini splits for homes and businesses from Mission to Brownsville. Local, bilingual, and straightforward about price.","Sistemas nuevos, reemplazos y mini splits para casas y negocios de Mission a Brownsville. Locales, bilingües y claros con el precio.")}</p>
  <ul class="checks">
   <li>{I["check"]}<span>{t("<b>10-year parts</b> and <b>2-year labor</b> warranty on every installation","Garantía de <b>10 años en partes</b> y <b>2 años en mano de obra</b> en cada instalación")}</span></li>
   <li>{I["check"]}<span>{t("Indoor unit with heating + outdoor unit, installed as a complete system","Máquina de adentro con calefacción + máquina de afuera, instaladas como sistema completo")}</span></li>
   <li>{I["check"]}<span>{t("Ask about our <b>cash price</b>","Pregunte por nuestro <b>precio de contado</b>")}</span></li>
  </ul>
  <div class="actions"><a class="btn btn-red btn-lg" href="tel:{TEL}">{I["phone"]} {t("Call","Llame")} {PHONE}</a><a class="btn btn-ghost btn-lg" href="/services/ac-installation/">{t("See new systems","Ver sistemas nuevos")}</a></div>
  <p class="mini">{t("Residential &amp; Commercial &bull; Se habla español","Residencial y Comercial &bull; We speak English")}</p>
 </div>
 {lead_form()}
</div></section>
<div class="trust"><div class="wrap">
 <div class="item">{I["shield"]}<div><b>{t("10 Yr Parts / 2 Yr Labor","10 Años Partes / 2 Mano de Obra")}</b><span>{t("Certificate + invoice delivered","Certificado + factura entregados")}</span></div></div>
 <div class="item">{I["cash"]}<div><b>{t("Cash Price Available","Precio de Contado")}</b><span>{t("Clear quote before we start","Cotización clara antes de empezar")}</span></div></div>
 <div class="item">{I["pin"]}<div><b>{t("Valley Local","Locales del Valle")}</b><span>{t("Mission to Brownsville, TX","De Mission a Brownsville, TX")}</span></div></div>
 <div class="item">{I["chat"]}<div><b>English &amp; Español</b><span>{t("Residential and commercial","Residencial y comercial")}</span></div></div>
</div></div>
<section><div class="wrap">
 <div class="sec-head center"><span class="eyebrow">{t("What we do","Lo que hacemos")}</span><h2>{t("Cooling and heating, done as a complete system","Aire y calefacción, hechos como un sistema completo")}</h2><p class="lead">{t("We install the indoor unit with heating and the outdoor unit together, sized for your space, so it cools evenly and lasts.","Instalamos la máquina de adentro con calefacción y la de afuera juntas, del tamaño correcto para su espacio, para que enfríe parejo y dure.")}</p></div>
 <div class="grid3">{cards}</div>
</div></section>
<section class="alt"><div class="wrap grid2">
 <div class="photo"><img src="/images/ac-install.jpg" alt="Technician installing a new outdoor air conditioning unit" loading="lazy" width="1000" height="666"></div>
 <div><span class="eyebrow">{t("Why JR Refrigeration","Por qué JR Refrigeration")}</span><h2>{t("Straight answers, clean work, real warranty","Respuestas directas, trabajo limpio, garantía real")}</h2>
  <p class="lead">{t("You should know what you are paying for and what happens if something goes wrong. That is how we work.","Usted debe saber qué está pagando y qué pasa si algo falla. Así trabajamos.")}</p>
  <ul class="ticks">
   <li>{I["check"]}<span><b>{t("Complete systems","Sistemas completos")}</b> &mdash; {t("indoor unit with heating plus outdoor unit, matched and installed together.","máquina de adentro con calefacción más máquina de afuera, a juego e instaladas juntas.")}</span></li>
   <li>{I["check"]}<span><b>{t("Right size, every time","El tamaño correcto, siempre")}</b> &mdash; {t("3 to 5 ton systems matched to your home, not a guess.","sistemas de 3 a 5 toneladas según su casa, no al tanteo.")}</span></li>
   <li>{I["check"]}<span><b>{t("Paperwork in your hand","Papeles en su mano")}</b> &mdash; {t("warranty certificate and invoice delivered when we finish.","certificado de garantía y factura entregados al terminar.")}</span></li>
   <li>{I["check"]}<span><b>{t("Bilingual service","Servicio bilingüe")}</b> &mdash; {t("call, text or write to us in English or Spanish.","llame, mande texto o escriba en inglés o español.")}</span></li>
  </ul>
  <a class="btn btn-blue" href="/about/">{t("More about us","Más sobre nosotros")} {I["arrow"]}</a></div>
</div></section>
<section><div class="wrap">
 <div class="sec-head center"><span class="eyebrow">{t("How it works","Cómo funciona")}</span><h2>{t("From first call to cold air in three steps","De la primera llamada al aire frío en tres pasos")}</h2></div>
 <div class="steps">
  <div class="step"><div class="n">1</div><h3>{t("Call or send the form","Llame o envíe el formulario")}</h3><p>{t("Tell us about your home or business and what is going on. We answer in English or Spanish.","Cuéntenos de su casa o negocio y qué está pasando. Contestamos en inglés o español.")}</p></div>
  <div class="step"><div class="n">2</div><h3>{t("Free quote, clear price","Cotización gratis, precio claro")}</h3><p>{t("We size the system for your space and give you a straight price, including our cash price.","Calculamos el sistema para su espacio y le damos un precio directo, incluyendo precio de contado.")}</p></div>
  <div class="step"><div class="n">3</div><h3>{t("Installed, tested, warrantied","Instalado, probado, garantizado")}</h3><p>{t("Usually done in a day. You get your warranty certificate and invoice before we leave.","Normalmente en un día. Recibe su certificado de garantía y factura antes de que nos vayamos.")}</p></div>
 </div>
</div></section>
<section class="alt"><div class="wrap grid2">
 <div><span class="eyebrow">{t("Mini splits","Mini splits")}</span><h2>{t("One room too hot? A mini split fixes it without ducts.","¿Un cuarto muy caliente? Un mini split lo arregla sin ductos.")}</h2>
  <p class="lead">{t("Garage conversions, home offices, casitas, shops and rentals. Quiet, efficient, and it heats in winter too.","Garajes convertidos, oficinas en casa, casitas, talleres y rentas. Silencioso, eficiente, y también calienta en invierno.")}</p>
  <a class="btn btn-red" href="/services/mini-splits/">{t("Mini split installation","Instalación de mini splits")} {I["arrow"]}</a></div>
 <div class="photo"><img src="/images/mini-room.jpg" alt="Living room with a ductless mini split wall unit" loading="lazy" width="1000" height="666"></div>
</div></section>
<div class="band"><div class="wrap">
 <h2>{t("Our Warranty","Nuestra Garantía")}</h2>
 <div class="big">{t("10 YEARS parts &bull; 2 YEARS labor","10 AÑOS partes &bull; 2 AÑOS mano de obra")}</div>
 <p>{t("Every installation comes with a written warranty certificate and your invoice. Keep them with your home records.","Cada instalación viene con un certificado de garantía por escrito y su factura. Guárdelos con los papeles de su casa.")}</p>
 <a class="btn btn-white" href="/contact/">{t("Get a quote","Pedir cotización")}</a>
</div></div>
<section><div class="wrap grid2">
 <div><span class="eyebrow">{t("Service area","Área de servicio")}</span><h2>{t("Serving the whole Rio Grande Valley","Sirviendo a todo el Valle del Río Grande")}</h2>
  <p class="lead">{t("From Mission to Brownsville and everywhere in between.","De Mission a Brownsville y todo lo que está en medio.")}</p>
  <ul class="cities">{cities}</ul>
  <p style="margin-top:16px"><a href="/service-area/">{t("See the full service area","Ver toda el área de servicio")} &rarr;</a></p></div>
 <div class="map"><iframe title="Rio Grande Valley service area map" src="https://www.google.com/maps?q=Rio+Grande+Valley,+Texas&z=9&output=embed" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe></div>
</div></section>
<section class="alt"><div class="wrap">
 <div class="sec-head center"><span class="eyebrow">FAQ</span><h2>{t("Questions people ask us","Preguntas que nos hacen")}</h2></div>
 {faq_block(faqs)}
</div></section>
{cta_final()}'''
    return page("JR Refrigeration | Air Conditioning & Heating | Rio Grande Valley, TX",
                "New A/C systems, replacements, mini splits and heating for homes and businesses from Mission to Brownsville, TX. 10-year parts / 2-year labor warranty. Se habla español. Call (210) 946-0246.",
                body, "/", "/")

def service_page(s):
    ticks = "".join(f'<li>{I["check"]}<span>{t(en,es)}</span></li>' for en,es in s["ticks"])
    body_html = "".join(f'<h2>{t(h,hs)}</h2><p>{t(p,ps)}</p>' for h,hs,p,ps in s["body"])
    others = "".join(f'<li><a href="/services/{o["slug"]}/">{t(*o["title"])}</a></li>' for o in SERVICES if o is not s)
    body = f'''
<div class="phero"><div class="bg" style="background-image:url(/{s["img"]})"></div><div class="shade"></div><div class="wrap">
 <div class="crumbs"><a href="/">{t("Home","Inicio")}</a> &rsaquo; {t("Services","Servicios")} &rsaquo; {t(*s["title"])}</div>
 <h1>{t(*s["h1"])}</h1><p class="lead">{t(*s["lead"])}</p>
 <div class="actions" style="display:flex;gap:12px;flex-wrap:wrap;margin-top:18px"><a class="btn btn-red btn-lg" href="tel:{TEL}">{I["phone"]} {PHONE}</a><a class="btn btn-ghost btn-lg" href="#quote">{t("Request a quote","Pedir cotización")}</a></div>
</div></div>
<section><div class="wrap content">
 <div class="main">
  <div class="photo" style="margin-bottom:28px"><img src="/{s.get("img2",s["img"])}" alt="{s["h1"][0]}" width="1000" height="666"></div>
  {body_html}
  <div class="callout"><b>{t("Included with this service","Incluido con este servicio")}</b><ul class="ticks" style="margin-bottom:0">{ticks}</ul></div>
  <h2>{t("Common questions","Preguntas comunes")}</h2>{faq_block(s["faq"])}
  <h2>{t("Other services","Otros servicios")}</h2><ul>{others}</ul>
 </div>
 <aside class="side" id="quote">{lead_form(compact=True)}
  <div class="card" style="margin-top:18px"><h3>{t("Prefer to talk?","¿Prefiere hablar?")}</h3><p>{t("Call or text us. English or Spanish.","Llame o mande texto. Inglés o español.")}</p><a class="btn btn-blue" href="tel:{TEL}">{I["phone"]} {PHONE}</a></div>
 </aside>
</div></section>
<div class="band blue"><div class="wrap"><h2>{t("10 years parts, 2 years labor, on every installation.","10 años partes, 2 años mano de obra, en cada instalación.")}</h2><p>{t("Warranty certificate and invoice delivered when the job is done.","Certificado de garantía y factura entregados al terminar el trabajo.")}</p><a class="btn btn-white" href="/contact/">{t("Get a free quote","Pedir cotización gratis")}</a></div></div>'''
    return page(f'{s["h1"][0]} | JR Refrigeration, Rio Grande Valley TX', s["lead"][0], body, f'/services/{s["slug"]}/', f'/services/{s["slug"]}/', og_img=s["img"])

def area_page():
    cities = "".join(f'<li>{I["pin"]}{c}</li>' for c in CITIES)
    body = f'''
<div class="phero"><div class="bg" style="background-image:url(/images/valley.jpg)"></div><div class="shade"></div><div class="wrap">
 <div class="crumbs"><a href="/">{t("Home","Inicio")}</a> &rsaquo; {t("Service Area","Área de Servicio")}</div>
 <h1>{t("Serving the Rio Grande Valley, Mission to Brownsville","Sirviendo al Valle del Río Grande, de Mission a Brownsville")}</h1>
 <p class="lead">{t("Hidalgo, Cameron, Willacy and Starr counties. If you are in the Valley, we come to you.","Condados de Hidalgo, Cameron, Willacy y Starr. Si está en el Valle, vamos a usted.")}</p></div></div>
<section><div class="wrap grid2">
 <div><h2>{t("Cities we serve","Ciudades que atendemos")}</h2><ul class="cities">{cities}</ul>
 <p style="margin-top:18px;color:var(--muted)">{t("Don't see your town? Call us. If it is in the Valley, we are there.","¿No ve su pueblo? Llámenos. Si está en el Valle, allá estamos.")}</p>
 <p style="font-size:.9rem;color:var(--muted)"><i>{t("Advertised pricing applies to the Rio Grande Valley area only.","Los precios anunciados son solo para el área del Valle del Río Grande.")}</i></p></div>
 <div class="map"><iframe title="Rio Grande Valley service area map" src="https://www.google.com/maps?q=Rio+Grande+Valley,+Texas&z=9&output=embed" loading="lazy"></iframe></div>
</div></section>
{cta_final()}'''
    return page("Service Area | JR Refrigeration | Mission to Brownsville, TX", "JR Refrigeration installs A/C systems, mini splits and heating across the Rio Grande Valley: Mission, McAllen, Edinburg, Pharr, Weslaco, Harlingen, Brownsville and more.", body, "/service-area/", "/service-area/")

def about_page():
    body = f'''
<div class="phero"><div class="bg" style="background-image:url(/images/ac-install.jpg)"></div><div class="shade"></div><div class="wrap">
 <div class="crumbs"><a href="/">{t("Home","Inicio")}</a> &rsaquo; {t("About","Nosotros")}</div>
 <h1>{t("A local A/C company that does the whole job","Una compañía local de A/C que hace el trabajo completo")}</h1>
 <p class="lead">{t("JR Refrigeration installs and services air conditioning and heating for homes and businesses across the Rio Grande Valley.","JR Refrigeration instala y da servicio a aire acondicionado y calefacción para casas y negocios en todo el Valle del Río Grande.")}</p></div></div>
<section><div class="wrap content">
 <div class="main">
  <h2>{t("What we believe","En qué creemos")}</h2>
  <p>{t("A new air conditioning system is one of the biggest purchases most families make for their home. You should get a clear price before the work starts, a complete system installed the right way, and a written warranty you can keep. That is the whole business.","Un sistema nuevo de aire acondicionado es una de las compras más grandes que una familia hace para su casa. Debe recibir un precio claro antes de empezar, un sistema completo instalado de la manera correcta y una garantía por escrito que pueda guardar. Ese es todo el negocio.")}</p>
  <h2>{t("What we do","Qué hacemos")}</h2>
  <ul class="ticks">
   <li>{I["check"]}<span>{t("New central A/C systems, 3 to 5 tons, with the indoor unit with heating and the outdoor unit","Sistemas centrales nuevos de 3 a 5 toneladas, con máquina de adentro con calefacción y máquina de afuera")}</span></li>
   <li>{I["check"]}<span>{t("Full system replacements","Reemplazos de sistema completo")}</span></li>
   <li>{I["check"]}<span>{t("Ductless mini splits, single and multi-zone","Mini splits sin ductos, de una y varias zonas")}</span></li>
   <li>{I["check"]}<span>{t("Heating installation and service","Instalación y servicio de calefacción")}</span></li>
   <li>{I["check"]}<span>{t("Commercial air conditioning and heating","Aire acondicionado y calefacción comercial")}</span></li>
  </ul>
  <h2>{t("Our warranty","Nuestra garantía")}</h2>
  <p>{t("10 years on parts and 2 years on labor, on every installation. You receive the warranty certificate and your invoice when the job is done.","10 años en partes y 2 años en mano de obra, en cada instalación. Recibe el certificado de garantía y su factura al terminar el trabajo.")}</p>
  <h2>{t("Where we work","Dónde trabajamos")}</h2>
  <p>{t("The whole Rio Grande Valley, from Mission to Brownsville. Advertised pricing applies to the Valley only.","Todo el Valle del Río Grande, de Mission a Brownsville. Los precios anunciados son solo para el Valle.")} <a href="/service-area/">{t("See the service area","Ver el área de servicio")}</a>.</p>
  <h2>{t("Two languages, one standard","Dos idiomas, un mismo estándar")}</h2>
  <p>{t("Call, text or write to us in English or Spanish. You get the same answers, the same price and the same warranty either way.","Llame, mande texto o escriba en inglés o español. Recibe las mismas respuestas, el mismo precio y la misma garantía de cualquier forma.")}</p>
 </div>
 <aside class="side">{lead_form(compact=True)}</aside>
</div></section>
{cta_final()}'''
    return page("About JR Refrigeration | A/C & Heating, Rio Grande Valley TX", "JR Refrigeration is a bilingual air conditioning and heating company serving the Rio Grande Valley with new systems, replacements and mini splits, backed by a 10-year parts / 2-year labor warranty.", body, "/about/", "/about/")

def contact_page():
    body = f'''
<div class="phero"><div class="bg" style="background-image:url(/images/thermostat.jpg)"></div><div class="shade"></div><div class="wrap">
 <div class="crumbs"><a href="/">{t("Home","Inicio")}</a> &rsaquo; {t("Contact","Contacto")}</div>
 <h1>{t("Get your free quote","Pida su cotización gratis")}</h1>
 <p class="lead">{t("Call, text, or send the form. We will call you back to set a time.","Llame, mande texto o envíe el formulario. Le llamamos para agendar.")}</p></div></div>
<section><div class="wrap content">
 <div class="main">
  <div class="card" style="margin-bottom:22px"><div class="icon">{I["phone"]}</div><h3>{t("Call or text","Llame o mande texto")}</h3><p style="font-size:1.05rem">{t("Fastest way to reach us. English or Spanish.","La forma más rápida de contactarnos. Inglés o español.")}</p><a class="btn btn-red btn-lg" href="tel:{TEL}">{I["phone"]} {PHONE}</a></div>
  <div class="card" style="margin-bottom:22px"><div class="icon">{I["pin"]}</div><h3>{t("Service area","Área de servicio")}</h3><p>{t("The whole Rio Grande Valley, Mission to Brownsville.","Todo el Valle del Río Grande, de Mission a Brownsville.")} <a href="/service-area/">{t("See cities","Ver ciudades")}</a></p></div>
  <div class="card"><div class="icon">{I["shield"]}</div><h3>{t("Warranty","Garantía")}</h3><p>{t("10 years parts, 2 years labor. Certificate and invoice delivered with every installation.","10 años partes, 2 años mano de obra. Certificado y factura entregados con cada instalación.")}</p></div>
 </div>
 <aside class="side">{lead_form()}</aside>
</div></section>'''
    return page("Contact JR Refrigeration | Free A/C Quote | (210) 946-0246", "Call or text (210) 946-0246 or send the form for a free quote on a new A/C system, replacement, mini split or heating in the Rio Grande Valley. English and Spanish.", body, "/contact/", "/contact/")

def thanks_page():
    body = f'''<section style="min-height:50vh"><div class="wrap" style="max-width:720px;text-align:center">
 <span class="eyebrow">{t("Request received","Solicitud recibida")}</span>
 <h1>{t("Thank you. We will call you shortly.","Gracias. Le llamamos en breve.")}</h1>
 <p class="lead">{t("If it is urgent, call or text us now.","Si es urgente, llame o mande texto ahora.")}</p>
 <a class="btn btn-red btn-lg" href="tel:{TEL}">{I["phone"]} {PHONE}</a>
 <p style="margin-top:30px"><a href="/">{t("Back to home","Volver al inicio")}</a></p>
</div></section>'''
    return page("Thank You | JR Refrigeration", "We received your request and will call you back shortly.", body, "/thank-you/", "", schema=False)

def privacy_page():
    body = f'''<section><div class="wrap" style="max-width:760px">
 <h1>{t("Privacy","Privacidad")}</h1>
 <p>{t("When you send our contact form, we receive the information you type (name, phone, email, city, service and message). We use it only to respond to your request and schedule service. We do not sell or share it with third parties for marketing.","Cuando envía nuestro formulario, recibimos la información que escribe (nombre, teléfono, email, ciudad, servicio y mensaje). La usamos solo para responder a su solicitud y agendar servicio. No la vendemos ni la compartimos con terceros para publicidad.")}</p>
 <p>{t("Form submissions are delivered by FormSubmit. This site uses no advertising cookies. The language toggle stores your choice in your browser only.","Los formularios se entregan a través de FormSubmit. Este sitio no usa cookies de publicidad. El selector de idioma guarda su preferencia solo en su navegador.")}</p>
 <p>{t("Questions? Call","¿Preguntas? Llame al")} <a href="tel:{TEL}">{PHONE}</a>.</p>
</div></section>'''
    return page("Privacy | JR Refrigeration", "How JR Refrigeration handles the information you send through this website.", body, "/privacy/", "", schema=False)

def notfound_page():
    body = f'''<section style="min-height:50vh"><div class="wrap" style="max-width:720px;text-align:center">
 <h1>{t("Page not found","Página no encontrada")}</h1><p class="lead">{t("That link is not here. Try the home page or call us.","Ese enlace no está aquí. Vaya al inicio o llámenos.")}</p>
 <a class="btn btn-blue" href="/">{t("Home","Inicio")}</a> <a class="btn btn-red" href="tel:{TEL}">{PHONE}</a></div></section>'''
    return page("Not Found | JR Refrigeration", "Page not found.", body, "/404.html", "", schema=False)

FAVICON = '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#0a2342"/><text x="32" y="43" text-anchor="middle" font-family="Montserrat,Arial,sans-serif" font-weight="900" font-size="30" fill="#fff">JR</text></svg>'

def write(rel, content):
    p = os.path.join(ROOT, rel); os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f: f.write(content)

def main():
    write("css/style.css", CSS.strip()+"\n"); write("js/main.js", JS.strip()+"\n"); write("favicon.svg", FAVICON)
    write("index.html", home())
    urls = ["/"]
    for s in SERVICES:
        write(f"services/{s['slug']}/index.html", service_page(s)); urls.append(f"/services/{s['slug']}/")
    write("service-area/index.html", area_page()); urls.append("/service-area/")
    write("about/index.html", about_page()); urls.append("/about/")
    write("contact/index.html", contact_page()); urls.append("/contact/")
    write("thank-you/index.html", thanks_page()); write("privacy/index.html", privacy_page()); urls.append("/privacy/")
    write("404.html", notfound_page())
    today = datetime.date.today().isoformat()
    write("sitemap.xml", '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(f"  <url><loc>{DOMAIN}{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls) + "</urlset>\n")
    write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
    print("built", len(urls), "pages")

if __name__ == "__main__": main()
