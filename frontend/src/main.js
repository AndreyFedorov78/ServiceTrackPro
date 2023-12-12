import { createApp } from 'vue';
import App from './App.vue';
//import MyComponent from './MyComponent.vue'; // Импортируем компонент
//import MyComponent2 from './MyComponent2.vue'; // Импортируем компонент
import { createRouter, createWebHistory } from 'vue-router';
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap/dist/js/bootstrap.bundle';
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'




const app = createApp(App);
app.use(BootstrapVue)
app.use(IconsPlugin)

//import { ButtonGroupPlugin } from 'bootstrap-vue'
//app.use(ButtonGroupPlugin)
//import { NavbarPlugin } from 'bootstrap-vue'
//app.use(NavbarPlugin)



// Optionally install the BootstrapVue icon components plugin




// Регистрируем компонент MyComponent глобально или внутри других компонентов
//app.component('my-component', MyComponent);
//app.component('my-component2', MyComponent2);


const router = createRouter({
  history: createWebHistory(),
  routes: [
 //   { path: '/', component: MyComponent }, // Путь к первой странице
 //   { path: '/second', component: MyComponent2 }, // Путь ко второй странице
  ],
});


app.use(router); // Используем маршрутизатор

app.mount('#app');