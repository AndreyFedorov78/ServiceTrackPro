<template>

  <div class="col-sm m-4 shadow p-3 bg-white rounded">

    <form v-if="request" @submit.prevent="updateRequest">
      <div class="form-group" >
        <div>
          Создал: {{ request ? request.created_by.name : "" }} <b class="p-4"></b>
          <b>Аварийная: </b> <input type="checkbox" v-model="request.status"><b class="p-4"></b>
        </div>
        Дата создания:
        <v-calendar v-model="request.request_date" :inputFormat="'dd-MM-yyyy'"></v-calendar>
      </div>

      <div class="form-group">
        <label for="customerRequestNumber">Номер заявки заказчика</label>
        <input type="text" class="form-control" v-model="request.customer_request_number" id="customerRequestNumber">
      </div>
      <div class="form-group">
        <label for="object">Объект</label>
        <v-select v-model="request.object" :options="objects" label="sub_name"/>
      </div>
      <div class="form-group">
        <label for="requestText">Текст заявки</label>
        <textarea class="form-control" v-model="request.request_text" id="requestText" rows="4"></textarea>
      </div>
      <!-- Добавьте остальные поля заявки, которые нужно редактировать -->
      <div class="form-group">
        Дата выполнения:
        <v-calendar v-model="request.completion_date" :inputFormat="'dd-MM-yyyy'"></v-calendar>
      </div>
      <div class="form-group">
        <label>Ответственное лицо</label>
        <v-select v-model="request.responsible" :options="users" label="name"/>
      </div>

      <div class="form-group">
        <label>Номер КП</label><br>
        <input v-model="request.estimate_number" />
      </div>
      <div class="form-group">
        <label>Сумма с НДС</label><br>
        <input v-model="request.amount_with_vat" />
      </div>
      <div class="form-group">
        <label>Простое закрытие </label>  &nbsp;
        <input  type="checkbox" v-model="request.simple_closure"/>
      </div>

      <div class="form-group">
        <label>Номер счета </label><br>
        <input  v-model="request.invoice_number"/>
      </div>
      <div class="form-group">
        Дата оплаты:
        <v-calendar v-model="request.payment_date" :inputFormat="'dd-MM-yyyy'"></v-calendar>
      </div>

      <div class="form-group">
        <label for="notes">Примечания</label>
        <textarea class="form-control" v-model="request.notes" id="notes" rows="4"></textarea>
      </div>
      <!-- Добавьте другие поля заявки -->
      <button type="submit" class="btn btn-primary">Сохранить изменения</button>
    </form>
  </div>


</template>

<script>
import {FetchJsonPUT, FetchJsonGET, convertToDate} from './utils.js';
import VueSelect from 'vue-select';
import 'vue-select/dist/vue-select.css';
import Calendar from 'vue3-datepicker'

// список полей с датами
const dates=['request_date', 'completion_date', 'payment_date']


export default {
  components: {
    'v-select': VueSelect,
    'v-calendar': Calendar,
  },
  data() {
    return {

      id: this.$route.params.id,
      request: null,

      users: [],
      objects: [],
      tmp: null,
    };
  },
  async created() {


    //this.customers = await FetchJsonGET(this.api_path + 'customers/');
    this.users = await FetchJsonGET(this.api_path + 'users/');
    this.objects = await FetchJsonGET(this.api_path + 'objects/');
    this.request = await FetchJsonGET(this.api_path + 'request/' + this.id);
    dates.forEach((item) => {
      this.request[item] = convertToDate(this.request[item]);
    });

    //if (null === this.request.responsible) {
    //  this.request.responsible = this.users[0];
    // }
  },
  methods: {
    async updateRequest() {
      //dates.forEach((item) => {
      //  this.request[item] = formatDate(this.request[item]);
      //});
      await FetchJsonPUT(this.api_path + 'request/' + this.id, this.request);
      window.location.href = "/";
      //dates.forEach((item) => {
      //  this.request[item] = convertToDate(this.request[item]);
      //});
    }

  },
};
</script>

<style>
div {
  padding-bottom: 1em;
}

.vdp-datepicker__calendar {
  background-color: #f0f0f0 !important; /* ваш цвет фона */
  /* другие стили по вашему выбору */
}
</style>
