import{g as h,d as m,n as y,e as E,f as b,u as P,r as p,w as C}from"./@vue-500f6e4a.js";var v;const l=typeof window<"u",Q=e=>typeof e=="string",d=()=>{};l&&((v=window==null?void 0:window.navigator)==null?void 0:v.userAgent)&&/iP(ad|hone|od)/.test(window.navigator.userAgent);function S(e){return typeof e=="function"?e():P(e)}function T(e){return e}function W(e){return E()?(b(e),!0):!1}function N(e,n=!0){h()?m(e):n?e():y(e)}function x(e){var n;const t=S(e);return(n=t==null?void 0:t.$el)!=null?n:t}const _=l?window:void 0;l&&window.document;l&&window.navigator;l&&window.location;function O(...e){let n,t,o,r;if(Q(e[0])?([t,o,r]=e,n=_):[n,t,o,r]=e,!n)return d;let a=d;const u=C(()=>x(n),i=>{a(),i&&(i.addEventListener(t,o,r),a=()=>{i.removeEventListener(t,o,r),a=d})},{immediate:!0,flush:"post"}),s=()=>{u(),a()};return W(s),s}const c=typeof globalThis<"u"?globalThis:typeof window<"u"?window:typeof global<"u"?global:typeof self<"u"?self:{},f="__vueuse_ssr_handlers__";c[f]=c[f]||{};c[f];var w;(function(e){e.UP="UP",e.RIGHT="RIGHT",e.DOWN="DOWN",e.LEFT="LEFT",e.NONE="NONE"})(w||(w={}));var H=Object.defineProperty,g=Object.getOwnPropertySymbols,L=Object.prototype.hasOwnProperty,B=Object.prototype.propertyIsEnumerable,I=(e,n,t)=>n in e?H(e,n,{enumerable:!0,configurable:!0,writable:!0,value:t}):e[n]=t,U=(e,n)=>{for(var t in n||(n={}))L.call(n,t)&&I(e,t,n[t]);if(g)for(var t of g(n))B.call(n,t)&&I(e,t,n[t]);return e};const j={easeInSine:[.12,0,.39,0],easeOutSine:[.61,1,.88,1],easeInOutSine:[.37,0,.63,1],easeInQuad:[.11,0,.5,0],easeOutQuad:[.5,1,.89,1],easeInOutQuad:[.45,0,.55,1],easeInCubic:[.32,0,.67,0],easeOutCubic:[.33,1,.68,1],easeInOutCubic:[.65,0,.35,1],easeInQuart:[.5,0,.75,0],easeOutQuart:[.25,1,.5,1],easeInOutQuart:[.76,0,.24,1],easeInQuint:[.64,0,.78,0],easeOutQuint:[.22,1,.36,1],easeInOutQuint:[.83,0,.17,1],easeInExpo:[.7,0,.84,0],easeOutExpo:[.16,1,.3,1],easeInOutExpo:[.87,0,.13,1],easeInCirc:[.55,0,1,.45],easeOutCirc:[0,.55,.45,1],easeInOutCirc:[.85,0,.15,1],easeInBack:[.36,0,.66,-.56],easeOutBack:[.34,1.56,.64,1],easeInOutBack:[.68,-.6,.32,1.6]};U({linear:T},j);function z(e={}){const{window:n=_,initialWidth:t=1/0,initialHeight:o=1/0,listenOrientation:r=!0,includeScrollbar:a=!0}=e,u=p(t),s=p(o),i=()=>{n&&(a?(u.value=n.innerWidth,s.value=n.innerHeight):(u.value=n.document.documentElement.clientWidth,s.value=n.document.documentElement.clientHeight))};return i(),N(i),O("resize",i,{passive:!0}),r&&O("orientationchange",i,{passive:!0}),{width:u,height:s}}export{z as u};
