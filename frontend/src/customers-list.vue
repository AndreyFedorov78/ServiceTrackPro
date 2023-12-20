<template>
  <!-- ваш шаблон для customers-list.vue -->
   <div  class="col-sm m-4 shadow p-3  bg-white rounded">
      <a href="/customer/0/"> [добавить заказчика] </a>
     <table class="table table-sm table-bordered">
         <thead>
    <tr>
      <th scope="col" class="text-center main_bg">#</th> <!-- Нумерация -->
      <th scope="col" class="text-left main_bg">Заголовок столбца</th>
      <!-- Другие заголовки столбцов -->
    </tr>
  </thead>
  <tbody>
       <tr v-for="( customer, number) in customers" :key="customer.id">
         <th scope="col" class="text-center">
           {{number}}
         </th>
         <td>
           <a v-bind:href="'/customer/'+customer.id"> {{customer.name}} </a>
         </td>

      </tr>

  </tbody>

     </table>

  </div>
</template>

<script>
//import {FetchJsonPOST} from './utils.js'
import {FetchJsonGET} from './utils.js'
export default {

  data() {
    return {
      customers: [] // переменная для хранения данных о заказчиках
    };
  },
  created() {
    // Метод created вызывается при создании компонента
    // В этом методе можно выполнить запрос для получения данных о заказчиках

    // Например, запрос к API для получения списка заказчиков

    FetchJsonGET('/api/customers/')
      .then(data => {
        this.customers = data; // присваиваем данные переменной customers
      })
      .catch(error => {
        console.error('Ошибка при получении данных о заказчиках:', error);
      });
  }
};
</script>

<style>

/* Ваш стиль */
</style>




<!--template>
  <div id="cont" class="col-sm m-4 shadow p-3  bg-white rounded">

    <center><h1>Пример рабочего поля</h1></center>

  </div>

</template>

<script>
export default {
  name: "customers"
}
</script>

<style-- scoped>

</style-->