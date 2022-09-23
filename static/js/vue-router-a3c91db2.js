import{s as et,u as F,j as N,a0 as Te,n as tt,I as Be,z as q,ag as je,y as ae,r as nt,w as rt}from"./@vue-500f6e4a.js";/*!
  * vue-router v4.1.3
  * (c) 2022 Eduardo San Martin Morote
  * @license MIT
  */const z=typeof window<"u";function st(e){return e.__esModule||e[Symbol.toStringTag]==="Module"}const S=Object.assign;function le(e,t){const n={};for(const r in t){const s=t[r];n[r]=I(s)?s.map(e):e(s)}return n}const W=()=>{},I=Array.isArray,ot=/\/$/,it=e=>e.replace(ot,"");function ue(e,t,n="/"){let r,s={},l="",d="";const g=t.indexOf("#");let c=t.indexOf("?");return g<c&&g>=0&&(c=-1),c>-1&&(r=t.slice(0,c),l=t.slice(c+1,g>-1?g:t.length),s=e(l)),g>-1&&(r=r||t.slice(0,g),d=t.slice(g,t.length)),r=ut(r!=null?r:t,n),{fullPath:r+(l&&"?")+l+d,path:r,query:s,hash:d}}function ct(e,t){const n=t.query?e(t.query):"";return t.path+(n&&"?")+n+(t.hash||"")}function we(e,t){return!t||!e.toLowerCase().startsWith(t.toLowerCase())?e:e.slice(t.length)||"/"}function at(e,t,n){const r=t.matched.length-1,s=n.matched.length-1;return r>-1&&r===s&&G(t.matched[r],n.matched[s])&&ze(t.params,n.params)&&e(t.query)===e(n.query)&&t.hash===n.hash}function G(e,t){return(e.aliasOf||e)===(t.aliasOf||t)}function ze(e,t){if(Object.keys(e).length!==Object.keys(t).length)return!1;for(const n in e)if(!lt(e[n],t[n]))return!1;return!0}function lt(e,t){return I(e)?Se(e,t):I(t)?Se(t,e):e===t}function Se(e,t){return I(t)?e.length===t.length&&e.every((n,r)=>n===t[r]):e.length===1&&e[0]===t}function ut(e,t){if(e.startsWith("/"))return e;if(!e)return t;const n=t.split("/"),r=e.split("/");let s=n.length-1,l,d;for(l=0;l<r.length;l++)if(d=r[l],d!==".")if(d==="..")s>1&&s--;else break;return n.slice(0,s).join("/")+"/"+r.slice(l-(l===r.length?1:0)).join("/")}var X;(function(e){e.pop="pop",e.push="push"})(X||(X={}));var Y;(function(e){e.back="back",e.forward="forward",e.unknown=""})(Y||(Y={}));function ft(e){if(!e)if(z){const t=document.querySelector("base");e=t&&t.getAttribute("href")||"/",e=e.replace(/^\w+:\/\/[^\/]+/,"")}else e="/";return e[0]!=="/"&&e[0]!=="#"&&(e="/"+e),it(e)}const ht=/^[^#]+#/;function dt(e,t){return e.replace(ht,"#")+t}function pt(e,t){const n=document.documentElement.getBoundingClientRect(),r=e.getBoundingClientRect();return{behavior:t.behavior,left:r.left-n.left-(t.left||0),top:r.top-n.top-(t.top||0)}}const ee=()=>({left:window.pageXOffset,top:window.pageYOffset});function mt(e){let t;if("el"in e){const n=e.el,r=typeof n=="string"&&n.startsWith("#"),s=typeof n=="string"?r?document.getElementById(n.slice(1)):document.querySelector(n):n;if(!s)return;t=pt(s,e)}else t=e;"scrollBehavior"in document.documentElement.style?window.scrollTo(t):window.scrollTo(t.left!=null?t.left:window.pageXOffset,t.top!=null?t.top:window.pageYOffset)}function Ce(e,t){return(history.state?history.state.position-t:-1)+e}const he=new Map;function gt(e,t){he.set(e,t)}function vt(e){const t=he.get(e);return he.delete(e),t}let yt=()=>location.protocol+"//"+location.host;function qe(e,t){const{pathname:n,search:r,hash:s}=t,l=e.indexOf("#");if(l>-1){let g=s.includes(e.slice(l))?e.slice(l).length:1,c=s.slice(g);return c[0]!=="/"&&(c="/"+c),we(c,"")}return we(n,e)+r+s}function Rt(e,t,n,r){let s=[],l=[],d=null;const g=({state:f})=>{const m=qe(e,location),y=n.value,b=t.value;let k=0;if(f){if(n.value=m,t.value=f,d&&d===y){d=null;return}k=b?f.position-b.position:0}else r(m);s.forEach(P=>{P(n.value,y,{delta:k,type:X.pop,direction:k?k>0?Y.forward:Y.back:Y.unknown})})};function c(){d=n.value}function u(f){s.push(f);const m=()=>{const y=s.indexOf(f);y>-1&&s.splice(y,1)};return l.push(m),m}function o(){const{history:f}=window;!f.state||f.replaceState(S({},f.state,{scroll:ee()}),"")}function a(){for(const f of l)f();l=[],window.removeEventListener("popstate",g),window.removeEventListener("beforeunload",o)}return window.addEventListener("popstate",g),window.addEventListener("beforeunload",o),{pauseListeners:c,listen:u,destroy:a}}function ke(e,t,n,r=!1,s=!1){return{back:e,current:t,forward:n,replaced:r,position:window.history.length,scroll:s?ee():null}}function Et(e){const{history:t,location:n}=window,r={value:qe(e,n)},s={value:t.state};s.value||l(r.value,{back:null,current:r.value,forward:null,position:t.length-1,replaced:!0,scroll:null},!0);function l(c,u,o){const a=e.indexOf("#"),f=a>-1?(n.host&&document.querySelector("base")?e:e.slice(a))+c:yt()+e+c;try{t[o?"replaceState":"pushState"](u,"",f),s.value=u}catch(m){console.error(m),n[o?"replace":"assign"](f)}}function d(c,u){const o=S({},t.state,ke(s.value.back,c,s.value.forward,!0),u,{position:s.value.position});l(c,o,!0),r.value=c}function g(c,u){const o=S({},s.value,t.state,{forward:c,scroll:ee()});l(o.current,o,!0);const a=S({},ke(r.value,c,null),{position:o.position+1},u);l(c,a,!1),r.value=c}return{location:r,state:s,push:g,replace:d}}function Pt(e){e=ft(e);const t=Et(e),n=Rt(e,t.state,t.location,t.replace);function r(l,d=!0){d||n.pauseListeners(),history.go(l)}const s=S({location:"",base:e,go:r,createHref:dt.bind(null,e)},t,n);return Object.defineProperty(s,"location",{enumerable:!0,get:()=>t.location.value}),Object.defineProperty(s,"state",{enumerable:!0,get:()=>t.state.value}),s}function ln(e){return e=location.host?e||location.pathname+location.search:"",e.includes("#")||(e+="#"),Pt(e)}function wt(e){return typeof e=="string"||e&&typeof e=="object"}function Ge(e){return typeof e=="string"||typeof e=="symbol"}const H={path:"/",name:void 0,params:{},query:{},hash:"",fullPath:"/",matched:[],meta:{},redirectedFrom:void 0},Ke=Symbol("");var be;(function(e){e[e.aborted=4]="aborted",e[e.cancelled=8]="cancelled",e[e.duplicated=16]="duplicated"})(be||(be={}));function K(e,t){return S(new Error,{type:e,[Ke]:!0},t)}function $(e,t){return e instanceof Error&&Ke in e&&(t==null||!!(e.type&t))}const Ae="[^/]+?",St={sensitive:!1,strict:!1,start:!0,end:!0},Ct=/[.+*?^${}()[\]/\\]/g;function kt(e,t){const n=S({},St,t),r=[];let s=n.start?"^":"";const l=[];for(const u of e){const o=u.length?[]:[90];n.strict&&!u.length&&(s+="/");for(let a=0;a<u.length;a++){const f=u[a];let m=40+(n.sensitive?.25:0);if(f.type===0)a||(s+="/"),s+=f.value.replace(Ct,"\\$&"),m+=40;else if(f.type===1){const{value:y,repeatable:b,optional:k,regexp:P}=f;l.push({name:y,repeatable:b,optional:k});const w=P||Ae;if(w!==Ae){m+=10;try{new RegExp(`(${w})`)}catch(M){throw new Error(`Invalid custom RegExp for param "${y}" (${w}): `+M.message)}}let O=b?`((?:${w})(?:/(?:${w}))*)`:`(${w})`;a||(O=k&&u.length<2?`(?:/${O})`:"/"+O),k&&(O+="?"),s+=O,m+=20,k&&(m+=-8),b&&(m+=-20),w===".*"&&(m+=-50)}o.push(m)}r.push(o)}if(n.strict&&n.end){const u=r.length-1;r[u][r[u].length-1]+=.7000000000000001}n.strict||(s+="/?"),n.end?s+="$":n.strict&&(s+="(?:/|$)");const d=new RegExp(s,n.sensitive?"":"i");function g(u){const o=u.match(d),a={};if(!o)return null;for(let f=1;f<o.length;f++){const m=o[f]||"",y=l[f-1];a[y.name]=m&&y.repeatable?m.split("/"):m}return a}function c(u){let o="",a=!1;for(const f of e){(!a||!o.endsWith("/"))&&(o+="/"),a=!1;for(const m of f)if(m.type===0)o+=m.value;else if(m.type===1){const{value:y,repeatable:b,optional:k}=m,P=y in u?u[y]:"";if(I(P)&&!b)throw new Error(`Provided param "${y}" is an array but it is not repeatable (* or + modifiers)`);const w=I(P)?P.join("/"):P;if(!w)if(k)f.length<2&&(o.endsWith("/")?o=o.slice(0,-1):a=!0);else throw new Error(`Missing required param "${y}"`);o+=w}}return o||"/"}return{re:d,score:r,keys:l,parse:g,stringify:c}}function bt(e,t){let n=0;for(;n<e.length&&n<t.length;){const r=t[n]-e[n];if(r)return r;n++}return e.length<t.length?e.length===1&&e[0]===40+40?-1:1:e.length>t.length?t.length===1&&t[0]===40+40?1:-1:0}function At(e,t){let n=0;const r=e.score,s=t.score;for(;n<r.length&&n<s.length;){const l=bt(r[n],s[n]);if(l)return l;n++}if(Math.abs(s.length-r.length)===1){if(_e(r))return 1;if(_e(s))return-1}return s.length-r.length}function _e(e){const t=e[e.length-1];return e.length>0&&t[t.length-1]<0}const _t={type:0,value:""},Ot=/[a-zA-Z0-9_]/;function xt(e){if(!e)return[[]];if(e==="/")return[[_t]];if(!e.startsWith("/"))throw new Error(`Invalid path "${e}"`);function t(m){throw new Error(`ERR (${n})/"${u}": ${m}`)}let n=0,r=n;const s=[];let l;function d(){l&&s.push(l),l=[]}let g=0,c,u="",o="";function a(){!u||(n===0?l.push({type:0,value:u}):n===1||n===2||n===3?(l.length>1&&(c==="*"||c==="+")&&t(`A repeatable param (${u}) must be alone in its segment. eg: '/:ids+.`),l.push({type:1,value:u,regexp:o,repeatable:c==="*"||c==="+",optional:c==="*"||c==="?"})):t("Invalid state to consume buffer"),u="")}function f(){u+=c}for(;g<e.length;){if(c=e[g++],c==="\\"&&n!==2){r=n,n=4;continue}switch(n){case 0:c==="/"?(u&&a(),d()):c===":"?(a(),n=1):f();break;case 4:f(),n=r;break;case 1:c==="("?n=2:Ot.test(c)?f():(a(),n=0,c!=="*"&&c!=="?"&&c!=="+"&&g--);break;case 2:c===")"?o[o.length-1]=="\\"?o=o.slice(0,-1)+c:n=3:o+=c;break;case 3:a(),n=0,c!=="*"&&c!=="?"&&c!=="+"&&g--,o="";break;default:t("Unknown state");break}}return n===2&&t(`Unfinished custom RegExp for param "${u}"`),a(),d(),s}function Mt(e,t,n){const r=kt(xt(e.path),n),s=S(r,{record:e,parent:t,children:[],alias:[]});return t&&!s.record.aliasOf==!t.record.aliasOf&&t.children.push(s),s}function Nt(e,t){const n=[],r=new Map;t=xe({strict:!1,end:!0,sensitive:!1},t);function s(o){return r.get(o)}function l(o,a,f){const m=!f,y=Lt(o);y.aliasOf=f&&f.record;const b=xe(t,o),k=[y];if("alias"in o){const O=typeof o.alias=="string"?[o.alias]:o.alias;for(const M of O)k.push(S({},y,{components:f?f.record.components:y.components,path:M,aliasOf:f?f.record:y}))}let P,w;for(const O of k){const{path:M}=O;if(a&&M[0]!=="/"){const B=a.record.path,L=B[B.length-1]==="/"?"":"/";O.path=a.record.path+(M&&L+M)}if(P=Mt(O,a,b),f?f.alias.push(P):(w=w||P,w!==P&&w.alias.push(P),m&&o.name&&!Oe(P)&&d(o.name)),y.children){const B=y.children;for(let L=0;L<B.length;L++)l(B[L],P,f&&f.children[L])}f=f||P,c(P)}return w?()=>{d(w)}:W}function d(o){if(Ge(o)){const a=r.get(o);a&&(r.delete(o),n.splice(n.indexOf(a),1),a.children.forEach(d),a.alias.forEach(d))}else{const a=n.indexOf(o);a>-1&&(n.splice(a,1),o.record.name&&r.delete(o.record.name),o.children.forEach(d),o.alias.forEach(d))}}function g(){return n}function c(o){let a=0;for(;a<n.length&&At(o,n[a])>=0&&(o.record.path!==n[a].record.path||!Ve(o,n[a]));)a++;n.splice(a,0,o),o.record.name&&!Oe(o)&&r.set(o.record.name,o)}function u(o,a){let f,m={},y,b;if("name"in o&&o.name){if(f=r.get(o.name),!f)throw K(1,{location:o});b=f.record.name,m=S(It(a.params,f.keys.filter(w=>!w.optional).map(w=>w.name)),o.params),y=f.stringify(m)}else if("path"in o)y=o.path,f=n.find(w=>w.re.test(y)),f&&(m=f.parse(y),b=f.record.name);else{if(f=a.name?r.get(a.name):n.find(w=>w.re.test(a.path)),!f)throw K(1,{location:o,currentLocation:a});b=f.record.name,m=S({},a.params,o.params),y=f.stringify(m)}const k=[];let P=f;for(;P;)k.unshift(P.record),P=P.parent;return{name:b,path:y,params:m,matched:k,meta:Ht(k)}}return e.forEach(o=>l(o)),{addRoute:l,resolve:u,removeRoute:d,getRoutes:g,getRecordMatcher:s}}function It(e,t){const n={};for(const r of t)r in e&&(n[r]=e[r]);return n}function Lt(e){return{path:e.path,redirect:e.redirect,name:e.name,meta:e.meta||{},aliasOf:void 0,beforeEnter:e.beforeEnter,props:$t(e),children:e.children||[],instances:{},leaveGuards:new Set,updateGuards:new Set,enterCallbacks:{},components:"components"in e?e.components||null:e.component&&{default:e.component}}}function $t(e){const t={},n=e.props||!1;if("component"in e)t.default=n;else for(const r in e.components)t[r]=typeof n=="boolean"?n:n[r];return t}function Oe(e){for(;e;){if(e.record.aliasOf)return!0;e=e.parent}return!1}function Ht(e){return e.reduce((t,n)=>S(t,n.meta),{})}function xe(e,t){const n={};for(const r in e)n[r]=r in t?t[r]:e[r];return n}function Ve(e,t){return t.children.some(n=>n===e||Ve(e,n))}const Ue=/#/g,Tt=/&/g,Bt=/\//g,jt=/=/g,zt=/\?/g,De=/\+/g,qt=/%5B/g,Gt=/%5D/g,Qe=/%5E/g,Kt=/%60/g,Fe=/%7B/g,Vt=/%7C/g,We=/%7D/g,Ut=/%20/g;function me(e){return encodeURI(""+e).replace(Vt,"|").replace(qt,"[").replace(Gt,"]")}function Dt(e){return me(e).replace(Fe,"{").replace(We,"}").replace(Qe,"^")}function de(e){return me(e).replace(De,"%2B").replace(Ut,"+").replace(Ue,"%23").replace(Tt,"%26").replace(Kt,"`").replace(Fe,"{").replace(We,"}").replace(Qe,"^")}function Qt(e){return de(e).replace(jt,"%3D")}function Ft(e){return me(e).replace(Ue,"%23").replace(zt,"%3F")}function Wt(e){return e==null?"":Ft(e).replace(Bt,"%2F")}function J(e){try{return decodeURIComponent(""+e)}catch{}return""+e}function Yt(e){const t={};if(e===""||e==="?")return t;const r=(e[0]==="?"?e.slice(1):e).split("&");for(let s=0;s<r.length;++s){const l=r[s].replace(De," "),d=l.indexOf("="),g=J(d<0?l:l.slice(0,d)),c=d<0?null:J(l.slice(d+1));if(g in t){let u=t[g];I(u)||(u=t[g]=[u]),u.push(c)}else t[g]=c}return t}function Me(e){let t="";for(let n in e){const r=e[n];if(n=Qt(n),r==null){r!==void 0&&(t+=(t.length?"&":"")+n);continue}(I(r)?r.map(l=>l&&de(l)):[r&&de(r)]).forEach(l=>{l!==void 0&&(t+=(t.length?"&":"")+n,l!=null&&(t+="="+l))})}return t}function Xt(e){const t={};for(const n in e){const r=e[n];r!==void 0&&(t[n]=I(r)?r.map(s=>s==null?null:""+s):r==null?r:""+r)}return t}const Zt=Symbol(""),Ne=Symbol(""),te=Symbol(""),Ye=Symbol(""),pe=Symbol("");function Q(){let e=[];function t(r){return e.push(r),()=>{const s=e.indexOf(r);s>-1&&e.splice(s,1)}}function n(){e=[]}return{add:t,list:()=>e,reset:n}}function T(e,t,n,r,s){const l=r&&(r.enterCallbacks[s]=r.enterCallbacks[s]||[]);return()=>new Promise((d,g)=>{const c=a=>{a===!1?g(K(4,{from:n,to:t})):a instanceof Error?g(a):wt(a)?g(K(2,{from:t,to:a})):(l&&r.enterCallbacks[s]===l&&typeof a=="function"&&l.push(a),d())},u=e.call(r&&r.instances[s],t,n,c);let o=Promise.resolve(u);e.length<3&&(o=o.then(c)),o.catch(a=>g(a))})}function fe(e,t,n,r){const s=[];for(const l of e)for(const d in l.components){let g=l.components[d];if(!(t!=="beforeRouteEnter"&&!l.instances[d]))if(Jt(g)){const u=(g.__vccOpts||g)[t];u&&s.push(T(u,n,r,l,d))}else{let c=g();s.push(()=>c.then(u=>{if(!u)return Promise.reject(new Error(`Couldn't resolve component "${d}" at "${l.path}"`));const o=st(u)?u.default:u;l.components[d]=o;const f=(o.__vccOpts||o)[t];return f&&T(f,n,r,l,d)()}))}}return s}function Jt(e){return typeof e=="object"||"displayName"in e||"props"in e||"__vccOpts"in e}function Ie(e){const t=q(te),n=q(Ye),r=N(()=>t.resolve(F(e.to))),s=N(()=>{const{matched:c}=r.value,{length:u}=c,o=c[u-1],a=n.matched;if(!o||!a.length)return-1;const f=a.findIndex(G.bind(null,o));if(f>-1)return f;const m=Le(c[u-2]);return u>1&&Le(o)===m&&a[a.length-1].path!==m?a.findIndex(G.bind(null,c[u-2])):f}),l=N(()=>s.value>-1&&rn(n.params,r.value.params)),d=N(()=>s.value>-1&&s.value===n.matched.length-1&&ze(n.params,r.value.params));function g(c={}){return nn(c)?t[F(e.replace)?"replace":"push"](F(e.to)).catch(W):Promise.resolve()}return{route:r,href:N(()=>r.value.href),isActive:l,isExactActive:d,navigate:g}}const en=Be({name:"RouterLink",compatConfig:{MODE:3},props:{to:{type:[String,Object],required:!0},replace:Boolean,activeClass:String,exactActiveClass:String,custom:Boolean,ariaCurrentValue:{type:String,default:"page"}},useLink:Ie,setup(e,{slots:t}){const n=Te(Ie(e)),{options:r}=q(te),s=N(()=>({[$e(e.activeClass,r.linkActiveClass,"router-link-active")]:n.isActive,[$e(e.exactActiveClass,r.linkExactActiveClass,"router-link-exact-active")]:n.isExactActive}));return()=>{const l=t.default&&t.default(n);return e.custom?l:je("a",{"aria-current":n.isExactActive?e.ariaCurrentValue:null,href:n.href,onClick:n.navigate,class:s.value},l)}}}),tn=en;function nn(e){if(!(e.metaKey||e.altKey||e.ctrlKey||e.shiftKey)&&!e.defaultPrevented&&!(e.button!==void 0&&e.button!==0)){if(e.currentTarget&&e.currentTarget.getAttribute){const t=e.currentTarget.getAttribute("target");if(/\b_blank\b/i.test(t))return}return e.preventDefault&&e.preventDefault(),!0}}function rn(e,t){for(const n in t){const r=t[n],s=e[n];if(typeof r=="string"){if(r!==s)return!1}else if(!I(s)||s.length!==r.length||r.some((l,d)=>l!==s[d]))return!1}return!0}function Le(e){return e?e.aliasOf?e.aliasOf.path:e.path:""}const $e=(e,t,n)=>e!=null?e:t!=null?t:n,sn=Be({name:"RouterView",inheritAttrs:!1,props:{name:{type:String,default:"default"},route:Object},compatConfig:{MODE:3},setup(e,{attrs:t,slots:n}){const r=q(pe),s=N(()=>e.route||r.value),l=q(Ne,0),d=N(()=>{let u=F(l);const{matched:o}=s.value;let a;for(;(a=o[u])&&!a.components;)u++;return u}),g=N(()=>s.value.matched[d.value]);ae(Ne,N(()=>d.value+1)),ae(Zt,g),ae(pe,s);const c=nt();return rt(()=>[c.value,g.value,e.name],([u,o,a],[f,m,y])=>{o&&(o.instances[a]=u,m&&m!==o&&u&&u===f&&(o.leaveGuards.size||(o.leaveGuards=m.leaveGuards),o.updateGuards.size||(o.updateGuards=m.updateGuards))),u&&o&&(!m||!G(o,m)||!f)&&(o.enterCallbacks[a]||[]).forEach(b=>b(u))},{flush:"post"}),()=>{const u=s.value,o=e.name,a=g.value,f=a&&a.components[o];if(!f)return He(n.default,{Component:f,route:u});const m=a.props[o],y=m?m===!0?u.params:typeof m=="function"?m(u):m:null,k=je(f,S({},y,t,{onVnodeUnmounted:P=>{P.component.isUnmounted&&(a.instances[o]=null)},ref:c}));return He(n.default,{Component:k,route:u})||k}}});function He(e,t){if(!e)return null;const n=e(t);return n.length===1?n[0]:n}const on=sn;function un(e){const t=Nt(e.routes,e),n=e.parseQuery||Yt,r=e.stringifyQuery||Me,s=e.history,l=Q(),d=Q(),g=Q(),c=et(H);let u=H;z&&e.scrollBehavior&&"scrollRestoration"in history&&(history.scrollRestoration="manual");const o=le.bind(null,i=>""+i),a=le.bind(null,Wt),f=le.bind(null,J);function m(i,p){let h,v;return Ge(i)?(h=t.getRecordMatcher(i),v=p):v=i,t.addRoute(v,h)}function y(i){const p=t.getRecordMatcher(i);p&&t.removeRoute(p)}function b(){return t.getRoutes().map(i=>i.record)}function k(i){return!!t.getRecordMatcher(i)}function P(i,p){if(p=S({},p||c.value),typeof i=="string"){const R=ue(n,i,p.path),_=t.resolve({path:R.path},p),D=s.createHref(R.fullPath);return S(R,_,{params:f(_.params),hash:J(R.hash),redirectedFrom:void 0,href:D})}let h;if("path"in i)h=S({},i,{path:ue(n,i.path,p.path).path});else{const R=S({},i.params);for(const _ in R)R[_]==null&&delete R[_];h=S({},i,{params:a(i.params)}),p.params=a(p.params)}const v=t.resolve(h,p),C=i.hash||"";v.params=o(f(v.params));const A=ct(r,S({},i,{hash:Dt(C),path:v.path})),E=s.createHref(A);return S({fullPath:A,hash:C,query:r===Me?Xt(i.query):i.query||{}},v,{redirectedFrom:void 0,href:E})}function w(i){return typeof i=="string"?ue(n,i,c.value.path):S({},i)}function O(i,p){if(u!==i)return K(8,{from:p,to:i})}function M(i){return V(i)}function B(i){return M(S(w(i),{replace:!0}))}function L(i){const p=i.matched[i.matched.length-1];if(p&&p.redirect){const{redirect:h}=p;let v=typeof h=="function"?h(i):h;return typeof v=="string"&&(v=v.includes("?")||v.includes("#")?v=w(v):{path:v},v.params={}),S({query:i.query,hash:i.hash,params:"path"in v?{}:i.params},v)}}function V(i,p){const h=u=P(i),v=c.value,C=i.state,A=i.force,E=i.replace===!0,R=L(h);if(R)return V(S(w(R),{state:C,force:A,replace:E}),p||h);const _=h;_.redirectedFrom=p;let D;return!A&&at(r,v,h)&&(D=K(16,{to:_,from:v}),Ee(v,v,!0,!1)),(D?Promise.resolve(D):ge(_,v)).catch(x=>$(x)?$(x,2)?x:se(x):re(x,_,v)).then(x=>{if(x){if($(x,2))return V(S({replace:E},w(x.to),{state:C,force:A}),p||_)}else x=ye(_,v,!0,E,C);return ve(_,v,x),x})}function Xe(i,p){const h=O(i,p);return h?Promise.reject(h):Promise.resolve()}function ge(i,p){let h;const[v,C,A]=cn(i,p);h=fe(v.reverse(),"beforeRouteLeave",i,p);for(const R of v)R.leaveGuards.forEach(_=>{h.push(T(_,i,p))});const E=Xe.bind(null,i,p);return h.push(E),j(h).then(()=>{h=[];for(const R of l.list())h.push(T(R,i,p));return h.push(E),j(h)}).then(()=>{h=fe(C,"beforeRouteUpdate",i,p);for(const R of C)R.updateGuards.forEach(_=>{h.push(T(_,i,p))});return h.push(E),j(h)}).then(()=>{h=[];for(const R of i.matched)if(R.beforeEnter&&!p.matched.includes(R))if(I(R.beforeEnter))for(const _ of R.beforeEnter)h.push(T(_,i,p));else h.push(T(R.beforeEnter,i,p));return h.push(E),j(h)}).then(()=>(i.matched.forEach(R=>R.enterCallbacks={}),h=fe(A,"beforeRouteEnter",i,p),h.push(E),j(h))).then(()=>{h=[];for(const R of d.list())h.push(T(R,i,p));return h.push(E),j(h)}).catch(R=>$(R,8)?R:Promise.reject(R))}function ve(i,p,h){for(const v of g.list())v(i,p,h)}function ye(i,p,h,v,C){const A=O(i,p);if(A)return A;const E=p===H,R=z?history.state:{};h&&(v||E?s.replace(i.fullPath,S({scroll:E&&R&&R.scroll},C)):s.push(i.fullPath,C)),c.value=i,Ee(i,p,h,E),se()}let U;function Ze(){U||(U=s.listen((i,p,h)=>{if(!Pe.listening)return;const v=P(i),C=L(v);if(C){V(S(C,{replace:!0}),v).catch(W);return}u=v;const A=c.value;z&&gt(Ce(A.fullPath,h.delta),ee()),ge(v,A).catch(E=>$(E,12)?E:$(E,2)?(V(E.to,v).then(R=>{$(R,20)&&!h.delta&&h.type===X.pop&&s.go(-1,!1)}).catch(W),Promise.reject()):(h.delta&&s.go(-h.delta,!1),re(E,v,A))).then(E=>{E=E||ye(v,A,!1),E&&(h.delta&&!$(E,8)?s.go(-h.delta,!1):h.type===X.pop&&$(E,20)&&s.go(-1,!1)),ve(v,A,E)}).catch(W)}))}let ne=Q(),Re=Q(),Z;function re(i,p,h){se(i);const v=Re.list();return v.length?v.forEach(C=>C(i,p,h)):console.error(i),Promise.reject(i)}function Je(){return Z&&c.value!==H?Promise.resolve():new Promise((i,p)=>{ne.add([i,p])})}function se(i){return Z||(Z=!i,Ze(),ne.list().forEach(([p,h])=>i?h(i):p()),ne.reset()),i}function Ee(i,p,h,v){const{scrollBehavior:C}=e;if(!z||!C)return Promise.resolve();const A=!h&&vt(Ce(i.fullPath,0))||(v||!h)&&history.state&&history.state.scroll||null;return tt().then(()=>C(i,p,A)).then(E=>E&&mt(E)).catch(E=>re(E,i,p))}const oe=i=>s.go(i);let ie;const ce=new Set,Pe={currentRoute:c,listening:!0,addRoute:m,removeRoute:y,hasRoute:k,getRoutes:b,resolve:P,options:e,push:M,replace:B,go:oe,back:()=>oe(-1),forward:()=>oe(1),beforeEach:l.add,beforeResolve:d.add,afterEach:g.add,onError:Re.add,isReady:Je,install(i){const p=this;i.component("RouterLink",tn),i.component("RouterView",on),i.config.globalProperties.$router=p,Object.defineProperty(i.config.globalProperties,"$route",{enumerable:!0,get:()=>F(c)}),z&&!ie&&c.value===H&&(ie=!0,M(s.location).catch(C=>{}));const h={};for(const C in H)h[C]=N(()=>c.value[C]);i.provide(te,p),i.provide(Ye,Te(h)),i.provide(pe,c);const v=i.unmount;ce.add(i),i.unmount=function(){ce.delete(i),ce.size<1&&(u=H,U&&U(),U=null,c.value=H,ie=!1,Z=!1),v()}}};return Pe}function j(e){return e.reduce((t,n)=>t.then(()=>n()),Promise.resolve())}function cn(e,t){const n=[],r=[],s=[],l=Math.max(t.matched.length,e.matched.length);for(let d=0;d<l;d++){const g=t.matched[d];g&&(e.matched.find(u=>G(u,g))?r.push(g):n.push(g));const c=e.matched[d];c&&(t.matched.find(u=>G(u,c))||s.push(c))}return[n,r,s]}function fn(){return q(te)}export{ln as a,un as c,fn as u};
