import{v as P,x as X,y as Z,A as G}from"./element-plus-df419614.js";import{u as K}from"./loggedInfo-268f6dc2.js";import{_ as L}from"./index-66a691da.js";import{r as f,w as V,d as j,a4 as E,o as T,c as B,X as g,Q as d,a as b,W as D,u,F as z,V as O,a0 as ee,s as te,P as M,T as S,a7 as ae}from"./@vue-500f6e4a.js";import{d as $}from"./dayjs-d69067b3.js";import{g as ne,u as oe}from"./dateChange-eb10ac1f.js";import{m as se,d as re}from"./index-771e9942.js";import{u as le}from"./cellMouseEnter-f72a73da.js";import{u as ce}from"./deductScore-d679635c.js";import{u as ie}from"./initFormData-b064dc9f.js";import"./lodash-es-8e578a42.js";import"./@element-plus-58134fba.js";import"./@popperjs-892fd7f5.js";import"./@ctrl-eb0b847c.js";import"./async-validator-efc2d198.js";import"./memoize-one-99e54574.js";import"./escape-html-4bbaf1e1.js";import"./normalize-wheel-es-da779ce4.js";import"./@floating-ui-d1015eb5.js";import"./pinia-d75d73cf.js";import"./index-f3494083.js";import"./axios-805d1980.js";import"./vue-router-a3c91db2.js";import"./lodash-4ca21166.js";import"./pinia-plugin-persistedstate-4761f546.js";const ue=[{label:"\u7985\u9053ID",prop:"ztId",align:"center",slot:"ztId"},{label:"\u7F3A\u9677\u7B49\u7EA7",prop:"severity",align:"center",sortable:!0},{label:"\u7F3A\u9677\u6807\u9898",prop:"title",align:"center",showOverflowTooltip:!0},{label:"\u6240\u5C5E\u9879\u76EE",prop:"projectId",align:"center",sortable:!0,showOverflowTooltip:!0},{label:"\u521B\u5EFA\u4EBA",prop:"openedBy",align:"center"},{label:"\u521B\u5EFA\u65E5\u671F",prop:"openedDate",align:"center",sortable:!0},{label:"\u89E3\u51B3\u4EBA",prop:"resolvedBy",align:"center"}];const de=O("\u8FD4\u56DE"),pe=["onClick"],me={__name:"index",props:{detailTableData:{type:Object,default:{}}},emits:["backClick"],setup(a,{expose:e,emit:s}){const c=a,r=K();let _=f([]);V(()=>c.detailTableData,n=>{_.value=n}),j(()=>{C()});const C=()=>{let n=JSON.parse(JSON.stringify(c.detailTableData));n.forEach(o=>{for(let t=0;t<r.userList.length;t++)o.openedBy===r.userList[t].account&&(o.openedBy=r.userList[t].realname),o.resolvedBy===r.userList[t].account&&(o.resolvedBy=r.userList[t].realname);for(let t=0;t<r.prjectList.length;t++)o.projectId===r.prjectList[t].id&&(o.projectId=r.prjectList[t].name)}),console.log(n),_.value=n},k=()=>{s("backClick")},H=n=>{window.open(n)};return e({getTableData:C}),(n,o)=>{const t=P,v=E("e-table");return T(),B(z,null,[g(t,{type:"primary",plain:"",onClick:k,size:"small",style:{"margin-bottom":"10px"}},{default:d(()=>[de]),_:1}),b("div",null,[g(v,{options:u(ue),data:u(_),stripe:"",border:""},{ztId:d(({scope:l})=>[b("div",{class:"ztId",onClick:p=>H(l.row.accessLink)},D(l.row.ztId),9,pe)]),_:1},8,["options","data"])])],64)}}},_e=L(me,[["__scopeId","data-v-72d2e563"]]),ve=[{type:"select",value:[],label:"\u59D3\u540D",prop:"devName",attrs:{style:{width:"100%"},multiple:!0,collapseTags:!0},rules:[{required:!0,message:"\u59D3\u540D\u4E0D\u80FD\u4E3A\u7A7A",trigger:"blur"}],children:[],multiple:!0},{type:"date-picker",value:[$(new Date(ne()).setHours(0,0,0)).format("YYYY-MM-DD HH:mm:ss"),$(new Date().setHours(23,59,59)).format("YYYY-MM-DD HH:mm:ss")],label:"\u65F6\u95F4",prop:"dateRange",rules:[{required:!0,message:"\u65E5\u671F\u9009\u62E9\u4E0D\u80FD\u4E3A\u7A7A",trigger:"blur"}],attrs:{style:{width:"100%"},multiple:!0,collapseTags:!0,type:"daterange",rangeSeparator:"\u81F3",startPlaceholder:"\u5F00\u59CB\u65E5\u671F",endPlaceholder:"\u7ED3\u675F\u65E5\u671F",format:"YYYY-MM-DD",valueFormat:"YYYY-MM-DD HH:mm:ss",shortcuts:[{text:"\u4ECA\u5929",value:()=>{const a=new Date().setHours(0,0,0),e=new Date().setHours(23,59,59);return[a,e]}},{text:"\u4E00\u5468\u5185",value:()=>{const a=new Date().setHours(23,59,59),e=new Date().setTime(new Date().getTime()-3600*1e3*24*7);return[new Date(e).setHours(0,0,0),a]}},{text:"\u4E00\u6708\u5185",value:()=>{const a=new Date().setHours(23,59,59),e=new Date().setTime(new Date().getTime()-3600*1e3*24*30);return[new Date(e).setHours(0,0,0),a]}},{text:"\u534A\u5E74\u5185",value:()=>{const a=new Date().setHours(23,59,59),e=new Date().setTime(new Date().getTime()-3600*1e3*24*182);return[new Date(e).setHours(0,0,0),a]}},{text:"\u4E00\u5E74\u5185",value:()=>{const a=new Date().setHours(23,59,59),e=new Date().setTime(new Date().getTime()-3600*1e3*24*365);return[new Date(e).setHours(0,0,0),a]}},{text:"\u7B2C\u4E00\u5B63\u5EA6",value:()=>{var a=new Date,e=a.getFullYear();const s=new Date(e,0,1).setHours(0,0,0),c=new Date(e,2,31).setHours(23,59,59);return[s,c]}},{text:"\u7B2C\u4E8C\u5B63\u5EA6",value:()=>{var a=new Date,e=a.getFullYear();const s=new Date(e,3,1).setHours(0,0,0),c=new Date(e,5,30).setHours(23,59,59);return[s,c]}},{text:"\u7B2C\u4E09\u5B63\u5EA6",value:()=>{var a=new Date,e=a.getFullYear();const s=new Date(e,6,1).setHours(0,0,0),c=new Date(e,8,30).setHours(23,59,59);return[s,c]}},{text:"\u7B2C\u56DB\u5B63\u5EA6",value:()=>{var a=new Date,e=a.getFullYear();const s=new Date(e,9,1).setHours(0,0,0),c=new Date(e,11,31).setHours(23,59,59);return[s,c]}}]}}],ge=[{label:"\u59D3\u540D",prop:"devName",align:"center"},{label:"\u9057\u6F0F\u603B\u6570",prop:"missingBugCount",align:"center",sortable:!0,slot:"missingBugCount"},{label:"\u6263\u5206\u6570",prop:"deductPoint",align:"center",sortable:!0,slot:"deductPoint"}];const De={class:"wrapper targetSetpage-wrapper"},be=O("\u67E5\u8BE2"),fe=O("\u91CD\u7F6E"),we=["onClick"],he={class:"deRule"},ye={class:"ruleRange"},Te={class:"result"},Ce={class:"deductPoint"},ke={__name:"index",emits:["addTab"],setup(a,{emit:e}){const[s,c,r]=oe(),[_,C]=le("missingBugCount"),[k,H,n,o]=ce(),t=ie(),v=f(null);let l=f(ve),p=ee({devName:[],openedBeginDate:"",openedEndDate:""}),I=f([]),N=f([]);V(()=>_.value,i=>{o("devMissingBug",i)}),j(()=>{t(l.value),R(p),o("devMissingBug",_.value)});const R=i=>{const m=l.value[0].children;se(i).then(w=>{const h=w.data;h&&h.length&&(I.value=h.map(y=>{for(let Y of m)y.devName===Y.value&&(y.account=y.devName,y.devName=Y.label);return y}))})},q=async i=>{await re(i).then(m=>{m.data&&(N.value=m.data)})},J=i=>{const m=i.model,w=i.model.dateRange;i.form.validate(h=>{h&&(p.devName=m.devName,p.openedBeginDate=s.value||w[0],p.openedEndDate=c.value||w[1],R(p))})},A=i=>{s.value="",c.value="",t(l.value),I.value=[]},Q=i=>{},U=i=>{r(i)},W=async i=>{N.value=[];let m=JSON.parse(JSON.stringify(p));m.devName=i,await q(m),e("addTab",N.value)};return(i,m)=>{const w=P,h=E("e-form"),y=X,Y=E("e-table");return T(),B("div",De,[g(h,{ref_key:"form",ref:v,options:u(l),onVisibleChange:Q,onDateChange:U},{action:d(x=>[g(w,{type:"primary",onClick:F=>J(x)},{default:d(()=>[be]),_:2},1032,["onClick"]),g(w,{onClick:F=>A()},{default:d(()=>[fe]),_:2},1032,["onClick"])]),_:1},8,["options"]),g(Y,{options:u(ge),data:u(I),stripe:"",border:"",onCellMouseEnter:u(C)},{missingBugCount:d(({scope:x})=>[b("div",{class:"bugCount",onClick:F=>W(x.row.account)},D(x.row.missingBugCount),9,we)]),deductPoint:d(({scope:x})=>[g(y,{placement:"top","hide-after":150},{content:d(()=>[b("div",null,[b("div",he,"\u6263\u5206\u89C4\u5219\uFF1A"+D(u(k).rule),1),b("div",ye," \u6263\u5206\u8303\u56F4\uFF1A"+D(u(k).scoreInterval),1),b("div",Te," \u5F53\u524D\u8003\u6838\u6307\u6807 "+D(u(_))+" \u5728"+D(u(H))+"\u8303\u56F4\uFF0C\u6545\u6263"+D(u(n))+"\u5206 ",1)])]),default:d(()=>[b("div",Ce,D(x.row.deductPoint),1)]),_:2},1024)]),_:1},8,["options","data","onCellMouseEnter"])])}}},xe=L(ke,[["__scopeId","data-v-46532d07"]]);const He={class:"wrapper"},Ye={__name:"index",setup(a){const e=te([]);let s=f([]);const c=f(null),r=f("\u7EDF\u8BA1\u9875"),_=n=>{if(s.value=n,console.log(n),e.value.length)r.value="\u8BE6\u60C5\u9875";else{const o="\u8BE6\u60C5\u9875";e.value.push({content:_e,name:"\u8BE6\u60C5\u9875",title:"\u8BE6\u60C5\u9875"}),r.value=o}},C=n=>{const o=e.value;let t=r.value;t===n&&o.forEach((v,l)=>{if(v.name===n){const p=o[l+1]||o[l-1];p&&(t=p.name)}}),r.value="\u7EDF\u8BA1\u9875",e.value=o.filter(v=>v.name!==n)},k=()=>{r.value="\u7EDF\u8BA1\u9875"},H=n=>{n==="\u8BE6\u60C5\u9875"&&c.value[0].getTableData()};return(n,o)=>{const t=Z,v=G;return T(),B("div",He,[g(v,{modelValue:r.value,"onUpdate:modelValue":o[0]||(o[0]=l=>r.value=l),type:"card",class:"demo-tabs",onTabRemove:C,onTabChange:H},{default:d(()=>[g(t,{label:"\u7EDF\u8BA1\u9875",name:"\u7EDF\u8BA1\u9875"},{default:d(()=>[(T(),M(S(u(xe)),{onAddTab:_},null,32))]),_:1}),(T(!0),B(z,null,ae(u(e),l=>(T(),M(t,{key:l.name,label:l.title,name:l.name,closable:""},{default:d(()=>[(T(),M(S(l.content),{onBackClick:k,detailTableData:u(s),ref_for:!0,ref_key:"detailRef",ref:c},null,40,["detailTableData"]))]),_:2},1032,["label","name"]))),128))]),_:1},8,["modelValue"])])}}},et=L(Ye,[["__scopeId","data-v-e299f1d8"]]);export{et as default};
