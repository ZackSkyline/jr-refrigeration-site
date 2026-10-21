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
