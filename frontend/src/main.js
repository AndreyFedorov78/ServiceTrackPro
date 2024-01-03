import {createApp} from 'vue';
import App from './App.vue';
import PageHeader from './page-header.vue';
import RequestList from './requests-list.vue';
//import IndexPage from './index-page.vue';
import Customers from './customers-list.vue';
import Objects from './objects-list.vue';
import CustomerDetail from './customer-detail.vue';
import ObjectDetail from './object-detail.vue';
import NotFoundComponent from './page-not-found';

import {createRouter, createWebHistory} from 'vue-router';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.bundle';





const app = createApp(App);
// Регистрируем компоненты
app.component('page-header', PageHeader);

app.config.globalProperties.api_path = process.env.VUE_APP_API_PATH;  // путь к API



const router = createRouter({
    history: createWebHistory(),
    routes: [
        {path: '/', component: RequestList}, // index.html
        {path: '/customers/', component: Customers},
        {path: '/customer/:id', component: CustomerDetail, props: true},
        {path: '/objects/', component: Objects, props: true},
        {path: '/object/:id', component: ObjectDetail, props: true},
        {path: '/:catchAll(.*)', component: NotFoundComponent}, // Компонент для отображения ошибки 404
    ],
});

app.use(router); // Используем маршрутизатор
app.mount('#app');