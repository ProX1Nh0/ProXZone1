from pathlib import Path

p = Path('index.html')
s = p.read_text(encoding='utf-8')
marker = '<!-- PROXZONE-UI-PATCH -->'
if marker in s:
    print('Patch already present')
    raise SystemExit(0)

patch = r'''<!-- PROXZONE-UI-PATCH -->
<style>
.pxz-cat-photo{width:36px;height:36px;border-radius:9px;object-fit:cover;display:block;flex-shrink:0;border:1px solid rgba(255,255,255,.12)}
.pxz-extra-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
.pxz-extra-card{background:var(--panel);border:1px solid var(--line);border-radius:14px;padding:16px;display:flex;flex-direction:column;gap:12px}
.pxz-extra-card:hover{border-color:rgba(61,139,255,.4);transform:translateY(-2px);transition:.18s}
.pxz-extra-card h4{font-family:'Orbitron',sans-serif;font-size:15px;margin:0}
.pxz-extra-card p{font-size:12.5px;color:var(--ink-soft);line-height:1.5;margin:0;flex:1}
.pxz-extra-play{border:0;border-radius:9px;padding:10px 14px;background:var(--grad);color:#07070f;font-weight:800;cursor:pointer}
#pxz-game-modal{position:fixed;inset:0;z-index:300;background:rgba(0,0,0,.82);backdrop-filter:blur(7px);display:none;align-items:center;justify-content:center;padding:20px}
#pxz-game-modal.open{display:flex}
.pxz-modal-box{width:min(1100px,96vw);height:min(760px,92vh);background:var(--panel);border:1px solid var(--line);border-radius:16px;overflow:hidden;display:flex;flex-direction:column;box-shadow:0 30px 80px rgba(0,0,0,.6)}
.pxz-modal-head{display:flex;align-items:center;justify-content:space-between;padding:12px 16px;border-bottom:1px solid var(--line);font-weight:800}
.pxz-modal-close{border:1px solid var(--line);background:var(--bg-2);color:var(--ink);border-radius:8px;padding:7px 11px;cursor:pointer}
.pxz-modal-frame{flex:1;min-height:0;background:#000}.pxz-modal-frame iframe{width:100%;height:100%;border:0;display:block}
#pxz-calculator{position:fixed;inset:0;z-index:400;background:radial-gradient(circle at 50% 20%,rgba(61,139,255,.22),transparent 45%),#07070f;display:flex;align-items:center;justify-content:center;padding:20px}
#pxz-calculator.hide{display:none}.pxz-calc-box{width:min(390px,94vw);background:var(--panel);border:1px solid var(--line);border-radius:18px;padding:20px;box-shadow:0 30px 90px rgba(0,0,0,.55)}
.pxz-calc-brand{font-family:'Orbitron',sans-serif;text-align:center;font-size:20px;margin-bottom:4px}.pxz-calc-sub{text-align:center;color:var(--ink-soft);font-size:12px;margin-bottom:16px}
.pxz-calc-display{width:100%;height:58px;background:#080912;border:1px solid var(--line);border-radius:10px;color:var(--ink);font-size:24px;text-align:right;padding:10px 12px;margin-bottom:12px;outline:none}
.pxz-calc-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:8px}.pxz-calc-grid button{height:48px;border:1px solid var(--line);border-radius:9px;background:var(--bg-2);color:var(--ink);font-size:16px;font-weight:700;cursor:pointer}
.pxz-calc-grid .op{color:var(--blue)}.pxz-calc-grid .eq{background:var(--grad);color:#07070f;border:0}.pxz-enter{width:100%;margin-top:12px;border:0;border-radius:10px;padding:12px;background:var(--grad);color:#07070f;font-weight:900;cursor:pointer}
@media(max-width:700px){.pxz-extra-grid{grid-template-columns:1fr}.pxz-modal-box{height:88vh}}
</style>
<script>
(function(){
const IMG={esporte:'https://commons.wikimedia.org/wiki/Special:FilePath/Soccer_ball.jpg',esportes:'https://commons.wikimedia.org/wiki/Special:FilePath/Soccer_ball.jpg',tabuleiro:'https://commons.wikimedia.org/wiki/Special:FilePath/Chess_board.jpg',acao:'https://commons.wikimedia.org/wiki/Special:FilePath/Sports_car_(40652604980).jpg','ação':'https://commons.wikimedia.org/wiki/Special:FilePath/Sports_car_(40652604980).jpg'};
function categories(){document.querySelectorAll('.cat-item').forEach(x=>{let l=(x.querySelector('.cat-text b')?.textContent||'').trim().toLowerCase(),u=IMG[l],b=x.querySelector('.cat-icon');if(u&&b&&!b.querySelector('.pxz-cat-photo')){b.innerHTML='<img class="pxz-cat-photo" src="'+u+'" alt="'+l+'">';}})}
function brand(){let o=document.querySelector('.brand-logo');if(!o||o.dataset.pxzDone)return;o.dataset.pxzDone='1';let w=document.createElement('div');w.setAttribute('aria-label','ProXZone');w.style.cssText='height:42px;width:48px;display:flex;align-items:center;justify-content:center;color:var(--ink);filter:drop-shadow(0 0 10px rgba(61,139,255,.35))';w.innerHTML='<svg viewBox="0 0 64 64" width="40" height="40"><rect x="7" y="14" width="50" height="36" rx="10" fill="none" stroke="currentColor" stroke-width="5"/><path d="M18 32h10M23 27v10M42 29h.1M49 36h.1" stroke="currentColor" stroke-width="5" stroke-linecap="round"/><path d="M29 14l5-7 5 7" fill="none" stroke="currentColor" stroke-width="4" stroke-linecap="round"/></svg>';o.replaceWith(w)}
function modal(){if(document.getElementById('pxz-game-modal'))return;let m=document.createElement('div');m.id='pxz-game-modal';m.innerHTML='<div class="pxz-modal-box"><div class="pxz-modal-head"><span id="pxz-modal-title">Jogo</span><button class="pxz-modal-close">Fechar ✕</button></div><div class="pxz-modal-frame"></div></div>';document.body.appendChild(m);m.querySelector('.pxz-modal-close').onclick=close;m.onclick=e=>{if(e.target===m)close()}}
function open(t,u){modal();let m=document.getElementById('pxz-game-modal');document.getElementById('pxz-modal-title').textContent=t;m.querySelector('.pxz-modal-frame').innerHTML='<iframe src="'+u+'" title="'+t+'" allow="autoplay; fullscreen; gamepad" allowfullscreen referrerpolicy="strict-origin-when-cross-origin"></iframe>';m.classList.add('open')}
function close(){let m=document.getElementById('pxz-game-modal');if(m){m.classList.remove('open');m.querySelector('.pxz-modal-frame').innerHTML=''}}
function games(){if(document.getElementById('pxz-extra-catalog'))return;let main=document.querySelector('.main')||document.querySelector('main');if(!main)return;let sec=document.createElement('section');sec.id='pxz-extra-catalog';sec.innerHTML='<div class="cat-section-head"><div class="cat-section-icon" style="background:rgba(61,139,255,.15)">🎮</div><div><h3>Mais jogos</h3><span>Um destaque de cada catálogo</span></div></div><div class="pxz-extra-grid"></div>';let grid=sec.querySelector('.pxz-extra-grid');[['Esportes','Soccer Random','Jogo de futebol para dois jogadores.','https://www.gamepix.com/play/soccer-random'],['Tabuleiro','Xadrez','Partida de xadrez dentro do ProXZone.','https://gamezipper.com/chess/?utm_source=proxzone'],['Ação','Slope','Desvie dos obstáculos e mantenha a bola na pista.','https://gamezipper.com/slope/?utm_source=proxzone']].forEach(g=>{let c=document.createElement('article');c.className='pxz-extra-card';c.innerHTML='<div style="font-size:11px;color:var(--blue);font-weight:800;text-transform:uppercase;letter-spacing:.8px">'+g[0]+'</div><h4>'+g[1]+'</h4><p>'+g[2]+'</p><button class="pxz-extra-play">Jogar agora ▶</button>';c.querySelector('button').onclick=()=>open(g[1],g[3]);grid.appendChild(c)});main.appendChild(sec)}
function calc(){if(document.getElementById('pxz-calculator'))return;let c=document.createElement('div');c.id='pxz-calculator';c.innerHTML='<div class="pxz-calc-box"><div class="pxz-calc-brand">ProXZone</div><div class="pxz-calc-sub">Calculadora rápida antes de entrar</div><input class="pxz-calc-display" id="pxz-calc-display" readonly><div class="pxz-calc-grid"><button data-v="C" class="op">C</button><button data-v="back" class="op">⌫</button><button data-v="(" class="op">(</button><button data-v=")" class="op">)</button><button data-v="7">7</button><button data-v="8">8</button><button data-v="9">9</button><button data-v="/" class="op">÷</button><button data-v="4">4</button><button data-v="5">5</button><button data-v="6">6</button><button data-v="*" class="op">×</button><button data-v="1">1</button><button data-v="2">2</button><button data-v="3">3</button><button data-v="-" class="op">−</button><button data-v="0">0</button><button data-v=".">.</button><button data-v="+" class="op">+</button><button data-v="=" class="eq">=</button></div><button class="pxz-enter" id="pxz-enter">Entrar no ProXZone 🎮</button></div>';document.body.appendChild(c);let d=c.querySelector('#pxz-calc-display');c.querySelectorAll('[data-v]').forEach(b=>b.onclick=()=>{let v=b.dataset.v;if(v==='C')d.value='';else if(v==='back')d.value=d.value.slice(0,-1);else if(v==='='){if(!/^[0-9+*/().\-\s]+$/.test(d.value))return;try{let r=Function('"use strict";return ('+d.value+')')();d.value=Number.isFinite(r)?String(r):'Erro'}catch(e){d.value='Erro'}}else d.value==='Erro'?d.value=v:d.value+=v});c.querySelector('#pxz-enter').onclick=()=>c.classList.add('hide')}
function boot(){brand();categories();games();calc();setTimeout(categories,700)}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',boot);else boot();
})();
</script>
'''
if '</body>' not in s:
    raise SystemExit('closing body not found')
s=s.replace('</body>',patch+'\n</body>',1)
p.write_text(s,encoding='utf-8')
print('ProXZone patch applied')
