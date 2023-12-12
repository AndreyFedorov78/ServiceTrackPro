
<template>

   <page-header></page-header>


  <div>
    <router-view></router-view>
  </div>
</template>


<style>
/* Глобальные стили для body */
body {

  padding-top: 4em;
  /* Указание пути к вашему изображению в качестве фона */
  background-image: url('@/assets/background1.png');


  /* Подстройка изображения под ширину экрана и повторение по вертикали */
  background-size: 100% auto; /* Подстроить по ширине, высота - авто */
  background-repeat: repeat-y; /* Повторять только по вертикали */

}
</style>


<script>
import {getToken} from './utils.js'
export default {
  mounted() {
    const csrfToken = getToken();
    console.log(csrfToken)
  },



   delimiters: ["[[", "]]"] // Устанавливаем delimiters внутри компонента

};
</script>