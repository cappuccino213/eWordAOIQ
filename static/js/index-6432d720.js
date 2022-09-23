import{v as G,l as H,j as r,w as K}from"./element-plus-df419614.js";import{_ as W,l as P}from"./index-66a691da.js";import{u as Y,a as Z,b as ee,c as te,d as le}from"./deductPoint-95fe9152.js";import{r as u,a0 as ae,d as se,w as oe,a4 as x,o as D,c as I,X as a,Q as s,u as d,a as R,F as S,E as $,V as n,ay as re,az as ie}from"./@vue-500f6e4a.js";import"./lodash-es-8e578a42.js";import"./@element-plus-58134fba.js";import"./@popperjs-892fd7f5.js";import"./@ctrl-eb0b847c.js";import"./dayjs-d69067b3.js";import"./axios-805d1980.js";import"./async-validator-efc2d198.js";import"./memoize-one-99e54574.js";import"./escape-html-4bbaf1e1.js";import"./normalize-wheel-es-da779ce4.js";import"./@floating-ui-d1015eb5.js";import"./vue-router-a3c91db2.js";import"./lodash-4ca21166.js";import"./pinia-d75d73cf.js";import"./pinia-plugin-persistedstate-4761f546.js";import"./index-f3494083.js";const ne=[{type:"select",value:"",label:"\u6307\u6807\u7C7B\u578B",prop:"indexType",attrs:{style:{width:"100%"},clearable:!0},children:[{type:"option",value:"dev",label:"\u5F00\u53D1"},{type:"option",value:"test",label:"\u6D4B\u8BD5"}]},{type:"select",value:"",label:"\u6307\u6807\u540D\u79F0",prop:"indexID",attrs:{style:{width:"100%"},clearable:!0},children:[{type:"option",value:"severityBug",label:"\u4E25\u91CD\u7F3A\u9677"},{type:"option",value:"activatedBug",label:"\u6FC0\u6D3B\u7F3A\u9677(dev)"},{type:"option",value:"smokeTest",label:"\u5192\u70DF\u6D4B\u8BD5(dev)"},{type:"option",value:"invalidBug",label:"\u65E0\u6548\u7F3A\u9677(test)"},{type:"option",value:"missingBug",label:"\u9057\u6F0F\u7F3A\u9677(test)"}]}],pe=[{type:"select",value:"",label:"\u6307\u6807\u7C7B\u578B",prop:"indexType",rules:[{required:!0,message:"\u6307\u6807\u7C7B\u578B\u4E0D\u80FD\u4E3A\u7A7A",trigger:"blur"}],attrs:{style:{width:"100%"},disabled:!0},children:[]},{type:"input",value:"",label:"\u6307\u6807\u540D\u79F0",prop:"indexName",rules:[{required:!0,message:"\u6307\u6807\u540D\u79F0\u4E0D\u80FD\u4E3A\u7A7A",trigger:"blur"}],attrs:{clearable:!0}},{type:"select",value:"",label:"\u6307\u6807\u6807\u8BC6",prop:"indexID",rules:[{required:!0,message:"\u6307\u6807ID\u4E0D\u80FD\u4E3A\u7A7A",trigger:"blur"}],attrs:{style:{width:"100%"}},children:[{type:"option",value:"invalidBug",label:"invalidBug"},{type:"option",value:"severityBug",label:"severityBug"},{type:"option",value:"missingBug",label:"missingBug"},{type:"option",value:"activatedBug",label:"activatedBug"},{type:"option",value:"smokeTest",label:"smokeTest"}]},{type:"input",value:"",label:"\u6263\u5206\u8303\u56F4",prop:"scoreInterval",rules:[{required:!0,message:"\u6307\u6807\u6807\u8BC6\u4E0D\u80FD\u4E3A\u7A7A",trigger:"blur"},{pattern:/(\|)/,message:"\u5FC5\u987B\u5305\u542B | ",trigger:"blur"}],attrs:{clearable:!0}},{type:"input",value:"",label:"\u6263\u5206\u89C4\u5219",prop:"rule",rules:[{required:!0,message:"\u89C4\u5219\u4E0D\u80FD\u4E3A\u7A7A",trigger:"blur"},{pattern:/(\|)/,message:"\u5FC5\u987B\u5305\u542B | ",trigger:"blur"}],attrs:{clearable:!0}}],ue=[{type:"select",value:"",label:"\u6307\u6807\u7C7B\u578B",prop:"indexType",rules:[{required:!0,message:"\u6307\u6807\u7C7B\u578B\u4E0D\u80FD\u4E3A\u7A7A",trigger:"blur"}],attrs:{style:{width:"100%"}},children:[{type:"option",value:"dev",label:"dev"},{type:"option",value:"test",label:"test"}]},{type:"input",value:"",label:"\u6307\u6807\u540D\u79F0",prop:"indexName",rules:[{required:!0,message:"\u6307\u6807\u540D\u79F0\u4E0D\u80FD\u4E3A\u7A7A",trigger:"blur"}],attrs:{clearable:!0}},{type:"select",value:"",label:"\u6307\u6807\u6807\u8BC6",prop:"indexID",rules:[{required:!0,message:"\u6307\u6807ID\u4E0D\u80FD\u4E3A\u7A7A",trigger:"blur"}],attrs:{style:{width:"100%"}},children:[{type:"option",value:"invalidBug",label:"invalidBug"},{type:"option",value:"severityBug",label:"severityBug"},{type:"option",value:"missingBug",label:"missingBug"},{type:"option",value:"activatedBug",label:"activatedBug"},{type:"option",value:"smokeTest",label:"smokeTest"}]},{type:"input",value:"",label:"\u6263\u5206\u8303\u56F4",prop:"scoreInterval",rules:[{required:!0,message:"\u6307\u6807\u6807\u8BC6\u4E0D\u80FD\u4E3A\u7A7A",trigger:"blur"},{pattern:/(\|)/,message:"\u5FC5\u987B\u5305\u542B | ",trigger:"blur"}],attrs:{clearable:!0}},{type:"input",value:"",label:"\u6263\u5206\u89C4\u5219",prop:"rule",rules:[{required:!0,message:"\u89C4\u5219\u4E0D\u80FD\u4E3A\u7A7A",trigger:"blur"},{pattern:/(\|)/,message:"\u5FC5\u987B\u5305\u542B | ",trigger:"blur"}],attrs:{clearable:!0}}],de=[{label:"\u6307\u6807\u7C7B\u578B",prop:"indexType",align:"left"},{label:"\u6307\u6807\u540D\u79F0",prop:"indexName",align:"left"},{label:"\u6263\u5206\u8303\u56F4",prop:"scoreInterval",align:"left"},{label:"\u6263\u5206\u89C4\u5219",prop:"rule",align:"left"},{label:"\u64CD\u4F5C",align:"center",action:!0}];const ce=h=>(re("data-v-cac3b048"),h=h(),ie(),h),ve={class:"wrapper targetSetpage-wrapper"},ge=n("\u67E5\u8BE2"),me=n("\u91CD\u7F6E"),be={style:{"padding-left":"2px",margin:"5px 0 10px"}},ye=ce(()=>R("span",{style:{"padding-left":"1px"}},"\u65B0\u589E",-1)),_e=n("\u4FEE\u6539"),fe=n("\u5220\u9664"),he=n("\u4FEE\u6539"),ke=n("\u5220\u9664"),Ce=n("\u53D6\u6D88"),xe=n("\u786E\u5B9A"),Be=n("\u53D6\u6D88"),we=n("\u786E\u5B9A"),De={__name:"index",setup(h){const z=Y(),V=u(null);let c=ae({indexType:"",indexName:"",indexID:""}),T=u([]),v=u(!1),g=u(!1),m=u(pe),F=u(ue),B=u({}),b=u(""),k=u({});se(()=>{y(c),j()}),oe(()=>B.value,e=>{F.value.forEach(t=>{t.value=e[t.prop],k.value[t.prop]=t.value})});const y=e=>{Z(e).then(t=>{T.value=t.data})},j=()=>{switch(P.getCache("dept")){case 3:b.value="dev";break;case 4:b.value="test";break;default:b.value=""}},M=e=>{Object.keys(c).forEach(t=>{c[t]=e.model[t]}),y(c)},U=e=>{e.form.resetFields()},J=()=>{const e=P.getCache("role");e==="td"?m.value[0].value="dev":e==="qd"?m.value[0].value="test":e==="top"&&(m.value[0].children.push({type:"option",value:"dev",label:"dev"},{type:"option",value:"test",label:"test"}),m.value[0].attrs.disabled=!1),v.value=!0},q=e=>{B.value=JSON.parse(JSON.stringify(e.row)),g.value=!0},Q=e=>{const t=e.getFormData();e.validate()(_=>{if(_)if(Object.keys(t).some(f=>k.value[f]!==t[f])){if(t.scoreInterval.split("|").filter(l=>l).length!==t.rule.split("|").filter(l=>l).length){r.error("\u89C4\u5219\u8BBE\u7F6E\u6709\u8BEF");return}let C={...B.value,...e.model};ee(C).then(l=>{l.code===200&&l.status?(r.success("\u6307\u6807\u4FEE\u6539\u6210\u529F"),y(c),z.getRuleList()):(r.error(l.message),N(e)),g.value=!1})}else{r.warning("\u6570\u636E\u672A\u4FEE\u6539");return}else r.error("\u586B\u5199\u6709\u8BEF")})},A=(e,t)=>{t()},O=e=>{K.confirm("\u786E\u5B9A\u8981\u5220\u9664\u6B64\u6761\u6570\u636E\u5417?","\u8B66\u544A",{confirmButtonText:"\u786E\u5B9A",cancelButtonText:"\u53D6\u6D88",type:"warning"}).then(()=>{te({id:e.row.id}).then(t=>{t.code===200&&t.status?(r.success("\u6570\u636E\u5220\u9664\u6210\u529F"),y(c)):r.error(t.message)})}).catch(()=>{r({type:"info",message:"\u5220\u9664\u64CD\u4F5C\u5DF2\u53D6\u6D88"})})},E=(e,t)=>{v.value=!1,g.value=!1,m.value[0].children=[],t!=="update"?e.resetFields():N(e)},N=e=>{Object.keys(k.value).forEach(t=>{e.model[t]=k.value[t]})},L=(e,t)=>{m.value[0].children=[],e.resetFields(),t()},X=e=>{const t=e.getFormData();e.validate()(_=>{if(_){if(t.scoreInterval.split("|").filter(i=>i).length!==t.rule.split("|").filter(i=>i).length){r.error("\u89C4\u5219\u8BBE\u7F6E\u6709\u8BEF");return}le(e.model).then(i=>{i.code===200&&i.status?(r.success(i.message),e.resetFields(),v.value=!1):r.error(i.message)}),y(c)}else r.error("\u9A8C\u8BC1\u5931\u8D25")})};return(e,t)=>{const o=G,_=x("e-form"),w=x("Plus"),i=H,f=x("e-table"),C=x("e-pop-form");return D(),I("div",ve,[a(_,{ref_key:"form",ref:V,options:d(ne)},{action:s(l=>[a(o,{type:"primary",onClick:p=>M(l)},{default:s(()=>[ge]),_:2},1032,["onClick"]),a(o,{onClick:p=>U(l)},{default:s(()=>[me]),_:2},1032,["onClick"])]),_:1},8,["options"]),R("div",be,[a(o,{onClick:J,type:"primary"},{default:s(()=>[a(i,null,{default:s(()=>[a(w)]),_:1}),ye]),_:1})]),a(f,{data:d(T),options:d(de),stripe:""},{action:s(({scope:l})=>[l.row.indexType==d(b)||d(b)===""?(D(),I(S,{key:0},[a(o,{type:"primary",size:"small",onClick:p=>q(l)},{default:s(()=>[_e]),_:2},1032,["onClick"]),a(o,{type:"danger",size:"small",onClick:p=>O(l)},{default:s(()=>[fe]),_:2},1032,["onClick"])],64)):(D(),I(S,{key:1},[a(o,{disabled:"",type:"primary",size:"small",onClick:p=>q(l)},{default:s(()=>[he]),_:2},1032,["onClick"]),a(o,{disabled:"",type:"danger",size:"small",onClick:p=>O(l)},{default:s(()=>[ke]),_:2},1032,["onClick"])],64))]),_:1},8,["data","options"]),a(C,{visible:d(v),"onUpdate:visible":t[0]||(t[0]=l=>$(v)?v.value=l:v=l),options:d(m),title:"\u65B0\u589E\u8003\u6838\u5BA2\u89C2\u6307\u6807",width:"30%",isScroll:"",onPopClose:L},{footer:s(({form:l})=>[a(o,{onClick:p=>E(l)},{default:s(()=>[Ce]),_:2},1032,["onClick"]),a(o,{type:"primary",onClick:p=>X(l)},{default:s(()=>[xe]),_:2},1032,["onClick"])]),_:1},8,["visible","options"]),a(C,{visible:d(g),"onUpdate:visible":t[1]||(t[1]=l=>$(g)?g.value=l:g=l),options:d(F),title:"\u4FEE\u6539\u8003\u6838\u5BA2\u89C2\u6307\u6807",width:"30%",isScroll:"",onPopClose:A},{footer:s(({form:l})=>[a(o,{onClick:p=>E(l,e.id="update")},{default:s(()=>[Be]),_:2},1032,["onClick"]),a(o,{type:"primary",onClick:p=>Q(l)},{default:s(()=>[we]),_:2},1032,["onClick"])]),_:1},8,["visible","options"])])}}},Xe=W(De,[["__scopeId","data-v-cac3b048"]]);export{Xe as default};
