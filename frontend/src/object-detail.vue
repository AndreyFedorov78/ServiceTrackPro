<template>
  <div class="col-sm m-4 shadow p-3 bg-white rounded">

    <form v-if="object" @submit.prevent="updateObject">
      <div class="form-group">
        <label for="name">Название объекта</label>
        <input type="text" class="form-control" v-model="object.name" id="name">
      </div>
      <div class="form-group">
        <label for="address">Адрес объекта</label>
        <textarea class="form-control" v-model="object.address" id="address" rows="4"></textarea>
      </div>

      <div class="form-group">
        <label>Заказчик </label>
        <v-select
                  v-model="object.customer"
                  :options="customers"
                  label="name"/>

      </div>

      <div class="form-group">


        <label >Ответственное лицо </label>
        <v-select
            v-model=" object.responsible "
            :options="users"
            label="name"/>
      </div>
      <button type="submit" class="btn btn-primary">Сохранить изменения</button>
    </form>
  </div>
</template>


<script>
import {FetchJsonPUT} from './utils.js';
import {FetchJsonGET} from './utils.js';
import VueSelect from 'vue-select';
import 'vue-select/dist/vue-select.css';


export default {
  components: {
    'v-select': VueSelect,
  },
  data() {
    return {
      selectedCustomer: 1,
      id: this.$route.params.id,
      object: null, // Переменная для хранения данных о заказчиках
      customers: [],
      users:[]
    };
  },
  async created() {
    this.customers = await FetchJsonGET(this.api_path + 'customers/');
    this.users = await FetchJsonGET(this.api_path + 'users/');
    this.object = await FetchJsonGET(this.api_path + 'object/' + this.id);
    if (null === this.object.responsible) {
      this.object.responsible=this.users[0];
    }
  },
  methods: {
    async updateObject() {
      // Отправка отредактированных данных об объекте на бэкэнд

      await FetchJsonPUT(this.api_path +'object/' + this.id, this.object)
      window.location.href = "/objects";

    }
  },




};
</script>

<style>

div {
  padding-bottom: 1em;
}

</style>
