
html = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
<meta name="theme-color" content="#000000">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<title>MetaNex AI Pro | Institutional Trading Terminal</title>
<style>
:root{--bg:#000;--surface:#0a0a0a;--surface2:#141414;--surface3:#1c1c1c;--border:#222;--border2:#333;--text:#fff;--text2:#8e8e93;--text3:#636366;--accent:#0a84ff;--accent2:#5e5ce6;--up:#30d158;--down:#ff453a;--warn:#ff9f0a;--gold:#ffd60a;--purple:#bf5af2;--cyan:#64d2ff;--green2:#34c759;}
*{margin:0;padding:0;box-sizing:border-box;-webkit-tap-highlight-color:transparent;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;}
html,body{height:100%;width:100%;overflow:hidden;background:var(--bg);color:var(--text);}
.screen{display:none;height:100%;width:100%;flex-direction:column;position:absolute;inset:0;}
.screen.active{display:flex;}

/* HEADER */
.header{height:56px;background:var(--bg);border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;padding:0 12px;flex-shrink:0;z-index:50;}
.header-left,.header-right{display:flex;align-items:center;gap:4px;}
.header-title{font-size:18px;font-weight:600;letter-spacing:-0.3px;}
.icon-btn{width:40px;height:40px;border-radius:50%;display:flex;align-items:center;justify-content:center;background:transparent;border:none;color:var(--text);font-size:20px;cursor:pointer;transition:background .15s;}
.icon-btn:active{background:var(--surface2);}
.icon-btn svg{width:22px;height:22px;}

/* CONTENT */
.content{flex:1;overflow-y:auto;overflow-x:hidden;-webkit-overflow-scrolling:touch;position:relative;}
::-webkit-scrollbar{width:0;background:transparent;}

/* BOTTOM NAV */
.bottom-nav{height:64px;background:var(--surface);border-top:1px solid var(--border);display:flex;justify-content:space-around;align-items:center;flex-shrink:0;padding-bottom:env(safe-area-inset-bottom,0);backdrop-filter:blur(20px);}
.nav-item{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px;cursor:pointer;color:var(--text2);height:100%;transition:all .2s;position:relative;}
.nav-item.active{color:var(--accent);}
.nav-item svg{width:22px;height:22px;}
.nav-item span{font-size:10px;font-weight:500;}
.nav-badge{position:absolute;top:6px;right:calc(50% - 16px);background:var(--down);color:#fff;font-size:9px;width:16px;height:16px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;}

/* SIDE MENU */
.menu-overlay{position:fixed;inset:0;background:rgba(0,0,0,.6);z-index:100;opacity:0;pointer-events:none;transition:opacity .25s;backdrop-filter:blur(4px);}
.menu-overlay.open{opacity:1;pointer-events:auto;}
.side-menu{position:fixed;left:0;top:0;bottom:0;width:85%;max-width:340px;background:linear-gradient(180deg,var(--surface) 0%,var(--bg) 100%);z-index:101;transform:translateX(-100%);transition:transform .35s cubic-bezier(.32,.72,0,1);display:flex;flex-direction:column;border-right:1px solid var(--border);}
.side-menu.open{transform:translateX(0);}
.menu-header{padding:20px 16px 16px;border-bottom:1px solid var(--border);background:var(--surface2);}
.menu-account-row{display:flex;align-items:center;gap:12px;margin-bottom:8px;}
.menu-avatar{width:44px;height:44px;border-radius:50%;background:linear-gradient(135deg,var(--accent),var(--purple));display:flex;align-items:center;justify-content:center;font-weight:700;font-size:18px;}
.menu-account-info{flex:1;}
.menu-account-name{font-size:17px;font-weight:600;}
.menu-server{font-size:13px;color:var(--text2);margin-top:2px;}
.menu-manage{color:var(--accent);font-size:14px;cursor:pointer;margin-top:8px;display:inline-block;}
.menu-section-title{font-size:11px;text-transform:uppercase;letter-spacing:1px;color:var(--text3);padding:16px 16px 8px;font-weight:600;}
.menu-link{display:flex;align-items:center;gap:14px;padding:13px 16px;cursor:pointer;transition:background .1s;border-bottom:1px solid rgba(255,255,255,.03);}
.menu-link:active{background:var(--surface2);}
.menu-link svg{width:22px;height:22px;color:var(--text2);flex-shrink:0;}
.menu-link span{font-size:15px;}
.menu-link .right{margin-left:auto;display:flex;align-items:center;gap:8px;}
.menu-badge{background:var(--down);color:#fff;font-size:10px;min-width:20px;height:20px;border-radius:10px;display:flex;align-items:center;justify-content:center;padding:0 6px;font-weight:600;}
.ads-badge{border:1px solid var(--accent);color:var(--accent);font-size:10px;padding:2px 8px;border-radius:4px;}
.menu-footer{padding:16px;border-top:1px solid var(--border);margin-top:auto;}
.menu-status{display:flex;align-items:center;gap:8px;font-size:13px;color:var(--text2);}
.status-dot{width:8px;height:8px;border-radius:50%;background:var(--up);animation:pulse 2s infinite;}
@keyframes pulse{0%,100%{opacity:1;}50%{opacity:.4;}}

/* TOAST */
.toast{position:fixed;top:64px;left:50%;transform:translateX(-50%) translateY(-30px);background:var(--surface3);border:1px solid var(--border2);color:var(--text);padding:12px 20px;border-radius:12px;font-size:14px;z-index:200;opacity:0;pointer-events:none;transition:all .3s;white-space:nowrap;box-shadow:0 8px 32px rgba(0,0,0,.4);}
.toast.show{opacity:1;transform:translateX(-50%) translateY(0);}

/* MODAL */
.modal-overlay{position:fixed;inset:0;background:rgba(0,0,0,.7);z-index:150;opacity:0;pointer-events:none;transition:opacity .2s;display:flex;align-items:flex-end;justify-content:center;}
.modal-overlay.open{opacity:1;pointer-events:auto;}
.modal-sheet{background:var(--surface2);width:100%;max-width:420px;border-radius:24px 24px 0 0;padding:20px 0;transform:translateY(100%);transition:transform .3s cubic-bezier(.32,.72,0,1);max-height:85vh;overflow-y:auto;}
.modal-overlay.open .modal-sheet{transform:translateY(0);}
.modal-header{padding:0 20px 16px;display:flex;align-items:center;justify-content:space-between;border-bottom:1px solid var(--border);margin-bottom:8px;}
.modal-title{font-size:18px;font-weight:700;}
.modal-close{width:32px;height:32px;border-radius:50%;background:var(--surface3);border:none;color:var(--text);font-size:18px;cursor:pointer;display:flex;align-items:center;justify-content:center;}
.modal-row{padding:14px 20px;display:flex;align-items:center;gap:12px;cursor:pointer;border-bottom:1px solid rgba(255,255,255,.03);}
.modal-row:active{background:var(--surface3);}
.modal-row svg{width:20px;height:20px;color:var(--text2);}
.modal-row span{font-size:15px;}

/* LOGIN */
.login-hero{text-align:center;padding:32px 24px 16px;}
.login-hero .logo{width:72px;height:72px;border-radius:20px;background:linear-gradient(135deg,var(--accent),var(--purple));margin:0 auto 16px;display:flex;align-items:center;justify-content:center;font-size:32px;box-shadow:0 8px 32px rgba(10,132,255,.3);}
.login-hero h1{font-size:24px;font-weight:700;margin-bottom:6px;}
.login-hero p{font-size:14px;color:var(--text2);}
.broker-card{display:flex;align-items:center;gap:14px;padding:16px 20px;margin:8px 16px;background:var(--surface2);border-radius:16px;border:1px solid var(--border);cursor:pointer;transition:all .2s;}
.broker-card:active{transform:scale(.98);}
.broker-logo{width:48px;height:48px;border-radius:14px;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:20px;flex-shrink:0;}
.broker-info{flex:1;}
.broker-name{font-size:16px;font-weight:600;}
.broker-meta{font-size:13px;color:var(--accent);margin-top:2px;}
.login-form{padding:8px 24px 24px;}
.input-group{margin-bottom:20px;position:relative;}
.input-group label{display:block;color:var(--text2);font-size:13px;margin-bottom:8px;text-transform:uppercase;letter-spacing:.5px;font-weight:500;}
.input-group input,.input-group select{width:100%;background:var(--surface2);border:1px solid var(--border);border-radius:12px;color:var(--text);font-size:16px;padding:14px 16px;outline:none;transition:border .2s;-webkit-appearance:none;}
.input-group input:focus,.input-group select:focus{border-color:var(--accent);}
.input-group input::placeholder{color:var(--text3);}
.checkbox-row{display:flex;align-items:center;justify-content:space-between;margin:20px 0;}
.checkbox-row label{color:var(--text2);font-size:14px;}
.check-box{width:24px;height:24px;border-radius:6px;background:var(--accent);display:flex;align-items:center;justify-content:center;font-size:14px;color:#fff;}
.btn-primary{width:100%;padding:16px;border-radius:14px;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border:none;font-size:16px;font-weight:700;cursor:pointer;transition:all .2s;box-shadow:0 4px 20px rgba(10,132,255,.3);}
.btn-primary:active{transform:scale(.98);opacity:.9;}
.btn-secondary{width:100%;padding:14px;border-radius:14px;background:var(--surface2);color:var(--text);border:1px solid var(--border);font-size:15px;font-weight:600;cursor:pointer;margin-top:10px;}
.link-text{text-align:center;color:var(--accent);font-size:14px;margin-top:16px;cursor:pointer;padding:8px;}
.divider{display:flex;align-items:center;gap:12px;padding:16px 24px;color:var(--text3);font-size:13px;}
.divider::before,.divider::after{flex:1;height:1px;background:var(--border);content:'';}

/* QUOTES */
.quote-item{display:flex;align-items:center;justify-content:space-between;padding:14px 16px;border-bottom:1px solid var(--border);cursor:pointer;transition:background .1s;position:relative;}
.quote-item:active{background:var(--surface2);}
.quote-item::before{content:'';position:absolute;left:0;top:0;bottom:0;width:3px;background:transparent;transition:background .2s;}
.quote-item.active::before{background:var(--accent);}
.quote-left{flex:1;}
.quote-pair{font-size:17px;font-weight:700;letter-spacing:-0.3px;}
.quote-meta{display:flex;align-items:center;gap:8px;margin-top:4px;}
.quote-time{font-size:11px;color:var(--text3);}
.quote-spread{font-size:11px;color:var(--text3);background:var(--surface2);padding:2px 6px;border-radius:4px;}
.quote-change{font-size:13px;font-weight:600;margin-top:2px;}
.quote-change.up{color:var(--up);}
.quote-change.down{color:var(--down);}
.quote-prices{text-align:right;}
.price-row{display:flex;align-items:baseline;gap:8px;justify-content:flex-end;}
.price-bid,.price-ask{font-size:22px;font-weight:300;font-variant-numeric:tabular-nums;letter-spacing:-0.5px;}
.price-bid sup,.price-ask sup{font-size:11px;font-weight:700;margin-left:1px;opacity:.8;}
.price-ext{font-size:12px;color:var(--text3);margin-top:4px;}
.price-arrow{font-size:10px;margin-left:2px;}

/* CHART */
.chart-topbar{display:flex;align-items:center;justify-content:space-between;padding:10px 16px;border-bottom:1px solid var(--border);background:var(--bg);}
.chart-symbol{font-size:15px;font-weight:700;color:var(--accent);cursor:pointer;display:flex;align-items:center;gap:6px;}
.chart-time{font-size:13px;color:var(--text2);background:var(--surface2);padding:4px 10px;border-radius:8px;cursor:pointer;}
.chart-container{position:relative;flex:1;background:var(--bg);overflow:hidden;}
#candleCanvas{width:100%;height:100%;display:block;}
.chart-sidebar{position:absolute;left:0;top:0;bottom:0;width:130px;background:rgba(10,10,10,.97);border-right:1px solid var(--border);transform:translateX(-100%);transition:transform .25s;z-index:10;overflow-y:auto;backdrop-filter:blur(10px);}
.chart-sidebar.open{transform:translateX(0);}
.sym-list-item{padding:12px 14px;font-size:14px;border-bottom:1px solid rgba(255,255,255,.04);cursor:pointer;display:flex;align-items:center;justify-content:space-between;}
.sym-list-item.active{color:var(--accent);background:var(--surface2);}
.sym-list-item:active{background:var(--surface2);}
.sym-list-item .sym-status{width:6px;height:6px;border-radius:50%;background:var(--up);}
.chart-tools{position:absolute;right:10px;top:10px;display:flex;flex-direction:column;gap:8px;z-index:5;}
.tool-btn{width:40px;height:40px;border-radius:12px;background:rgba(20,20,20,.9);border:1px solid var(--border);color:var(--text);display:flex;align-items:center;justify-content:center;font-size:16px;cursor:pointer;backdrop-filter:blur(10px);transition:all .15s;}
.tool-btn:active{background:var(--accent);color:#fff;}
.chart-overlay-btn{position:absolute;left:8px;top:50%;transform:translateY(-50%);width:36px;height:36px;background:rgba(20,20,20,.9);border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:18px;cursor:pointer;z-index:5;border:1px solid var(--border);backdrop-filter:blur(10px);color:var(--text2);}
.chart-info-panel{position:absolute;left:10px;top:10px;background:rgba(10,10,10,.85);border:1px solid var(--border);border-radius:12px;padding:10px 14px;z-index:5;backdrop-filter:blur(10px);}
.chart-info-row{display:flex;align-items:center;gap:12px;font-size:12px;color:var(--text2);}
.chart-info-row span.value{color:var(--text);font-weight:600;}
.chart-info-row.up .value{color:var(--up);}
.chart-info-row.down .value{color:var(--down);}

/* TRADE */
.trade-stats{padding:16px;border-bottom:1px solid var(--border);}
.stat-row{display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;}
.stat-row:last-child{margin-bottom:0;}
.stat-label{font-size:15px;color:var(--text);}
.stat-dots{flex:1;border-bottom:2px dotted var(--border2);margin:0 10px 4px;}
.stat-value{font-size:15px;font-variant-numeric:tabular-nums;font-weight:600;}
.ai-status-bar{padding:10px 16px;background:linear-gradient(90deg,rgba(10,132,255,.1),rgba(191,90,242,.1));border-bottom:1px solid var(--border);display:flex;align-items:center;gap:10px;}
.ai-status-bar .pulse{width:10px;height:10px;border-radius:50%;background:var(--up);animation:pulse 1.5s infinite;box-shadow:0 0 10px var(--up);}
.ai-status-bar span{font-size:13px;color:var(--text2);}
.ai-status-bar span strong{color:var(--up);}
.positions-header{padding:12px 16px;font-size:12px;color:var(--text3);text-transform:uppercase;letter-spacing:.8px;font-weight:700;display:flex;align-items:center;justify-content:space-between;}
.position-item{padding:14px 16px;border-bottom:1px solid var(--border);display:flex;justify-content:space-between;align-items:center;transition:background .1s;}
.position-item:active{background:var(--surface2);}
.pos-info{flex:1;}
.pos-pair{font-size:15px;font-weight:700;}
.pos-detail{font-size:12px;color:var(--text3);margin-top:3px;line-height:1.4;}
.pos-pl{font-size:15px;font-weight:700;}
.pos-pl.up{color:var(--up);}
.pos-pl.down{color:var(--down);}
.empty-state{flex:1;display:flex;flex-direction:column;align-items:center;justify-content:center;color:var(--text3);padding:40px;text-align:center;}
.empty-icon{font-size:56px;margin-bottom:16px;opacity:.25;}
.empty-title{font-size:16px;font-weight:600;color:var(--text2);margin-bottom:6px;}
.empty-desc{font-size:13px;color:var(--text3);max-width:240px;line-height:1.5;}

/* TRADE BUTTONS */
.trade-actions{padding:16px;display:grid;grid-template-columns:1fr 1fr;gap:12px;}
.trade-btn{padding:16px;border-radius:16px;border:none;font-size:16px;font-weight:700;cursor:pointer;transition:all .15s;display:flex;flex-direction:column;align-items:center;gap:4px;}
.trade-btn:active{transform:scale(.97);}
.trade-btn.buy{background:linear-gradient(135deg,#30d158,#248a3d);color:#fff;box-shadow:0 4px 20px rgba(48,209,88,.25);}
.trade-btn.sell{background:linear-gradient(135deg,#ff453a,#d70015);color:#fff;box-shadow:0 4px 20px rgba(255,69,58,.25);}
.trade-btn .sub{font-size:11px;opacity:.8;font-weight:500;}

/* HISTORY */
.hist-tabs{display:flex;border-bottom:1px solid var(--border);}
.hist-tab{flex:1;text-align:center;padding:14px;font-size:12px;color:var(--text3);cursor:pointer;text-transform:uppercase;letter-spacing:.8px;font-weight:700;border-bottom:2px solid transparent;transition:all .2s;}
.hist-tab.active{color:var(--accent);border-bottom-color:var(--accent);}
.deal-item{padding:14px 16px;border-bottom:1px solid var(--border);display:flex;justify-content:space-between;align-items:center;}
.deal-info{flex:1;}
.deal-pair{font-size:15px;font-weight:700;}
.deal-detail{font-size:12px;color:var(--text3);margin-top:3px;}
.deal-pl{font-size:15px;font-weight:700;}

/* AI CHAT */
.chat-container{flex:1;display:flex;flex-direction:column;overflow:hidden;position:relative;}
.chat-bg{position:absolute;inset:0;opacity:.03;pointer-events:none;background-image:radial-gradient(circle at 20% 50%,var(--accent) 0%,transparent 50%),radial-gradient(circle at 80% 80%,var(--purple) 0%,transparent 50%);}
.chat-messages{flex:1;overflow-y:auto;padding:16px;display:flex;flex-direction:column;gap:14px;position:relative;z-index:1;}
.msg-bubble{max-width:82%;padding:12px 16px;border-radius:20px;font-size:14px;line-height:1.5;word-wrap:break-word;animation:msgIn .25s ease;position:relative;}
@keyframes msgIn{from{opacity:0;transform:translateY(8px) scale(.96);}to{opacity:1;transform:translateY(0) scale(1);}}
.msg-bubble.user{align-self:flex-end;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border-bottom-right-radius:6px;}
.msg-bubble.ai{align-self:flex-start;background:var(--surface2);color:var(--text);border-bottom-left-radius:6px;border:1px solid var(--border);}
.msg-bubble.system{align-self:center;background:transparent;color:var(--text3);font-size:12px;max-width:90%;text-align:center;padding:8px 16px;}
.msg-bubble .msg-time{font-size:10px;opacity:.6;margin-top:6px;}
.msg-bubble.ai .msg-time{color:var(--text3);}
.chat-input-area{padding:12px 12px 24px;border-top:1px solid var(--border);display:flex;gap:10px;align-items:flex-end;background:var(--surface);position:relative;z-index:2;}
.chat-input{flex:1;background:var(--surface2);border:1px solid var(--border);border-radius:24px;padding:12px 18px;color:var(--text);font-size:15px;outline:none;max-height:120px;resize:none;line-height:1.4;transition:border .2s;}
.chat-input:focus{border-color:var(--accent);}
.send-btn{width:44px;height:44px;border-radius:50%;background:linear-gradient(135deg,var(--accent),var(--accent2));color:#fff;border:none;display:flex;align-items:center;justify-content:center;font-size:18px;cursor:pointer;flex-shrink:0;transition:all .15s;box-shadow:0 4px 15px rgba(10,132,255,.3);}
.send-btn:active{transform:scale(.9);}
.typing-indicator{display:flex;gap:4px;padding:14px 16px;align-items:center;}
.typing-dot{width:7px;height:7px;background:var(--text3);border-radius:50%;animation:bounce 1.4s infinite;}
.typing-dot:nth-child(2){animation-delay:.2s;}
.typing-dot:nth-child(3){animation-delay:.4s;}
@keyframes bounce{0%,80%,100%{transform:translateY(0);}40%{transform:translateY(-6px);}}
.ai-welcome{padding:20px;text-align:center;}
.ai-welcome h2{font-size:20px;margin-bottom:8px;background:linear-gradient(90deg,var(--accent),var(--purple));-webkit-background-clip:text;-webkit-text-fill-color:transparent;}
.ai-welcome p{font-size:13px;color:var(--text2);line-height:1.6;max-width:280px;margin:0 auto;}
.quick-chips{display:flex;gap:8px;padding:0 16px 12px;overflow-x:auto;flex-wrap:nowrap;}
.quick-chip{background:var(--surface2);border:1px solid var(--border);border-radius:20px;padding:8px 16px;font-size:13px;color:var(--text2);cursor:pointer;white-space:nowrap;transition:all .15s;}
.quick-chip:active{background:var(--accent);color:#fff;border-color:var(--accent);}

/* AI DASHBOARD */
.ai-dashboard{padding:16px;display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-bottom:8px;}
.ai-card{background:var(--surface2);border:1px solid var(--border);border-radius:16px;padding:14px;}
.ai-card-label{font-size:11px;color:var(--text3);text-transform:uppercase;letter-spacing:.5px;margin-bottom:6px;}
.ai-card-value{font-size:20px;font-weight:700;}
.ai-card-sub{font-size:12px;color:var(--text2);margin-top:2px;}
.ai-card.up .ai-card-value{color:var(--up);}
.ai-card.down .ai-card-value{color:var(--down);}
.ai-master-toggle{padding:16px;margin:0 16px 16px;background:linear-gradient(90deg,rgba(10,132,255,.15),rgba(191,90,242,.15));border:1px solid rgba(10,132,255,.3);border-radius:16px;display:flex;align-items:center;justify-content:space-between;cursor:pointer;transition:all .2s;}
.ai-master-toggle:active{transform:scale(.98);}
.ai-master-toggle.active{background:linear-gradient(90deg,rgba(48,209,88,.15),rgba(10,132,255,.15));border-color:rgba(48,209,88,.3);}
.ai-toggle-left{display:flex;align-items:center;gap:12px;}
.ai-toggle-icon{width:44px;height:44px;border-radius:14px;background:linear-gradient(135deg,var(--accent),var(--purple));display:flex;align-items:center;justify-content:center;font-size:20px;}
.ai-toggle-text h3{font-size:16px;margin-bottom:2px;}
.ai-toggle-text p{font-size:12px;color:var(--text2);}
.toggle-switch{width:52px;height:30px;border-radius:15px;background:var(--surface3);position:relative;cursor:pointer;transition:background .3s;border:1px solid var(--border);}
.toggle-switch::after{content:'';position:absolute;width:26px;height:26px;border-radius:50%;background:#fff;top:1px;left:1px;transition:transform .3s;box-shadow:0 2px 8px rgba(0,0,0,.3);}
.toggle-switch.on{background:var(--up);border-color:var(--up);}
.toggle-switch.on::after{transform:translateX(22px);}

/* NEWS */
.news-item{padding:16px;border-bottom:1px solid var(--border);cursor:pointer;}
.news-item:active{background:var(--surface2);}
.news-time{font-size:11px;color:var(--accent);margin-bottom:6px;font-weight:600;}
.news-title{font-size:15px;font-weight:600;line-height:1.4;margin-bottom:6px;}
.news-desc{font-size:13px;color:var(--text2);line-height:1.5;}
.news-tag{display:inline-block;background:var(--surface2);color:var(--text2);font-size:11px;padding:3px 10px;border-radius:6px;margin-top:8px;}

/* SETTINGS */
.settings-group{margin-bottom:8px;}
.settings-header{padding:16px 16px 8px;font-size:12px;color:var(--text3);text-transform:uppercase;letter-spacing:.8px;font-weight:700;}
.settings-row{display:flex;align-items:center;justify-content:space-between;padding:14px 16px;border-bottom:1px solid var(--border);cursor:pointer;}
.settings-row:active{background:var(--surface2);}
.settings-row-left{display:flex;align-items:center;gap:12px;}
.settings-row-left svg{width:20px;height:20px;color:var(--text2);}
.settings-row-title{font-size:15px;}
.settings-row-desc{font-size:12px;color:var(--text3);margin-top:2px;}
.settings-row-value{font-size:14px;color:var(--text2);display:flex;align-items:center;gap:6px;}

/* ECONOMIC CALENDAR */
.cal-item{padding:14px 16px;border-bottom:1px solid var(--border);display:flex;align-items:center;gap:12px;}
.cal-time{width:48px;text-align:center;flex-shrink:0;}
.cal-time .hour{font-size:16px;font-weight:700;}
.cal-time .min{font-size:11px;color:var(--text3);}
.cal-flag{width:28px;height:28px;border-radius:50%;background:var(--surface2);display:flex;align-items:center;justify-content:center;font-size:14px;}
.cal-info{flex:1;}
.cal-event{font-size:14px;font-weight:600;margin-bottom:2px;}
.cal-forecast{font-size:12px;color:var(--text2);}
.cal-impact{padding:3px 10px;border-radius:6px;font-size:11px;font-weight:700;}
.cal-impact.high{background:rgba(255,69,58,.15);color:var(--down);}
.cal-impact.medium{background:rgba(255,159,10,.15);color:var(--warn);}
.cal-impact.low{background:rgba(48,209,88,.15);color:var(--up);}

/* ADD SYMBOL */
.search-box{margin:12px 16px;background:var(--surface2);border-radius:12px;padding:12px 16px;display:flex;align-items:center;gap:10px;border:1px solid var(--border);}
.search-box input{background:transparent;border:none;color:var(--text);font-size:16px;outline:none;width:100%;}
.search-box input::placeholder{color:var(--text3);}
.folder-item{display:flex;align-items:center;justify-content:space-between;padding:16px;border-bottom:1px solid var(--border);cursor:pointer;}
.folder-item:active{background:var(--surface2);}
.folder-left{display:flex;align-items:center;gap:12px;}
.folder-icon{width:40px;height:40px;background:linear-gradient(135deg,#ffcc00,#ff9500);border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:18px;}
.folder-name{font-size:16px;font-weight:600;}
.folder-count{font-size:14px;color:var(--text3);}

/* SIGNALS */
.signal-card{margin:8px 16px;padding:16px;background:var(--surface2);border:1px solid var(--border);border-radius:16px;}
.signal-header{display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;}
.signal-pair{font-size:18px;font-weight:700;}
.signal-badge{padding:4px 12px;border-radius:8px;font-size:12px;font-weight:700;text-transform:uppercase;}
.signal-badge.buy{background:rgba(48,209,88,.15);color:var(--up);}
.signal-badge.sell{background:rgba(255,69,58,.15);color:var(--down);}
.signal-row{display:flex;justify-content:space-between;padding:8px 0;border-bottom:1px solid rgba(255,255,255,.04);}
.signal-row:last-child{border-bottom:none;}
.signal-label{font-size:13px;color:var(--text2);}
.signal-value{font-size:14px;font-weight:600;}
.signal-tp{color:var(--up);}
.signal-sl{color:var(--down);}
.signal-confidence{margin-top:12px;height:6px;background:var(--surface3);border-radius:3px;overflow:hidden;}
.signal-confidence-bar{height:100%;border-radius:3px;background:linear-gradient(90deg,var(--accent),var(--purple));transition:width .5s ease;}
.signal-conf-text{font-size:12px;color:var(--text2);margin-top:6px;text-align:right;}

/* ANIMATIONS */
@keyframes fadeIn{from{opacity:0;}to{opacity:1;}}
@keyframes slideUp{from{transform:translateY(20px);opacity:0;}to{transform:translateY(0);opacity:1;}}
.animate-fade{animation:fadeIn .4s ease;}
.animate-slide{animation:slideUp .4s ease;}

/* RESPONSIVE */
@media(min-width:768px){.side-menu{width:320px;}.modal-sheet{border-radius:24px;max-height:70vh;margin-bottom:20px;}}
</style>
</head>
<body>

<!-- TOAST -->
<div class="toast" id="toast"></div>

<!-- MODAL OVERLAY -->
<div class="modal-overlay" id="modalOverlay" onclick="closeModal()"><div class="modal-sheet" id="modalSheet" onclick="event.stopPropagation()"></div></div>

<!-- SIDE MENU -->
<div class="menu-overlay" id="menuOverlay" onclick="toggleMenu()"></div>
<div class="side-menu" id="sideMenu">
<div class="menu-header">
<div class="menu-account-row">
<div class="menu-avatar">AI</div>
<div class="menu-account-info">
<div class="menu-account-name">MetaNex AI Pro</div>
<div class="menu-server">436002224 • Exness-MT5Trial9</div>
</div>
</div>
<span class="menu-manage" onclick="showScreen('brokers');toggleMenu();">Manage accounts</span>
</div>
<div class="content">
<div class="menu-section-title">Trading</div>
<div class="menu-link" onclick="switchTab('trade');toggleMenu();">
<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/></svg>
<span>Trade</span>
</div>
<div class="menu-link" onclick="switchTab('ai');toggleMenu();">
<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>
<span>AI Command Center</span>
<div class="right"><div class="menu-badge" id="aiMenuBadge">ON</div></div>
</div>
<div class="menu-link" onclick="switchTab('quotes');toggleMenu();">
<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M7 16V4m0 0L3 8m4-4l4 4m6 12V8m0 0l-4 4m4-4l4 4"/></svg>
<span>Quotes</span>
</div>
<div class="menu-link" onclick="switchTab('charts');toggleMenu();">
<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>
<span>Charts</span>
</div>
<div class="menu-section-title">Information</div>
<div class="menu-link" onclick="showScreen('news');toggleMenu();">
<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M19 20H5a2 2 0 01-2-2V6a2 2 0 012-2h10a2 2 0 012 2v1m2 13a2 2 0 01-2-2V7m2 13a2 2 0 002-2V9a2 2 0 00-2-2h-2m-4-3H9M7 16h6M7 8h6v4H7V8z"/></svg>
<span>News</span>
</div>
<div class="menu-link" onclick="showScreen('calendar');toggleMenu();">
<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"/></svg>
<span>Economic Calendar</span>
<div class="right"><span class="ads-badge">Live</span></div>
</div>
<div class="menu-link" onclick="showScreen('signals');toggleMenu();">
<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
<span>AI Signals</span>
<div class="right"><div class="menu-badge" style="background:var(--warn);" id="signalBadge">3</div></div>
</div>
<div class="menu-section-title">System</div>
<div class="menu-link" onclick="showScreen('settings');toggleMenu();">
<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg>
<span>Settings</span>
</div>
<div class="menu-link" onclick="toggleMenu();toast('Journal: 12 entries');">
<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
<span>Journal</span>
</div>
<div class="menu-link" onclick="toggleMenu();toast('MetaNex AI Pro v3.1.0');">
<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4m0-4h.01"/></svg>
<span>About</span>
</div>
</div>
<div class="menu-footer">
<div class="menu-status">
<div class="status-dot"></div>
<span>Cloud AI Connected • Last sync: now</span>
</div>
</div>
</div>

<!-- SCREEN: BROKERS -->
<div class="screen active" id="screen-brokers">
<div class="header">
<div class="header-left"><button class="icon-btn" onclick="history.back()">&#8592;</button><div class="header-title">Brokers</div></div>
<div class="header-right"><button class="icon-btn">&#9776;</button></div>
</div>
<div class="search-box"><span style="color:var(--text3);font-size:18px;">&#128269;</span><input type="text" placeholder="Find broker" onfocus="toast('Search brokers...')"></div>
<div class="content">
<div class="broker-card" onclick="showScreen('login')">
<div class="broker-logo" style="background:linear-gradient(135deg,#667eea,#764ba2);">M</div>
<div class="broker-info"><div class="broker-name">MetaQuotes Ltd.</div><div class="broker-meta">MetaQuotes</div></div>
<span style="color:var(--text3);font-size:20px;">&#8250;</span>
</div>
<div class="broker-card" onclick="showScreen('login')">
<div class="broker-logo" style="background:#ffcc00;color:#000;">E</div>
<div class="broker-info"><div class="broker-name">Exness Technologies Ltd</div><div class="broker-meta">Exness</div></div>
<span style="color:var(--text3);font-size:20px;">&#8250;</span>
</div>
<div class="broker-card" onclick="showScreen('login')">
<div class="broker-logo" style="background:linear-gradient(135deg,#0a84ff,#0066cc);">I</div>
<div class="broker-info"><div class="broker-name">IC Markets Pty Ltd</div><div class="broker-meta">IC Markets</div></div>
<span style="color:var(--text3);font-size:20px;">&#8250;</span>
</div>
<div style="text-align:center;margin-top:50px;color:var(--text3);padding:0 24px;">
<div style="font-size:48px;margin-bottom:12px;opacity:.2;">&#128270;</div>
<div style="font-size:15px;margin-bottom:8px;font-weight:600;">Use search to find a company</div>
<div style="font-size:12px;line-height:1.5;">The application may feature brokerage companies which may not be regulated in your country. Exercise caution and responsibility before opening an account.</div>
</div>
</div>
<div style="padding:16px;border-top:1px solid var(--border);text-align:center;font-weight:700;font-size:13px;cursor:pointer;color:var(--text2);" onclick="toast('Broker search activated')">CAN'T FIND YOUR BROKER?</div>
</div>

<!-- SCREEN: LOGIN -->
<div class="screen" id="screen-login">
<div class="header">
<div class="header-left"><button class="icon-btn" onclick="showScreen('brokers')">&#8592;</button><div class="header-title">MetaQuotes Ltd.</div></div>
</div>
<div class="content">
<div class="login-hero">
<div class="logo">&#9889;</div>
<h1>MetaNex AI Pro</h1>
<p>Institutional-grade auto-trading terminal</p>
</div>
<div class="broker-card" style="opacity:.7;margin-bottom:8px;">
<div class="broker-logo" style="background:linear-gradient(135deg,#667eea,#764ba2);">M</div>
<div class="broker-info"><div class="broker-name">Open a demo account</div><div style="font-size:13px;color:var(--text3);">To learn trading and test strategies</div></div>
<span style="color:var(--text3);">&#8250;</span>
</div>
<div class="broker-card" style="opacity:.7;margin-bottom:8px;">
<div class="broker-logo" style="background:linear-gradient(135deg,#0a84ff,#0066cc);">R</div>
<div class="broker-info"><div class="broker-name">Open a real account</div><div style="font-size:13px;color:var(--text3);">For live trading, KYC required</div></div>
<span style="color:var(--text3);">&#8250;</span>
</div>
<div class="divider">or</div>
<div style="text-align:center;padding:8px 0 16px;font-weight:700;font-size:15px;">Login to existing account</div>
<div class="login-form">
<div class="input-group"><label>Login</label><input type="text" value="436002224" id="loginInput"></div>
<div class="input-group"><label>Password</label><input type="password" value="password123" id="passwordInput"></div>
<div class="input-group"><label>Server</label><select><option>Exness-MT5Trial9</option><option>MetaQuotes-Demo</option><option>Exness-Real</option><option>ICMarkets-Live</option></select></div>
<div class="checkbox-row"><label>Save password</label><div class="check-box">&#10003;</div></div>
<div class="link-text">Forgot password?</div>
<button class="btn-primary" onclick="doLogin()">LOGIN</button>
<button class="btn-secondary" onclick="showScreen('brokers')">Back to Brokers</button>
</div>
</div>
</div>

<!-- SCREEN: MAIN APP -->
<div class="screen" id="screen-main">

<!-- QUOTES TAB -->
<div class="tab-content active" id="tab-quotes">
<div class="header">
<div class="header-left"><button class="icon-btn" onclick="toggleMenu()">&#9776;</button><div class="header-title">Quotes</div></div>
<div class="header-right"><button class="icon-btn" onclick="showScreen('addsymbol')">&#43;</button><button class="icon-btn">&#9998;</button></div>
</div>
<div class="content" id="quotesContent"></div>
</div>

<!-- CHARTS TAB -->
<div class="tab-content" id="tab-charts">
<div class="header">
<div class="header-left"><button class="icon-btn" onclick="toggleMenu()">&#9776;</button><div class="header-title" id="chartHeaderTitle">Charts</div></div>
<div class="header-right"><button class="icon-btn">&#43;</button><button class="icon-btn">&#x270E;</button><button class="icon-btn" onclick="toggleChartSidebar()">&#x2630;</button></div>
</div>
<div class="chart-topbar">
<div style="display:flex;align-items:center;gap:8px;">
<span class="chart-symbol" id="chartSymbol" onclick="toggleChartSidebar()">BCHUSDm &#9662;</span>
<span class="chart-time" onclick="showTimeframeModal()">M5</span>
</div>
<div style="font-size:13px;color:var(--text2);display:flex;align-items:center;gap:6px;" id="marketStatus"><span class="status-dot" style="position:static;animation:none;width:8px;height:8px;"></span>Market open</div>
</div>
<div class="chart-container">
<div class="chart-sidebar" id="chartSidebar">
<div class="sym-list-item active" onclick="selectChartSymbol('BCHUSDm',this)"><span>BCHUSDm</span><span class="sym-status"></span></div>
<div class="sym-list-item" onclick="selectChartSymbol('BTCJPYm',this)"><span>BTCJPYm</span><span class="sym-status"></span></div>
<div class="sym-list-item" onclick="selectChartSymbol('BTCKRWm',this)"><span>BTCKRWm</span><span class="sym-status"></span></div>
<div class="sym-list-item" onclick="selectChartSymbol('BTCUSDm',this)"><span>BTCUSDm</span><span class="sym-status"></span></div>
<div class="sym-list-item" onclick="selectChartSymbol('ETHUSDm',this)"><span>ETHUSDm</span><span class="sym-status"></span></div>
<div class="sym-list-item" onclick="selectChartSymbol('LTCUSDm',this)"><span>LTCUSDm</span><span class="sym-status"></span></div>
<div class="sym-list-item" onclick="selectChartSymbol('XRPUSDm',this)"><span>XRPUSDm</span><span class="sym-status"></span></div>
<div class="sym-list-item" onclick="selectChartSymbol('EURUSDm',this)"><span>EURUSDm</span><span class="sym-status"></span></div>
<div class="sym-list-item" onclick="selectChartSymbol('USDJPYm',this)"><span>USDJPYm</span><span class="sym-status"></span></div>
<div class="sym-list-item" onclick="selectChartSymbol('GBPUSDm',this)"><span>GBPUSDm</span><span class="sym-status"></span></div>
<div class="sym-list-item" onclick="selectChartSymbol('AUDUSDm',this)"><span>AUDUSDm</span><span class="sym-status"></span></div>
<div class="sym-list-item" onclick="selectChartSymbol('USDCADm',this)"><span>USDCADm</span><span class="sym-status"></span></div>
</div>
<div class="chart-overlay-btn" onclick="toggleChartSidebar()">&#8250;</div>
<div class="chart-info-panel" id="chartInfoPanel">
<div class="chart-info-row"><span>O</span><span class="value" id="ciOpen">--</span><span>H</span><span class="value" id="ciHigh">--</span></div>
<div class="chart-info-row"><span>L</span><span class="value" id="ciLow">--</span><span>C</span><span class="value" id="ciClose">--</span></div>
</div>
<canvas id="candleCanvas"></canvas>
<div class="chart-tools">
<div class="tool-btn" onclick="addTrendLine()" title="Trend Line">&#128200;</div>
<div class="tool-btn" onclick="showIndicatorsModal()" title="Indicators">&#9881;</div>
<div class="tool-btn" onclick="showTimeframeModal()" title="Timeframe">&#9201;</div>
<div class="tool-btn" onclick="toggleCrosshair()" title="Crosshair">&#10010;</div>
</div>
</div>
</div>

<!-- TRADE TAB -->
<div class="tab-content" id="tab-trade">
<div class="header">
<div class="header-left"><button class="icon-btn" onclick="toggleMenu()">&#9776;</button><div class="header-title">Trade</div></div>
<div class="header-right"><button class="icon-btn" onclick="showSortModal()">&#8693;</button><button class="icon-btn" onclick="showScreen('addsymbol')">&#128196;</button></div>
</div>
<div class="content">
<div class="trade-stats">
<div class="stat-row"><span class="stat-label">Balance</span><span class="stat-dots"></span><span class="stat-value" id="balanceVal">$10,000.00</span></div>
<div class="stat-row"><span class="stat-label">Equity</span><span class="stat-dots"></span><span class="stat-value" id="equityVal">$10,000.00</span></div>
<div class="stat-row"><span class="stat-label">Free Margin</span><span class="stat-dots"></span><span class="stat-value" id="marginVal">$10,000.00</span></div>
<div class="stat-row"><span class="stat-label">Margin Level</span><span class="stat-dots"></span><span class="stat-value" id="marginLevel">100%</span></div>
</div>
<div class="ai-status-bar" id="aiStatusBar">
<div class="pulse"></div>
<span><strong>AI Bot:</strong> <span id="aiStatusText">Standby</span> • <span id="aiPairsText">0</span> pairs active</span>
</div>
<div class="positions-header">Positions <span id="posCount" style="color:var(--text3);">(0)</span></div>
<div id="positionsList"></div>
<div class="trade-actions">
<button class="trade-btn buy" onclick="manualTrade('BUY')">
<span>BUY</span>
<span class="sub" id="buyPrice">--</span>
</button>
<button class="trade-btn sell" onclick="manualTrade('SELL')">
<span>SELL</span>
<span class="sub" id="sellPrice">--</span>
</button>
</div>
</div>
</div>

<!-- HISTORY TAB -->
<div class="tab-content" id="tab-history">
<div class="header">
<div class="header-left"><button class="icon-btn" onclick="toggleMenu()">&#9776;</button><div class="header-title">History</div></div>
<div class="header-right"><button class="icon-btn">&#128260;</button><button class="icon-btn">&#8693;</button><button class="icon-btn">&#128197;</button></div>
</div>
<div class="content">
<div class="hist-tabs">
<div class="hist-tab active" onclick="switchHistTab('positions',this)">Positions</div>
<div class="hist-tab" onclick="switchHistTab('orders',this)">Orders</div>
<div class="hist-tab" onclick="switchHistTab('deals',this)">Deals</div>
</div>
<div id="histContent"></div>
</div>
</div>

<!-- AI AGENT TAB -->
<div class="tab-content" id="tab-ai">
<div class="header">
<div class="header-left"><button class="icon-btn" onclick="toggleMenu()">&#9776;</button><div class="header-title">AI Agent</div></div>
<div class="header-right"><button class="icon-btn" onclick="clearChat()">&#128465;</button></div>
</div>
<div class="chat-container">
<div class="chat-bg"></div>
<div class="chat-messages" id="chatMessages">
<div class="ai-welcome animate-fade">
<h2>&#129302; MetaNex AI</h2>
<p>Your 24/7 institutional trading co-pilot. I monitor markets, execute trades, and protect your capital even when your device is offline.</p>
</div>
</div>
<div class="quick-chips" id="quickChips">
<div class="quick-chip" onclick="sendQuick('Start auto trading')">&#9654; Start Bot</div>
<div class="quick-chip" onclick="sendQuick('Show account status')">&#128200; Status</div>
<div class="quick-chip" onclick="sendQuick('Analyze EURUSDm')">&#128269; Analyze</div>
<div class="quick-chip" onclick="sendQuick('Show active signals')">&#9889; Signals</div>
</div>
<div class="chat-input-area">
<textarea class="chat-input" id="chatInput" rows="1" placeholder="Command the AI..." onkeypress="handleChatKey(event)"></textarea>
<button class="send-btn" onclick="sendChat()">&#9654;</button>
</div>
</div>
</div>

<!-- BOTTOM NAV -->
<div class="bottom-nav">
<div class="nav-item active" onclick="switchTab('quotes')" data-tab="quotes">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M7 16V4m0 0L3 8m4-4l4 4m6 12V8m0 0l-4 4m4-4l4 4"/></svg>
<span>Quotes</span>
</div>
<div class="nav-item" onclick="switchTab('charts')" data-tab="charts">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>
<span>Charts</span>
</div>
<div class="nav-item" onclick="switchTab('trade')" data-tab="trade">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"/></svg>
<span>Trade</span>
</div>
<div class="nav-item" onclick="switchTab('history')" data-tab="history">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
<span>History</span>
</div>
<div class="nav-item" onclick="switchTab('ai')" data-tab="ai">
<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"/></svg>
<span>AI Agent</span>
<div class="nav-badge" id="aiNavBadge" style="display:none;">AI</div>
</div>
</div>
</div>

<!-- SCREEN: NEWS -->
<div class="screen" id="screen-news">
<div class="header">
<div class="header-left"><button class="icon-btn" onclick="showScreen('main');switchTab('quotes')">&#8592;</button><div class="header-title">News</div></div>
<div class="header-right"><button class="icon-btn">&#128260;</button></div>
</div>
<div class="content">
<div class="news-item animate-slide">
<div class="news-time">17:30 UTC</div>
<div class="news-title">Fed Chair Signals Potential Rate Pause in July</div>
<div class="news-desc">Federal Reserve officials hinted at a possible pause in the tightening cycle, sending the US Dollar lower against major counterparts.</div>
<div class="news-tag">USD</div>
</div>
<div class="news-item animate-slide" style="animation-delay:.1s;">
<div class="news-time">16:45 UTC</div>
<div class="news-title">Bitcoin ETF Inflows Reach $2.4B This Week</div>
<div class="news-desc">Institutional demand for spot Bitcoin ETFs continues to surge, pushing BTC above key resistance at $68,000.</div>
<div class="news-tag">Crypto</div>
</div>
<div class="news-item animate-slide" style="animation-delay:.2s;">
<div class="news-time">15:20 UTC</div>
<div class="news-title">ECB Maintains Rates, Euro Steady</div>
<div class="news-desc">The European Central Bank kept interest rates unchanged as expected, with President Lagarde emphasizing data-dependent future moves.</div>
<div class="news-tag">EUR</div>
</div>
<div class="news-item animate-slide" style="animation-delay:.3s;">
<div class="news-time">14:00 UTC</div>
<div class="news-title">AI Bot Detected Breakout on GBPJPY</div>
<div class="news-desc">MetaNex AI identified a bullish engulfing pattern on the 1H chart, triggering automated long positions across 847 user accounts.</div>
<div class="news-tag" style="background:rgba(10,132,255,.15);color:var(--accent);">AI Signal</div>
</div>
</div>
</div>

<!-- SCREEN: CALENDAR -->
<div class="screen" id="screen-calendar">
<div class="header">
<div class="header-left"><button class="icon-btn" onclick="showScreen('main');switchTab('quotes')">&#8592;</button><div class="header-title">Economic Calendar</div></div>
</div>
<div class="content">
<div class="cal-item">
<div class="cal-time"><div class="hour">18:00</div><div class="min">UTC</div></div>
<div class="cal-flag">&#127482;&#127480;</div>
<div class="cal-info"><div class="cal-event">ISM Manufacturing PMI</div><div class="cal-forecast">Forecast: 48.5 | Previous: 48.7</div></div>
<div class="cal-impact high">HIGH</div>
</div>
<div class="cal-item">
<div class="cal-time"><div class="hour">14:30</div><div class="min">UTC</div></div>
<div class="cal-flag">&#127467;&#127479;</div>
<div class="cal-info"><div class="cal-event">French CPI m/m</div><div class="cal-forecast">Forecast: 0.2% | Previous: 0.1%</div></div>
<div class="cal-impact medium">MED</div>
</div>
<div class="cal-item">
<div class="cal-time"><div class="hour">09:30</div><div class="min">UTC</div></div>
<div class="cal-flag">&#127471;&#127477;</div>
<div class="cal-info"><div class="cal-event">Tokyo Core CPI y/y</div><div class="cal-forecast">Forecast: 2.1% | Previous: 2.2%</div></div>
<div class="cal-impact low">LOW</div>
</div>
<div class="cal-item">
<div class="cal-time"><div class="hour">Tomorrow</div><div class="min">08:00</div></div>
<div class="cal-flag">&#127468;&#127463;</div>
<div class="cal-info"><div class="cal-event">BoE Interest Rate Decision</div><div class="cal-forecast">Forecast: 5.25% | Previous: 5.25%</div></div>
<div class="cal-impact high">HIGH</div>
</div>
</div>
</div>

<!-- SCREEN: SIGNALS -->
<div class="screen" id="screen-signals">
<div class="header">
<div class="header-left"><button class="icon-btn" onclick="showScreen('main');switchTab('quotes')">&#8592;</button><div class="header-title">AI Signals</div></div>
<div class="header-right"><button class="icon-btn" onclick="refreshSignals()">&#128260;</button></div>
</div>
<div class="content" id="signalsContent">
<div class="signal-card">
<div class="signal-header"><span class="signal-pair">EURUSDm</span><span class="signal-badge buy">BUY</span></div>
<div class="signal-row"><span class="signal-label">Entry Price</span><span class="signal-value">1.08520</span></div>
<div class="signal-row"><span class="signal-label">Take Profit</span><span class="signal-value signal-tp">1.09200 (+68 pips)</span></div>
<div class="signal-row"><span class="signal-label">Stop Loss</span><span class="signal-value signal-sl">1.08050 (-47 pips)</span></div>
<div class="signal-row"><span class="signal-label">Risk/Reward</span><span class="signal-value">1:1.45</span></div>
<div class="signal-confidence"><div class="signal-confidence-bar" style="width:87%;"></div></div>
<div class="signal-conf-text">AI Confidence: 87% • Pattern: Bullish Engulfing</div>
</div>
<div class="signal-card">
<div class="signal-header"><span class="signal-pair">GBPJPYm</span><span class="signal-badge sell">SELL</span></div>
<div class="signal-row"><span class="signal-label">Entry Price</span><span class="signal-value">192.450</span></div>
<div class="signal-row"><span class="signal-label">Take Profit</span><span class="signal-value signal-tp">191.200 (+125 pips)</span></div>
<div class="signal-row"><span class="signal-label">Stop Loss</span><span class="signal-value signal-sl">193.100 (-65 pips)</span></div>
<div class="signal-row"><span class="signal-label">Risk/Reward</span><span class="signal-value">1:1.92</span></div>
<div class="signal-confidence"><div class="signal-confidence-bar" style="width:92%;"></div></div>
<div class="signal-conf-text">AI Confidence: 92% • Pattern: Head and Shoulders</div>
</div>
<div class="signal-card">
<div class="signal-header"><span class="signal-pair">BTCUSDm</span><span class="signal-badge buy">BUY</span></div>
<div class="signal-row"><span class="signal-label">Entry Price</span><span class="signal-value">68,420.00</span></div>
<div class="signal-row"><span class="signal-label">Take Profit</span><span class="signal-value signal-tp">71,500.00 (+3,080)</span></div>
<div class="signal-row"><span class="signal-label">Stop Loss</span><span class="signal-value signal-sl">66,800.00 (-1,620)</span></div>
<div class="signal-row"><span class="signal-label">Risk/Reward</span><span class="signal-value">1:1.90</span></div>
<div class="signal-confidence"><div class="signal-confidence-bar" style="width:79%;"></div></div>
<div class="signal-conf-text">AI Confidence: 79% • Pattern: Ascending Triangle</div>
</div>
</div>
</div>

<!-- SCREEN: SETTINGS -->
<div class="screen" id="screen-settings">
<div class="header">
<div class="header-left"><button class="icon-btn" onclick="showScreen('main');switchTab('quotes')">&#8592;</button><div class="header-title">Settings</div></div>
</div>
<div class="content">
<div class="settings-group">
<div class="settings-header">AI Trading</div>
<div class="settings-row" onclick="toggleSetting(this,'aiEnabled')">
<div class="settings-row-left">
<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
<div><div class="settings-row-title">Auto-Trading</div><div class="settings-row-desc">Allow AI to trade automatically</div></div>
</div>
<div class="settings-row-value"><div class="toggle-switch on" id="sw-aiEnabled"></div></div>
</div>
<div class="settings-row" onclick="toggleSetting(this,'aiProtect')">
<div class="settings-row-left">
<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/></svg>
<div><div class="settings-row-title">Capital Protection</div><div class="settings-row-desc">Auto-close on market reversal</div></div>
</div>
<div class="settings-row-value"><div class="toggle-switch on" id="sw-aiProtect"></div></div>
</div>
<div class="settings-row" onclick="showModal('Risk Per Trade','1%','2%','5%','10%')">
<div class="settings-row-left">
<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
<div><div class="settings-row-title">Risk Per Trade</div><div class="settings-row-desc">Maximum exposure per signal</div></div>
</div>
<div class="settings-row-value">1% &#8250;</div>
</div>
</div>
<div class="settings-group">
<div class="settings-header">Interface</div>
<div class="settings-row" onclick="toggleSetting(this,'darkMode')">
<div class="settings-row-left">
<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"/></svg>
<div><div class="settings-row-title">Dark Mode</div></div>
</div>
<div class="settings-row-value"><div class="toggle-switch on" id="sw-darkMode"></div></div>
</div>
<div class="settings-row" onclick="showModal('Chart Style','Candles','Bars','Line','Heikin Ashi')">
<div class="settings-row-left">
<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M7 12l3-3 3 3 4-4M8 21l4-4 4 4M3 4h18M4 4h16v12a1 1 0 01-1 1H5a1 1 0 01-1-1V4z"/></svg>
<div><div class="settings-row-title">Chart Style</div></div>
</div>
<div class="settings-row-value">Candles &#8250;</div>
</div>
</div>
<div class="settings-group">
<div class="settings-header">Notifications</div>
<div class="settings-row" onclick="toggleSetting(this,'notifTrade')">
<div class="settings-row-left">
<svg fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path d="M15 17h5l-1.405-1.405A2.032 2.032 0 0118 14.158V11a6.002 6.002 0 00-4-5.659V5a2 2 0 10-4 0v.341C7.67 6.165 6 8.388 6 11v3.159c0 .538-.214 1.055-.595 1.436L4 17h5m6 0v1a3 3 0 11-6 0v-1m6 0H9"/></svg>
<div><div class="settings-row-title">Trade Alerts</div></div>
</div>
<div class="settings-row-value"><div class="toggle-switch on" id="sw-notifTrade"></div></div>
</div>
</div>
</div>
</div>

<!-- SCREEN: ADD SYMBOL -->
<div class="screen" id="screen-addsymbol">
<div class="header">
<div class="header-left"><button class="icon-btn" onclick="showScreen('main')">&#8592;</button><div class="header-title">Add Symbol</div></div>
</div>
<div class="search-box"><span style="color:var(--text3);font-size:18px;">&#128269;</span><input type="text" placeholder="Find symbols" id="symbolSearch" oninput="filterSymbols(this.value)"></div>
<div class="content">
<div class="folder-item" onclick="toast('Standard folder: 351 symbols')">
<div class="folder-left"><div class="folder-icon">&#128194;</div><span class="folder-name">Standard</span></div>
<span class="folder-count">4/351</span>
</div>
<div class="folder-item" onclick="toast('Crypto folder opened')">
<div class="folder-left"><div class="folder-icon" style="background:linear-gradient(135deg,#f7931a,#ffd60a);">&#8383;</div><span class="folder-name">Cryptocurrencies</span></div>
<span class="folder-count">12/48</span>
</div>
<div class="folder-item" onclick="toast('Forex folder opened')">
<div class="folder-left"><div class="folder-icon" style="background:linear-gradient(135deg,#0a84ff,#5e5ce6);">&#36;</div><span class="folder-name">Forex Majors</span></div>
<span class="folder-count">4/28</span>
</div>
<div id="symbolList" style="padding:8px 16px;"></div>
</div>
</div>

<script>
// ================= STATE =================
const state={
balance:100000,equity:100000,margin:100000,marginLevel:100,
positions:[],orders:[],deals:[],
aiActive:false,aiProtection:true,riskPerTrade:0.01,
currentSymbol:'BCHUSDm',timeframe:'M5',chartStyle:'candles',
candles:[],trendLines:[],crosshair:false,
settings:{aiEnabled:true,aiProtect:true,darkMode:true,notifTrade:true},
signals:[
{pair:'EURUSDm',type:'BUY',entry:1.08520,tp:1.09200,sl:1.08050,conf:87,rr:'1:1.45',pattern:'Bullish Engulfing'},
{pair:'GBPJPYm',type:'SELL',entry:192.450,tp:191.200,sl:193.100,conf:92,rr:'1:1.92',pattern:'Head and Shoulders'},
{pair:'BTCUSDm',type:'BUY',entry:68420,tp:71500,sl:66800,conf:79,rr:'1:1.90',pattern:'Ascending Triangle'}
]
};

const symbols=[
{pair:'EURUSDm',bid:1.08501,ask:1.08521,spread:20,digits:5,base:1.08},
{pair:'USDJPYm',bid:156.342,ask:156.362,spread:20,digits:3,base:156},
{pair:'GBPJPYm',bid:192.445,ask:192.465,spread:20,digits:3,base:192},
{pair:'GBPUSDm',bid:1.27451,ask:1.27471,spread:20,digits:5,base:1.27},
{pair:'AUDUSDm',bid:0.66421,ask:0.66441,spread:20,digits:5,base:0.66},
{pair:'USDCADm',bid:1.36251,ask:1.36271,spread:20,digits:5,base:1.36},
{pair:'BCHUSDm',bid:298.50,ask:298.84,spread:34,digits:2,base:300},
{pair:'BTCUSDm',bid:68421.50,ask:68460.20,spread:387,digits:2,base:68500},
{pair:'ETHUSDm',bid:3521.45,ask:3523.80,spread:235,digits:2,base:3520},
{pair:'XRPUSDm',bid:0.5423,ask:0.5431,spread:8,digits:4,base:0.54},
{pair:'LTCUSDm',bid:78.42,ask:78.58,spread:16,digits:2,base:78},
{pair:'SOLUSDm',bid:142.35,ask:142.65,spread:30,digits:2,base:142}
];

const allSymbols=['AUDCADm','AUDCHFm','AUDJPYm','AUDNZDm','AUDUSDm','CADCHFm','CADJPYm','CHFJPYm','EURAUDm','EURCADm','EURCHFm','EURGBPm','EURJPYm','EURNZDm','EURUSDm','GBPAUDm','GBPCADm','GBPCHFm','GBPJPYm','GBPNZDm','GBPUSDm','NZDCADm','NZDCHFm','NZDJPYm','NZDUSDm','USDCADm','USDCHFm','USDJPYm','BTCUSDm','ETHUSDm','LTCUSDm','XRPUSDm','BCHUSDm','SOLUSDm','DOTUSDm','ADAUSDm'];

// ================= UTILS =================
function toast(msg){const t=document.getElementById('toast');t.textContent=msg;t.classList.add('show');setTimeout(()=>t.classList.remove('show'),2800);}
function showScreen(id){document.querySelectorAll('.screen').forEach(s=>s.classList.remove('active'));document.getElementById('screen-'+id).classList.add('active');if(id==='main'){switchTab('quotes');}}
function switchTab(tab){document.querySelectorAll('.tab-content').forEach(t=>t.classList.remove('active'));document.getElementById('tab-'+tab).classList.add('active');document.querySelectorAll('.nav-item').forEach(n=>n.classList.remove('active'));document.querySelector(`.nav-item[data-tab="${tab}"]`).classList.add('active');if(tab==='charts'){setTimeout(resizeCanvas,50);}}
function toggleMenu(){document.getElementById('menuOverlay').classList.toggle('open');document.getElementById('sideMenu').classList.toggle('open');}
function doLogin(){toast('Authenticating...');setTimeout(()=>{showScreen('main');toast('Connected to Exness-MT5Trial9');initAI();},900);}

// ================= MODAL =================
function showModal(title,...options){const overlay=document.getElementById('modalOverlay');const sheet=document.getElementById('modalSheet');sheet.innerHTML=`<div class="modal-header"><div class="modal-title">${title}</div><button class="modal-close" onclick="closeModal()">&times;</button></div>`+options.map(o=>`<div class="modal-row" onclick="closeModal();toast('${title}: ${o}')"><span>${o}</span></div>`).join('');overlay.classList.add('open');}
function closeModal(){document.getElementById('modalOverlay').classList.remove('open');}
function showTimeframeModal(){showModal('Timeframe','M1','M5','M15','M30','H1','H4','D1','W1','MN');}
function showIndicatorsModal(){showModal('Indicators','Moving Average','Bollinger Bands','RSI','MACD','Fibonacci','Ichimoku','Volume');}
function showSortModal(){showModal('Sort By','Newest','Symbol','Profit','Volume');}

// ================= SETTINGS =================
function toggleSetting(row,key){const sw=row.querySelector('.toggle-switch');sw.classList.toggle('on');state.settings[key]=sw.classList.contains('on');if(key==='aiEnabled'){state.aiActive=state.settings.aiEnabled;if(state.aiActive){startAIBot();toast('AI Auto-Trading ENABLED');}else{toast('AI Auto-Trading DISABLED');}}updateAIStatus();}

// ================= QUOTES =================
function renderQuotes(){const c=document.getElementById('quotesContent');c.innerHTML=symbols.map((s,i)=>{const change=(Math.random()*180-60).toFixed(0);const pct=(change/s.bid*100).toFixed(2);const isUp=change>=0;const now=new Date();const timeStr=now.toTimeString().slice(0,8);const bidStr=s.bid.toFixed(s.digits);const askStr=s.ask.toFixed(s.digits);const bidMain=bidStr.slice(0,-1);const bidExt=bidStr.slice(-1);const askMain=askStr.slice(0,-1);const askExt=askStr.slice(-1);return`<div class="quote-item ${s.pair===state.currentSymbol?'active':''}" onclick="openChart('${s.pair}')">
<div class="quote-left"><div class="quote-pair">${s.pair}</div><div class="quote-meta"><span class="quote-time">${timeStr}</span><span class="quote-spread">${s.spread}</span></div><div class="quote-change ${isUp?'up':'down'}">${isUp?'+':''}${change} <span class="price-arrow">${isUp?'&#9650;':'&#9660;'}</span> ${isUp?'+':''}${pct}%</div></div>
<div class="quote-prices"><div class="price-row"><span class="price-bid">${bidMain}<sup>${bidExt}</sup></span><span class="price-ask">${askMain}<sup>${askExt}</sup></span></div><div class="price-ext">L: ${(s.bid*0.998).toFixed(s.digits)} &nbsp; H: ${(s.bid*1.002).toFixed(s.digits)}</div></div>
</div>`;}).join('');}
function openChart(pair){state.currentSymbol=pair;document.getElementById('chartSymbol').innerHTML=pair+' &#9662;';initCandles(pair);switchTab('charts');}

// ================= CHART =================
const canvas=document.getElementById('candleCanvas');const ctx=canvas.getContext('2d');
function resizeCanvas(){const rect=canvas.parentElement.getBoundingClientRect();canvas.width=rect.width*window.devicePixelRatio;canvas.height=rect.height*window.devicePixelRatio;ctx.scale(window.devicePixelRatio,window.devicePixelRatio);canvas.style.width=rect.width+'px';canvas.style.height=rect.height+'px';drawChart();}
function initCandles(symbol){const base=symbols.find(s=>s.pair===symbol)?.base||300;state.candles=[];let price=base;const now=Date.now();for(let i=0;i<70;i++){const open=price;const change=(Math.random()-.5)*base*.012;price+=change;const high=Math.max(open,price)+Math.random()*base*.004;const low=Math.min(open,price)-Math.random()*base*.004;state.candles.push({open,high,low,close:price,time:now-(70-i)*300000,isUp:price>=open});}}
function drawChart(){const w=canvas.width/window.devicePixelRatio;const h=canvas.height/window.devicePixelRatio;ctx.clearRect(0,0,w,h);const pad=50;const chartW=w-pad-10;const chartH=h-pad-20;const spacing=chartW/state.candles.length;const candleW=Math.max(3,spacing*.65);let min=Infinity,max=-Infinity;state.candles.forEach(c=>{if(c.low<min)min=c.low;if(c.high>max)max=c.high;});const range=max-min||1;const y=p=>chartH-((p-min)/range)*chartH+10;const x=i=>i*spacing+spacing/2+pad;ctx.strokeStyle='#1a1a1a';ctx.lineWidth=1;for(let i=0;i<=6;i++){const gy=10+(chartH/6)*i;ctx.beginPath();ctx.moveTo(pad,gy);ctx.lineTo(w-10,gy);ctx.stroke();const label=(max-(range/6)*i).toFixed(2);ctx.fillStyle='#555';ctx.font='11px sans-serif';ctx.fillText(label,4,gy+3);}for(let i=0;i<state.candles.length;i+=12){const gx=x(i);ctx.beginPath();ctx.moveTo(gx,10);ctx.lineTo(gx,chartH+10);ctx.stroke();}state.candles.forEach((c,i)=>{const cx=x(i);const o=y(c.open);const cl=y(c.close);const hi=y(c.high);const lo=y(c.low);const color=c.isUp?'#30d158':'#ff453a';ctx.strokeStyle=color;ctx.fillStyle=color;ctx.lineWidth=1.5;ctx.beginPath();ctx.moveTo(cx,hi);ctx.lineTo(cx,lo);ctx.stroke();const bodyTop=Math.min(o,cl);const bodyH=Math.max(1,Math.abs(o-cl));ctx.fillRect(cx-candleW/2,bodyTop,candleW,bodyH);});const last=state.candles[state.candles.length-1];if(last){const ly=y(last.close);ctx.strokeStyle='#0a84ff';ctx.setLineDash([5,5]);ctx.lineWidth=1;ctx.beginPath();ctx.moveTo(pad,ly);ctx.lineTo(w-10,ly);ctx.stroke();ctx.setLineDash([]);ctx.fillStyle='#0a84ff';ctx.font='bold 12px sans-serif';ctx.fillText(last.close.toFixed(2),w-60,ly-6);document.getElementById('ciOpen').textContent=last.open.toFixed(2);document.getElementById('ciHigh').textContent=last.high.toFixed(2);document.getElementById('ciLow').textContent=last.low.toFixed(2);document.getElementById('ciClose').textContent=last.close.toFixed(2);const row=document.querySelector('.chart-info-row:last-child');if(last.close>=last.open){row.classList.add('up');row.classList.remove('down');}else{row.classList.add('down');row.classList.remove('up');}}state.trendLines.forEach(tl=>{ctx.strokeStyle='#ff453a';ctx.lineWidth=2.5;ctx.beginPath();ctx.moveTo(x(tl.i1),y(tl.p1));ctx.lineTo(x(tl.i2),y(tl.p2));ctx.stroke();const ax=x(tl.i2),ay=y(tl.p2);ctx.fillStyle='#ff453a';ctx.beginPath();ctx.moveTo(ax,ay);ctx.lineTo(ax-8,ay-8);ctx.lineTo(ax+8,ay-8);ctx.fill();});ctx.fillStyle='#666';ctx.font='10px sans-serif';for(let i=0;i<5;i++){const idx=Math.floor((state.candles.length/5)*i);const t=new Date(state.candles[idx].time);const label=t.getHours()+':'+String(t.getMinutes()).padStart(2,'0');ctx.fillText(label,x(idx)-18,h-6);}}
function updateChart(){if(!state.candles.length)return;const last=state.candles[state.candles.length-1];const change=(Math.random()-.5)*last.close*.002;last.close+=change;if(last.close>last.high)last.high=last.close;if(last.close<last.low)last.low=last.close;last.isUp=last.close>=last.open;if(Date.now()-last.time>4000){const newOpen=last.close;state.candles.push({open:newOpen,high:newOpen,low:newOpen,close:newOpen,time:Date.now(),isUp:true});if(state.candles.length>90)state.candles.shift();}drawChart();}
function toggleChartSidebar(){document.getElementById('chartSidebar').classList.toggle('open');}
function selectChartSymbol(sym,el){state.currentSymbol=sym;document.getElementById('chartSymbol').innerHTML=sym+' &#9662;';document.querySelectorAll('.sym-list-item').forEach(e=>e.classList.remove('active'));el.classList.add('active');document.getElementById('chartSidebar').classList.remove('open');initCandles(sym);drawChart();toast('Chart: '+sym);}
function addTrendLine(){if(state.candles.length<10)return;const i1=Math.floor(state.candles.length*.25);const i2=state.candles.length-4;state.trendLines.push({i1,i2,p1:state.candles[i1].low,p2:state.candles[i2].high});drawChart();toast('Trend line added');}
function toggleCrosshair(){state.crosshair=!state.crosshair;toast(state.crosshair?'Crosshair ON':'Crosshair OFF');}

// ================= TRADE / POSITIONS =================
function updateTradeStats(){let totalPL=0;state.positions.forEach(p=>{const sym=symbols.find(s=>s.pair===p.pair);if(sym){const current=p.type==='BUY'?sym.bid:sym.ask;const pl=(current-p.price)*(p.type==='BUY'?1:-1)*p.volume*100000;p.pl=pl;totalPL+=pl;}});state.equity=state.balance+totalPL;state.margin=state.equity;state.marginLevel=state.margin>0?(state.equity/state.margin*100).toFixed(0):0;document.getElementById('balanceVal').textContent='$'+state.balance.toLocaleString('en',{minimumFractionDigits:2});document.getElementById('equityVal').textContent='$'+state.equity.toLocaleString('en',{minimumFractionDigits:2});document.getElementById('marginVal').textContent='$'+state.margin.toLocaleString('en',{minimumFractionDigits:2});document.getElementById('marginLevel').textContent=state.marginLevel+'%';document.getElementById('posCount').textContent='('+state.positions.length+')';document.getElementById('aiPairsText').textContent=state.positions.length;const buySym=symbols.find(s=>s.pair===state.currentSymbol);if(buySym){document.getElementById('buyPrice').textContent=buySym.ask.toFixed(buySym.digits);document.getElementById('sellPrice').textContent=buySym.bid.toFixed(buySym.digits);}renderPositions();}
function renderPositions(){const list=document.getElementById('positionsList');if(!state.positions.length){list.innerHTML=`<div class="empty-state" style="height:260px;"><div class="empty-icon">&#128200;</div><div class="empty-title">No open positions</div><div class="empty-desc">AI Bot will open positions automatically when enabled</div></div>`;return;}list.innerHTML=state.positions.map(p=>{const isUp=p.pl>=0;return`<div class="position-item" onclick="closePositionPrompt(${p.id})">
<div class="pos-info"><div class="pos-pair">${p.pair} <span style="color:${p.type==='BUY'?'var(--up)':'var(--down)'}">${p.type}</span> ${p.volume.toFixed(2)}</div><div class="pos-detail">Open: ${p.price.toFixed(5)} • ${new Date(p.time).toLocaleTimeString([],{hour:'2-digit',minute:'2-digit'})}<br>TP: ${p.tp.toFixed(5)} | SL: ${p.sl.toFixed(5)}</div></div>
<div class="pos-pl ${isUp?'up':'down'}">${isUp?'+':''}$${p.pl.toFixed(2)}</div>
</div>`;}).join('');}
function openPosition(pair,type,volume,tp,sl){const sym=symbols.find(s=>s.pair===pair);if(!sym)return;const price=type==='BUY'?sym.ask:sym.bid;const pos={id:Date.now()+Math.random(),pair,type,volume,price,tp,sl,time:Date.now(),pl:0};state.positions.push(pos);updateTradeStats();addToHistory(pos);return pos;}
function closePosition(id){const idx=state.positions.findIndex(p=>p.id===id);if(idx===-1)return;const p=state.positions[idx];state.balance+=p.pl;state.positions.splice(idx,1);updateTradeStats();addDealToHistory(p,'CLOSED');return p.pl;}
function closePositionPrompt(id){const p=state.positions.find(x=>x.id===id);if(!p)return;const pl=closePosition(id);const emoji=pl>=0?'&#9989;':'&#10060;';toast(`${emoji} Closed ${p.pair} ${p.type} | P&L: $${pl.toFixed(2)}`);}
function manualTrade(type){const sym=symbols.find(s=>s.pair===state.currentSymbol);if(!sym)return;const price=type==='BUY'?sym.ask:sym.bid;const tp=price*(type==='BUY'?1.008:0.992);const sl=price*(type==='BUY'?0.995:1.005);const vol=0.1;openPosition(state.currentSymbol,type,vol,tp,sl);toast(`${type} ${vol} ${state.currentSymbol} @ ${price.toFixed(sym.digits)}`);}

// ================= HISTORY =================
function switchHistTab(tab,el){document.querySelectorAll('.hist-tab').forEach(t=>t.classList.remove('active'));el.classList.add('active');state.histTab=tab;renderHistory();}
function addToHistory(pos){state.deals.unshift({...pos,action:'OPEN',time:Date.now()});if(state.deals.length>60)state.deals.pop();}
function addDealToHistory(pos,action){state.deals.unshift({...pos,action,time:Date.now()});if(state.deals.length>60)state.deals.pop();}
function renderHistory(){const c=document.getElementById('histContent');if(state.histTab==='positions'){if(!state.positions.length){c.innerHTML=`<div class="empty-state"><div class="empty-icon">&#128230;</div><div>Empty history</div></div>`;return;}c.innerHTML=state.positions.map(p=>{const isUp=p.pl>=0;return`<div class="deal-item"><div class="deal-info"><div class="deal-pair">${p.pair} ${p.type} ${p.volume.toFixed(2)}</div><div class="deal-detail">Open: ${p.price.toFixed(5)} • ${new Date(p.time).toLocaleTimeString()}</div></div><div class="deal-pl ${isUp?'up':'down'}">${isUp?'+':''}$${p.pl.toFixed(2)}</div></div>`;}).join('');}else if(state.histTab==='orders'){c.innerHTML=`<div class="empty-state"><div class="empty-icon">&#128230;</div><div>No pending orders</div></div>`;}else{if(!state.deals.length){c.innerHTML=`<div class="empty-state"><div class="empty-icon">&#128230;</div><div>Empty history</div></div>`;return;}c.innerHTML=state.deals.slice(0,25).map(d=>{const isUp=(d.pl||0)>=0;return`<div class="deal-item"><div class="deal-info"><div class="deal-pair">${d.pair} ${d.type} ${d.volume.toFixed(2)} [${d.action}]</div><div class="deal-detail">${d.price.toFixed(5)} • ${new Date(d.time).toLocaleTimeString()}</div></div><div class="deal-pl ${isUp?'up':'down'}">${isUp?'+':''}$${(d.pl||0).toFixed(2)}</div></div>`;}).join('');}}

// ================= AI CHAT =================
function initAI(){setTimeout(()=>{addAIMessage('&#129302; MetaNex AI initialized. Cloud connection established. I will trade for you 24/7, even if your device is offline.');addAIMessage('Type <b>"start bot"</b> to activate auto-trading across 10+ pairs, or ask me anything.');},600);}
function addUserMessage(text){const div=document.createElement('div');div.className='msg-bubble user';div.innerHTML=text+`<div class="msg-time">${new Date().toLocaleTimeString([],{hour:'2-digit',minute:'2-digit'})}</div>`;document.getElementById('chatMessages').appendChild(div);scrollChat();}
function addAIMessage(text){const div=document.createElement('div');div.className='msg-bubble ai';div.innerHTML=text+`<div class="msg-time">${new Date().toLocaleTimeString([],{hour:'2-digit',minute:'2-digit'})}</div>`;document.getElementById('chatMessages').appendChild(div);scrollChat();}
function addSystemMessage(text){const div=document.createElement('div');div.className='msg-bubble system';div.textContent=text;document.getElementById('chatMessages').appendChild(div);scrollChat();}
function showTyping(){const div=document.createElement('div');div.className='msg-bubble ai typing-indicator';div.id='typing';div.innerHTML='<div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div>';document.getElementById('chatMessages').appendChild(div);scrollChat();}
function hideTyping(){const t=document.getElementById('typing');if(t)t.remove();}
function scrollChat(){const c=document.getElementById('chatMessages');c.scrollTop=c.scrollHeight;}
function handleChatKey(e){if(e.key==='Enter'&&!e.shiftKey){e.preventDefault();sendChat();}}
function sendQuick(text){document.getElementById('chatInput').value=text;sendChat();}
function sendChat(){const input=document.getElementById('chatInput');const text=input.value.trim();if(!text)return;addUserMessage(text);input.value='';processAICommand(text);}
function clearChat(){document.getElementById('chatMessages').innerHTML='';addSystemMessage('Chat history cleared');}

function processAICommand(text){
showTyping();const lower=text.toLowerCase();
setTimeout(()=>{hideTyping();
if(lower.includes('start')||lower.includes('activate')||lower.includes('run')){
state.aiActive=true;updateAIStatus();addAIMessage('&#9889; <b>AI BOT ACTIVATED</b><br>Mode: Aggressive Growth<br>Pairs: 12 active<br>Risk/Trade: 1%<br>Protection: ON<br><br>I will now scan and execute trades automatically. You can close the app — I trade from the cloud.');
addSystemMessage('Bot started at '+new Date().toLocaleTimeString());
}else if(lower.includes('stop')||lower.includes('halt')||lower.includes('pause')){
state.aiActive=false;updateAIStatus();addAIMessage('&#128721; <b>AI BOT PAUSED</b><br>All new entries halted. Existing positions remain managed by protective stops.');
}else if(lower.includes('status')||lower.includes('balance')||lower.includes('equity')||lower.includes('account')){
addAIMessage(`&#128200; <b>Account Dashboard</b><br>Balance: <b>$${state.balance.toLocaleString('en',{minimumFractionDigits:2})}</b><br>Equity: <b>$${state.equity.toLocaleString('en',{minimumFractionDigits:2})}</b><br>Open Positions: <b>${state.positions.length}</b><br>AI Status: <b>${state.aiActive?'&#9989; ACTIVE':'&#9208; IDLE'}</b><br>Cloud Uptime: <b>99.99%</b>`);
}else if(lower.includes('analyze')||lower.includes('predict')||lower.includes('forecast')){
const sym=symbols[Math.floor(Math.random()*symbols.length)].pair;
const trend=Math.random()>.5?'BULLISH':'BEARISH';
const conf=Math.floor(Math.random()*15+80);
const patterns=['Ascending Triangle','Bullish Engulfing','Double Bottom','Falling Wedge','Breakout Channel','Harmonic Bat'];
addAIMessage(`&#128200; <b>Technical Analysis: ${sym}</b><br>Trend: <span style="color:${trend==='BULLISH'?'var(--up)':'var(--down)'}">${trend}</span><br>Confidence: <b>${conf}%</b><br>Pattern: <b>${patterns[Math.floor(Math.random()*patterns.length)]}</b><br>Volume: <b>${Math.random()>.5?'Increasing':'Above average'}</b><br>Recommendation: <b>${trend==='BULLISH'?'LONG with tight SL':'SHORT on rejection'}</b>`);
}else if(lower.includes('signal')||lower.includes('tp')||lower.includes('sl')){
addAIMessage('&#9889; <b>Active AI Signals</b><br>1. <b>EURUSDm</b> BUY @ 1.08520 | TP: 1.09200 | SL: 1.08050 | Conf: 87%<br>2. <b>GBPJPYm</b> SELL @ 192.450 | TP: 191.200 | SL: 193.100 | Conf: 92%<br>3. <b>BTCUSDm</b> BUY @ 68,420 | TP: 71,500 | SL: 66,800 | Conf: 79%<br><br>Go to <b>AI Signals</b> in the menu for full details.');
}else if(lower.includes('close all')){
let total=0;[...state.positions].forEach(p=>{total+=closePosition(p.id);});
addAIMessage(`&#9989; <b>All positions closed</b><br>Total P&L: <b>$${total.toFixed(2)}</b><br>New Balance: <b>$${state.balance.toLocaleString('en',{minimumFractionDigits:2})}</b>`);
}else if(lower.includes('help')||lower.includes('command')){
addAIMessage('&#129302; <b>Available Commands</b><br>&bull; "start bot" — activate 24/7 auto-trading<br>&bull; "stop bot" — pause new entries<br>&bull; "status" — full account summary<br>&bull; "analyze" — AI market forecast<br>&bull; "signals" — view TP/SL recommendations<br>&bull; "close all" — emergency close all<br>&bull; Ask about any pair!');
}else{
addAIMessage('I understand. I\'m monitoring global markets across 12 timeframes. Try "help" for commands or "analyze" for a forecast. Your capital is protected.');
}
},700+Math.random()*500);
}

// ================= AI TRADING BOT =================
function updateAIStatus(){const bar=document.getElementById('aiStatusBar');const txt=document.getElementById('aiStatusText');const badge=document.getElementById('aiNavBadge');const menuBadge=document.getElementById('aiMenuBadge');if(state.aiActive){bar.style.background='linear-gradient(90deg,rgba(48,209,88,.15),rgba(10,132,255,.15))';txt.textContent='ACTIVE — Cloud Trading';txt.style.color='var(--up)';badge.style.display='flex';menuBadge.textContent='ON';menuBadge.style.background='var(--up)';}else{bar.style.background='linear-gradient(90deg,rgba(255,159,10,.15),rgba(255,69,58,.15))';txt.textContent='Standby';txt.style.color='var(--warn)';badge.style.display='none';menuBadge.textContent='OFF';menuBadge.style.background='var(--text3)';}}
function startAIBot(){updateAIStatus();}
function runTradingBot(){if(!state.aiActive)return;const activePairs=symbols.filter((_,i)=>i<10);activePairs.forEach(sym=>{if(Math.random()>.75)return;const type=Math.random()>.5?'BUY':'SELL';const volume=parseFloat((0.05+Math.random()*0.45).toFixed(2));const price=type==='BUY'?sym.ask:sym.bid;const tp=price*(type==='BUY'?1.01:0.99);const sl=price*(type==='BUY'?0.994:1.006);const pos=openPosition(sym.pair,type,volume,tp,sl);if(pos){const reasons=['Bullish engulfing on M15','RSI oversold bounce','Support level hold','MACD golden cross','Volume spike breakout','AI pattern recognition match'];addAIMessage(`&#129302; BOT EXECUTED<br><b>${type} ${volume} ${sym.pair}</b> @ ${pos.price.toFixed(5)}<br>TP: ${pos.tp.toFixed(5)} | SL: ${pos.sl.toFixed(5)}<br>Reason: ${reasons[Math.floor(Math.random()*reasons.length)]}`);}}});
}
function botManagePositions(){if(!state.positions.length)return;state.positions.forEach(p=>{if(Math.random()>.92){const pl=closePosition(p.id);const emoji=pl>=0?'&#9989;':'&#10060;';const action=pl>=0?'Take Profit hit':'Stop Loss triggered';addAIMessage(`${emoji} <b>${action}</b><br>${p.pair} ${p.type} closed<br>P&L: <b>$${pl.toFixed(2)}</b>`);}});}

// ================= ADD SYMBOL =================
function filterSymbols(q){const list=document.getElementById('symbolList');const filtered=allSymbols.filter(s=>s.toLowerCase().includes(q.toLowerCase()));list.innerHTML=filtered.map(s=>`<div style="padding:12px;border-bottom:1px solid var(--border);cursor:pointer;display:flex;justify-content:space-between;align-items:center;" onclick="addSymbol('${s}')"><span style="font-size:15px;">${s}</span><span style="color:var(--accent);font-size:20px;">+</span></div>`).join('');}
function addSymbol(s){if(!symbols.find(x=>x.pair===s)){const base=Math.random()*1000+10;symbols.push({pair:s,bid:base,ask:base+0.5,spread:Math.floor(Math.random()*50),digits:5,base});}toast('Added '+s);renderQuotes();}
function refreshSignals(){toast('Refreshing AI signals...');setTimeout(()=>toast('3 new signals generated'),800);}

// ================= INIT & LOOPS =================
window.addEventListener('resize',()=>{if(document.getElementById('tab-charts').classList.contains('active'))resizeCanvas();});
renderQuotes();initCandles('BCHUSDm');resizeCanvas();filterSymbols('');renderHistory();updateAIStatus();

setInterval(()=>{
symbols.forEach(s=>{const move=(Math.random()-.5)*s.bid*.0006;s.bid+=move;s.ask=s.bid+s.spread*Math.pow(10,-s.digits);});
renderQuotes();updateChart();updateTradeStats();
},1000);

setInterval(()=>{if(state.aiActive&&Math.random()>.4)runTradingBot();botManagePositions();},12000);

setInterval(()=>{if(state.aiActive&&Math.random()>.6){
const msgs=['Scanning 12 pairs for breakout patterns...','Volatility spike detected on JPY basket','Monitoring liquidity at 1.0850 support','Correlation shift: EUR & GBP diverging','AI model confidence: 94% on current setup'];
addAIMessage('&#129302; '+msgs[Math.floor(Math.random()*msgs.length)]);
}},35000);

</script>
</body>
</html>'''

with open('/mnt/agents/output/metanex_ai_pro.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Saved successfully! Size:", len(html), "chars")
