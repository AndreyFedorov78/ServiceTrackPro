<template>
  <!-- ваш шаблон для customers-list.vue -->
  <div id="cont" class="col-sm m-4 shadow p-3  bg-white rounded">
  <div class="d-flex justify-content-end mb-3">
    <a class="btn btn-primary main_bg " href="/request/0/">Добавить заявку</a>
  </div>

    {{ requests }}

    <table class="table table-sm table-bordered">
      <thead>
      <tr>
        <th scope="col" class="text-center main_bg">#</th> <!-- Нумерация -->
        <th scope="col" class="text-left main_bg">Объект</th>
        <th scope="col" class="text-left main_bg">Заказчик</th>
        <th scope="col" class="text-left main_bg">Ответсвтенный</th>
        <!-- Другие заголовки столбцов -->
      </tr>
      </thead>
      <tbody>
      <tr v-for="( request, number) in requests" :key="request.id" >
        <th scope="col" class="text-center align-items-center"
          :class="{'text-danger': request.status}">
          {{ number + 1 }}
        </th>

        <td class="text-left align-middle"
            :class="{'text-danger': request.status}">
          {{ zeroPad(request.id,8) }}
        </td>
        <td class="text-left align-middle "
            :class="{'text-danger': request.status}">
          {{ formatDate(request.request_date)  }}
        </td>

        <td class="text-left align-middle"
            :class="{'text-danger': request.status}">
          <a v-on:click="handleDelete(request.id)" href="##">
            <img src="@/assets/icons/del.gif" class="icon">
          </a>
          <a v-bind:href="'/request/'+request.id"
             :class="{'text-danger': request.status}"> {{ request.request_text }} </a>
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
      requests: [], // переменная для хранения данных о заказчиках
    };
  },
  methods: {
    async load() {
      FetchJsonGET(this.api_path+'requests/')
          .then(data => {
            this.requests = data;
          }).catch(error => {
        console.error('Ошибка при получении данных', error);
      });
    },
    async handleDelete(id) {
      if (confirm('Вы уверены, что хотите удалить этот объект?')) {
        const url = '/api/request/' + id;
        await FetchJsonDELETE(url);
        await this.load();
      }
    },
    formatDate(value) {
      if (!value) return "";
      const date = new Date(value);
      const day = String(date.getDate()).padStart(2, "0");
      const month = String(date.getMonth() + 1).padStart(2, "0");
      const year = date.getFullYear();
      return `${day}/${month}/${year}`;
    },
    zeroPad(value, n) {
      let str = '' + value;
      while (str.length < n) {
        str = '0' + str;
      }
      return str;
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


