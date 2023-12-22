(function(){"use strict";var t={815:function(t,e,n){var r=n(963),o=n(252);function a(t,e,n,r,a,s){const i=(0,o.up)("page-header"),c=(0,o.up)("router-view");return(0,o.wg)(),(0,o.iD)(o.HY,null,[(0,o.Wm)(i),(0,o._)("div",null,[(0,o.Wm)(c)])],64)}function s(t){const e=t+"=",n=document.cookie.split(";");for(let r=0;r<n.length;r++){let t=n[r];while(" "===t.charAt(0))t=t.substring(1);if(0===t.indexOf(e))return decodeURIComponent(t.substring(e.length,t.length))}return null}function i(){return s("csrftoken")}async function c(t,e,n){const r={"Content-Type":"application/json",charset:"utf-8","X-CSRFToken":i()};try{let o={};o="GET"==e?{method:e,headers:r}:{method:e,headers:r,body:JSON.stringify(n)};const a=await fetch(t,o);if(a.ok){const t=await a.json();return t}return null}catch(o){return null}}async function l(t){return await c(t,"GET",null)}async function u(t,e){return await c(t,"DELETE",e)}async function d(t,e){return await c(t,"PUT",e)}var m={mounted(){const t=i();console.log(t)},delimiters:["[[","]]"]},p=n(744);const f=(0,p.Z)(m,[["render",a]]);var h=f,v=n.p+"img/ServiceTrack.b05de798.gif";const b={class:"navbar navbar-expand-lg navbar-light bg-light fixed-top"},g=(0,o._)("div",{class:"container-fluid"},[(0,o._)("img",{class:"logo",src:v,alt:"ServiceTrack"}),(0,o._)("div",{style:{width:"10em"},id:"navbarSupportedContent"},[(0,o._)("ul",{class:"navbar-nav me-auto mb-2 mb-lg-0"},[(0,o._)("li",{class:"nav-item dropdown"},[(0,o._)("a",{class:"nav-link dropdown-toggle",href:"#",id:"navbarDropdown",role:"button","data-bs-toggle":"dropdown","aria-expanded":"false"}," Меню "),(0,o._)("ul",{class:"dropdown-menu","aria-labelledby":"navbarDropdown"},[(0,o._)("li",null,[(0,o._)("a",{class:"dropdown-item",href:"/customers/"},"Заказчики")]),(0,o._)("li",null,[(0,o._)("hr",{class:"dropdown-divider"})]),(0,o._)("li",null,[(0,o._)("a",{class:"dropdown-item",href:"/admin/"},"Админка")])])])])])],-1),w=[g];function _(t,e){return(0,o.wg)(),(0,o.iD)("nav",b,w)}const y={},x=(0,p.Z)(y,[["render",_]]);var k=x;const O={id:"cont",class:"col-sm m-4 mt-6 shadow p-3 bg-white rounded"},D=(0,o._)("h1",null,"Пример рабочего поля",-1);function C(t,e,n,r,a,s){const i=(0,o.up)("center");return(0,o.wg)(),(0,o.iD)("div",O,[(0,o.Wm)(i,null,{default:(0,o.w5)((()=>[D])),_:1})])}var T={name:"index-page"};const j=(0,p.Z)(T,[["render",C]]);var E=j,S=n(577),Z=n.p+"img/del.c55638c3.gif";const U={id:"cont",class:"col-sm m-4 shadow p-3 bg-white rounded"},P=(0,o._)("div",{class:"d-flex justify-content-end mb-3"},[(0,o._)("button",{class:"btn btn-primary main_bg",href:"/customer/0/"},"Добавить заказчика")],-1),V={class:"table table-sm table-bordered"},W=(0,o._)("thead",null,[(0,o._)("tr",null,[(0,o._)("th",{scope:"col",class:"text-center main_bg"},"#"),(0,o._)("th",{scope:"col",class:"text-left main_bg"},"Заказчик")])],-1),z={scope:"col",class:"text-center align-items-center"},A={class:"text-left align-middle"},F=["onClick"],G=(0,o._)("img",{src:Z,class:"icon"},null,-1),H=[G],R=["href"];function Y(t,e,n,r,a,s){return(0,o.wg)(),(0,o.iD)("div",U,[P,(0,o._)("table",V,[W,(0,o._)("tbody",null,[((0,o.wg)(!0),(0,o.iD)(o.HY,null,(0,o.Ko)(a.customers,((t,e)=>((0,o.wg)(),(0,o.iD)("tr",{key:t.id},[(0,o._)("th",z,(0,S.zw)(e+1),1),(0,o._)("td",A,[(0,o._)("a",{onClick:e=>s.handleDelete(t.id),href:"##"},H,8,F),(0,o._)("a",{href:"/customer/"+t.id},(0,S.zw)(t.name),9,R)])])))),128))])])])}var I={data(){return{customers:[]}},methods:{async load(){l("/api/customers/").then((t=>{this.customers=t})).catch((t=>{console.error("Ошибка при получении данных",t)}))},async handleDelete(t){if(confirm("Вы уверены, что хотите удалить этого заказчика?")){const e="/api/customer/"+t;await u(e),await this.load()}}},created(){this.load()}};const J=(0,p.Z)(I,[["render",Y]]);var K=J;const L={class:"col-sm m-4 shadow p-3 bg-white rounded"},M={class:"form-group"},N=(0,o._)("label",{for:"name"},"Наименование",-1),X={class:"form-group"},$=(0,o._)("label",{for:"details"},"Реквизиты",-1),q={class:"form-group"},B=(0,o._)("label",{for:"representative"},"Ответственное лицо",-1),Q=(0,o._)("button",{type:"submit",class:"btn btn-primary"},"Сохранить изменения",-1);function tt(t,e,n,a,s,i){return(0,o.wg)(),(0,o.iD)("div",L,[(0,o._)("form",{onSubmit:e[3]||(e[3]=(0,r.iM)(((...t)=>i.updateCustomer&&i.updateCustomer(...t)),["prevent"]))},[(0,o._)("div",M,[N,(0,o.wy)((0,o._)("input",{type:"text",class:"form-control","onUpdate:modelValue":e[0]||(e[0]=t=>s.customer.name=t),id:"name"},null,512),[[r.nr,s.customer.name]])]),(0,o._)("div",X,[$,(0,o.wy)((0,o._)("textarea",{class:"form-control","onUpdate:modelValue":e[1]||(e[1]=t=>s.customer.details=t),id:"details",rows:"4"},null,512),[[r.nr,s.customer.details]])]),(0,o._)("div",q,[B,(0,o.wy)((0,o._)("input",{type:"text",class:"form-control","onUpdate:modelValue":e[2]||(e[2]=t=>s.customer.representative=t),id:"representative"},null,512),[[r.nr,s.customer.representative]])]),Q],32)])}var et={data(){return{id:this.$route.params.id,customer:{}}},created(){l("/api/customer/"+this.id).then((t=>{this.customer=t})).catch((t=>{console.error("Ошибка при получении данных о заказчиках:",t)}))},methods:{updateCustomer(){d("/api/customer/"+this.id,this.customer).then((t=>{this.customer=t,this.id=t.id,window.location.href="/customers"})).catch((t=>{console.error("Ошибка при обновлении данных о заказчике:",t)}))}}};const nt=(0,p.Z)(et,[["render",tt]]);var rt=nt;function ot(t,e,n,r,a,s){return(0,o.wg)(),(0,o.iD)("h1",null,"Такой страницы нет!")}var at={name:"page-not-found"};const st=(0,p.Z)(at,[["render",ot]]);var it=st,ct=n(201);n(39);const lt=(0,r.ri)(h);lt.component("page-header",k);const ut=(0,ct.p7)({history:(0,ct.PO)(),routes:[{path:"/",component:E},{path:"/customers/",component:K},{path:"/customer/:id",component:rt,props:!0},{path:"/:catchAll(.*)",component:it}]});lt.use(ut),lt.mount("#app")}},e={};function n(r){var o=e[r];if(void 0!==o)return o.exports;var a=e[r]={exports:{}};return t[r].call(a.exports,a,a.exports,n),a.exports}n.m=t,function(){var t=[];n.O=function(e,r,o,a){if(!r){var s=1/0;for(u=0;u<t.length;u++){r=t[u][0],o=t[u][1],a=t[u][2];for(var i=!0,c=0;c<r.length;c++)(!1&a||s>=a)&&Object.keys(n.O).every((function(t){return n.O[t](r[c])}))?r.splice(c--,1):(i=!1,a<s&&(s=a));if(i){t.splice(u--,1);var l=o();void 0!==l&&(e=l)}}return e}a=a||0;for(var u=t.length;u>0&&t[u-1][2]>a;u--)t[u]=t[u-1];t[u]=[r,o,a]}}(),function(){n.d=function(t,e){for(var r in e)n.o(e,r)&&!n.o(t,r)&&Object.defineProperty(t,r,{enumerable:!0,get:e[r]})}}(),function(){n.g=function(){if("object"===typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(t){if("object"===typeof window)return window}}()}(),function(){n.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)}}(),function(){n.p="/static/"}(),function(){var t={143:0};n.O.j=function(e){return 0===t[e]};var e=function(e,r){var o,a,s=r[0],i=r[1],c=r[2],l=0;if(s.some((function(e){return 0!==t[e]}))){for(o in i)n.o(i,o)&&(n.m[o]=i[o]);if(c)var u=c(n)}for(e&&e(r);l<s.length;l++)a=s[l],n.o(t,a)&&t[a]&&t[a][0](),t[a]=0;return n.O(u)},r=self["webpackChunkfrontend"]=self["webpackChunkfrontend"]||[];r.forEach(e.bind(null,0)),r.push=e.bind(null,r.push.bind(r))}();var r=n.O(void 0,[998],(function(){return n(815)}));r=n.O(r)})();
//# sourceMappingURL=app.7dbbec0f.js.map