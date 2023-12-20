import {createApp} from 'vue';
import App from './App.vue';
import PageHeader from './page-header.vue';
import IndexPage from './index-page.vue';
import Customers from './customers-list.vue';
import CustomerDetail from './customer-detail.vue';
import NotFoundComponent from './page-not-found';

import {createRouter, createWebHistory} from 'vue-router';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.bundle';




const app = createApp(App);
// Регистрируем компоненты
app.component('page-header', PageHeader);


const router = createRouter({
    history: createWebHistory(),
    routes: [
        {path: '/', component: IndexPage}, // index.html
        {path: '/customers/', component: Customers},
        { path: '/customer/:id', component: CustomerDetail, props: true }, // Добавление пути с динамическим параметром :id
        {path: '/:catchAll(.*)', component: NotFoundComponent}, // Компонент для отображения ошибки 404
    ],
});

app.use(router); // Используем маршрутизатор
app.mount('#app');