import{e as t}from"./index-f3494083.js";function a(e){return t.post({url:"/api/TestTaskList/list",data:e})}function r(e){return t.post({url:"/api/SmokeTestRecord/add",data:e})}function s(e){return t.post({url:"/api/SmokeTestRecord/AddBatch",data:e})}function d(e){return t.post({url:"/api/SmokeTestRecord/list",data:e})}function u(e){return t.put({url:"/api/SmokeTestRecord/update",data:e})}function c(e){return t.delete({url:"/api/SmokeTestRecord/delete",params:e})}export{r as a,s as b,d as c,c as d,a as s,u};