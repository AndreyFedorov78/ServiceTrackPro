<template>
  <!-- ваш шаблон для customers-list.vue -->
  <div id="cont" class="col-sm m-4 shadow p-3  bg-white rounded">
  <div class="d-flex justify-content-end mb-3">
    <button class="btn btn-primary main_bg " href="/customer/0/">Добавить заказчика</button>
  </div>
    <table class="table table-sm table-bordered">
      <thead>
      <tr>
        <th scope="col" class="text-center main_bg">#</th> <!-- Нумерация -->
        <th scope="col" class="text-left main_bg">Заказчик</th>
        <!-- Другие заголовки столбцов -->
      </tr>
      </thead>
      <tbody>
      <tr v-for="( customer, number) in customers" :key="customer.id">
        <th scope="col" class="text-center align-items-center">
          {{ number + 1 }}
        </th>
        <td class="text-left align-middle">
          <a v-on:click="handleDelete(customer.id)" href="##">
            <img src="@/assets/icons/del.gif" class="icon">
          </a>
          <a v-bind:href="'/customer/'+customer.id"> {{ customer.name }} </a>
        </td>

      </tr>

      </tbody>

    </table>

  </div>
</template>

<script>
//import {FetchJsonPOST} from './utils.js'
import {FetchJsonDELETE, FetchJsonGET} from './utils.js'

export default {

  data() {
    return {
      customers: [] // переменная для хранения данных о заказчиках
    };
  },
  methods: {
    async load() {
      FetchJsonGET('/api/customers/')
          .then(data => {
            this.customers = data; // присваиваем данные переменной customers
          }).catch(error => {
        console.error('Ошибка при получении данных', error);
      });
    },
    async handleDelete(id) {
      if (confirm('Вы уверены, что хотите удалить этого заказчика?')) {
        const url = '/api/customer/' + id;
        await FetchJsonDELETE(url);
        await this.load();
      }
    },


  },
  created() {
    this.load();
  }
};
</script>

<style>
.icon {
  height: 1em;
  padding-right: .5em;
}

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