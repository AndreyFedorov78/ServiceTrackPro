<template>
  <!-- ваш шаблон для customers-list.vue -->
  <div id="cont" class="col-sm m-4 shadow p-3  bg-white rounded">
  <div class="d-flex justify-content-end mb-3">
    <a class="btn btn-primary main_bg " href="/object/0/">Добавить объект</a>
  </div>

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
      <tr v-for="( object, number) in objects" :key="object.id">
        <th scope="col" class="text-center align-items-center">
          {{ number + 1 }}
        </th>
        <td class="text-left align-middle">
          <a v-on:click="handleDelete(object.id)" href="##">
            <img src="@/assets/icons/del.gif" class="icon">
          </a>
          <a v-bind:href="'/object/'+object.id"> {{ object.name }} </a>
        </td>
        <td class="text-left align-middle">
           {{ object.customer.name }}
        </td>
        <td class="text-left align-middle">
           {{ (object.responsible)?object.responsible.name:"не выбран"}}
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
      objects: [], // переменная для хранения данных о заказчиках
    };
  },
  methods: {
    async load() {


      FetchJsonGET(this.api_path+'objects/')
          .then(data => {
            this.objects = data;
          }).catch(error => {
        console.error('Ошибка при получении данных', error);
      });
    },
    async handleDelete(id) {
      if (confirm('Вы уверены, что хотите удалить этот объект?')) {
        const url = '/api/object/' + id;
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