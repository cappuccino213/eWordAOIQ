import{l as S,E as P,a as I,b as M,m as $,n as B,o as L,p as W,q as O,r as R,s as N,t as V,u as q}from"./element-plus-df419614.js";import{r as w,o,c as m,X as e,Q as t,F as D,a7 as A,P as u,T as E,a as i,W as k,u as h,d as j,V as C,ay as z,az as F,a4 as H,E as U,Y as K,aA as Q}from"./@vue-500f6e4a.js";import{_ as y,l as b}from"./index-66a691da.js";import{u as X}from"./vue-router-a3c91db2.js";import"./lodash-es-8e578a42.js";import"./@element-plus-58134fba.js";import"./@popperjs-892fd7f5.js";import"./@ctrl-eb0b847c.js";import"./dayjs-d69067b3.js";import"./axios-805d1980.js";import"./async-validator-efc2d198.js";import"./memoize-one-99e54574.js";import"./escape-html-4bbaf1e1.js";import"./normalize-wheel-es-da779ce4.js";import"./@floating-ui-d1015eb5.js";import"./lodash-4ca21166.js";import"./pinia-d75d73cf.js";import"./pinia-plugin-persistedstate-4761f546.js";const Y=[{name:"\u8003\u6838\u6307\u6807",index:"/targetSetPage",icon:"Aim"},{name:"\u7814\u53D1\u8003\u6838",index:"/defectActivate",icon:"Connection",children:[{name:"\u6FC0\u6D3B\u7F3A\u9677",index:"/defectActivate",icon:"Pointer"},{name:"\u4E25\u91CD\u7F3A\u9677",index:"/defectLevel",icon:"Position"},{name:"\u9057\u6F0F\u7F3A\u9677",index:"/defectOmit",icon:"View"},{name:"\u81EA\u6D4B\u5192\u70DF",index:"/selfTesting",icon:"Open"}]}],G=[{name:"\u6FC0\u6D3B\u7F3A\u9677",index:"/defectActivate",icon:"Pointer"},{name:"\u4E25\u91CD\u7F3A\u9677",index:"/defectLevel",icon:"Position"},{name:"\u9057\u6F0F\u7F3A\u9677",index:"/defectOmit",icon:"View"},{name:"\u81EA\u6D4B\u5192\u70DF",index:"/selfTesting",icon:"Open"}],J=[{name:"\u8003\u6838\u6307\u6807",index:"/targetSetPage",icon:"Aim"},{name:"\u8003\u6838\u9879\u76EE",index:"/smokeTestRecord",icon:"Smoking",children:[{name:"\u5192\u70DF\u6807\u8BB0",index:"/smokeTestRecord",icon:"WindPower"},{name:"\u5192\u70DF\u5217\u8868",index:"/smokeTestList",icon:"Document"}]},{name:"\u6D4B\u8BD5\u8003\u6838",index:"/invalidDefect",icon:"Notification",children:[{name:"\u65E0\u6548\u7F3A\u9677",index:"/invalidDefect",icon:"Close"},{name:"\u4E25\u91CD\u7F3A\u9677",index:"/seriousDefect",icon:"Warning"},{name:"\u9879\u76EE\u6743\u91CD",index:"/projectWeight",icon:"Open"},{name:"\u9057\u6F0F\u7F3A\u9677",index:"/omitDefect",icon:"Lock"}]}],Z=[{name:"\u8003\u6838\u9879\u76EE",index:"/smokeTestRecord",icon:"Smoking",children:[{name:"\u5192\u70DF\u6807\u8BB0",index:"/smokeTestRecord",icon:"WindPower"},{name:"\u5192\u70DF\u5217\u8868",index:"/smokeTestList",icon:"Document"}]},{name:"\u6D4B\u8BD5\u8003\u6838",index:"/invalidDefect",icon:"Notification",children:[{name:"\u65E0\u6548\u7F3A\u9677",index:"/invalidDefect",icon:"Close"},{name:"\u4E25\u91CD\u7F3A\u9677",index:"/seriousDefect",icon:"Warning"},{name:"\u9879\u76EE\u6743\u91CD",index:"/projectWeight",icon:"Open"},{name:"\u9057\u6F0F\u7F3A\u9677",index:"/omitDefect",icon:"Lock"}]}],ee=[{name:"\u8003\u6838\u6307\u6807",index:"/targetSetPage",icon:"Aim"},{name:"\u8003\u6838\u9879\u76EE",index:"/smokeTestRecord",icon:"Smoking",children:[{name:"\u5192\u70DF\u6807\u8BB0",index:"/smokeTestRecord",icon:"WindPower"},{name:"\u5192\u70DF\u5217\u8868",index:"/smokeTestList",icon:"Document"}]},{name:"\u7814\u53D1\u8003\u6838",index:"/defectActivate",icon:"Connection",children:[{name:"\u6FC0\u6D3B\u7F3A\u9677",index:"/defectActivate",icon:"Pointer"},{name:"\u4E25\u91CD\u7F3A\u9677",index:"/defectLevel",icon:"Position"},{name:"\u9057\u6F0F\u7F3A\u9677",index:"/defectOmit",icon:"View"},{name:"\u81EA\u6D4B\u5192\u70DF",index:"/selfTesting",icon:"Open"}]},{name:"\u6D4B\u8BD5\u8003\u6838",index:"/invalidDefect",icon:"Notification",children:[{name:"\u65E0\u6548\u7F3A\u9677",index:"/invalidDefect",icon:"Close"},{name:"\u4E25\u91CD\u7F3A\u9677",index:"/seriousDefect",icon:"Warning"},{name:"\u9879\u76EE\u6743\u91CD",index:"/projectWeight",icon:"Open"},{name:"\u9057\u6F0F\u7F3A\u9677",index:"/omitDefect",icon:"Lock"}]}];const ne={class:"wrapper"},te={style:{"margin-left":"7px"}},oe={__name:"index",props:{collapse:{type:Boolean,default:!1},defaultActive:{type:String,default:""},router:{type:Boolean,default:!0},name:{type:String,default:"name"},index:{type:String,default:"index"},icon:{type:String,default:"icon"},children:{type:String,default:"children"}},setup(n){let a=w();const s=b.getCache("role"),d=_=>({dev:G,td:Y,qa:Z,qd:J,top:ee})[_];return a.value=d(s),(_,f)=>{const p=S,l=P,x=I,r=M;return o(),m("div",ne,[e(r,{data:h(a),router:"",defaultActive:_.$route.path,collapse:n.collapse,style:{width:"150px"}},{default:t(()=>[(o(!0),m(D,null,A(h(a),(c,g)=>(o(),m(D,{key:g},[c[n.children]?(o(),u(x,{key:0,index:c[n.index]},{title:t(()=>[e(p,null,{default:t(()=>[(o(),u(E(c[n.icon])))]),_:2},1024),i("span",null,k(c[n.name]),1)]),default:t(()=>[(o(!0),m(D,null,A(c[n.children],v=>(o(),u(l,{key:v[n.index],index:v[n.index]},{default:t(()=>[i("span",te,k(v[n.name]),1)]),_:2},1032,["index"]))),128))]),_:2},1032,["index"])):(o(),u(l,{key:1,index:c[n.index]},{default:t(()=>[e(p,null,{default:t(()=>[(o(),u(E(c[n.icon])))]),_:2},1024),i("span",null,k(c[n.name]),1)]),_:2},1032,["index"]))],64))),128))]),_:1},8,["data","defaultActive","collapse"])])}}},ae=y(oe,[["__scopeId","data-v-40c18fbd"]]),ie="/static/img/company-logo-523f8b26.svg",ce={class:"nav-breadcrumb"},se={__name:"navBreadcrumb",setup(n){return(a,s)=>{const d=$;return o(),m("div",ce,[e(d,{separator:"/"})])}}};const de={class:"user-info DarkModelPage"},le={class:"el-dropdown-link"},re={class:"name"},me=C("\u7528\u6237\u4FE1\u606F"),_e=C("\u9000\u51FA\u767B\u5F55"),ue={__name:"userInfo",setup(n){let a=w("");const s=w(!1),d=X();j(()=>{window.document.documentElement.setAttribute("data-theme","light"),_()});const _=()=>{var l;a.value=(l=b.getCache("name"))!=null?l:""},f=()=>{s.value=!s.value,s.value?window.document.documentElement.setAttribute("data-theme","dark"):window.document.documentElement.setAttribute("data-theme","light")},p=()=>{b.deleteCache("token"),d.push("/login")};return(l,x)=>{const r=S,c=B,g=L,v=W,T=O;return o(),m("div",de,[i("div",{class:"switchTheme",onClick:f},[e(r)]),e(T,null,{dropdown:t(()=>[e(v,null,{default:t(()=>[e(g,null,{default:t(()=>[me]),_:1}),e(g,{onClick:p},{default:t(()=>[_e]),_:1})]),_:1})]),default:t(()=>[i("span",le,[e(c,{size:30,src:"https://cube.elemecdn.com/0/88/03b0d39583f48206768a7534e55bcpng.png"}),i("span",re,k(h(a)),1)])]),_:1})])}}},pe=y(ue,[["__scopeId","data-v-c24dfcae"]]);const fe=n=>(z("data-v-7e6361d3"),n=n(),F(),n),xe={class:"header"},ve=fe(()=>i("div",{class:"left-wrapper"},[i("div",{class:"logo"},[i("img",{class:"img",src:ie,alt:"logo"})]),i("span",null,"\u5168\u7F51\u4E91\u8003\u6838\u5BA2\u89C2\u6307\u6807\u67E5\u8BE2\u5E73\u53F0")],-1)),he={class:"userinfo"},ge={__name:"index",props:{collapse:{type:Boolean,default:!1}},emits:["update:collapse"],setup(n,{emit:a}){return(s,d)=>(o(),m("div",xe,[ve,i("div",he,[e(se),e(pe)])]))}},ke=y(ge,[["__scopeId","data-v-7e6361d3"]]);const we={class:"content"},ye={__name:"index",setup(n){let a=w(!1);return(s,d)=>{const _=R,f=N,p=H("router-view"),l=V,x=q;return o(),m("div",null,[e(x,null,{default:t(()=>[e(_,null,{default:t(()=>[e(ke,{collapse:h(a),"onUpdate:collapse":d[0]||(d[0]=r=>U(a)?a.value=r:a=r)},null,8,["collapse"])]),_:1}),e(x,null,{default:t(()=>[e(f,{width:"auto"},{default:t(()=>[e(ae,{collapse:h(a)},null,8,["collapse"])]),_:1}),e(l,null,{default:t(()=>[i("div",we,[e(p,null,{default:t(({Component:r})=>[e(K,{name:"fade"},{default:t(()=>[(o(),u(Q,{max:10},[(o(),u(E(r),{key:s.$route.name}))],1024))]),_:2},1024)]),_:1})])]),_:1})]),_:1})]),_:1})])}}},qe=y(ye,[["__scopeId","data-v-cd3f42e1"]]);export{qe as default};
