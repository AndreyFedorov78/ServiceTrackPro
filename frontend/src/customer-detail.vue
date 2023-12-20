<template>
  <div class="col-sm m-4 shadow p-3 bg-white rounded">
    <form @submit.prevent="updateCustomer">
      <div class="form-group">
        <label for="name">Наименование</label>
        <input type="text" class="form-control" v-model="customer.name" id="name">
      </div>
      <div class="form-group">
        <label for="details">Реквизиты</label>
        <textarea class="form-control" v-model="customer.details" id="details" rows="4"></textarea>
      </div>
      <div class="form-group">
        <label for="representative">Ответственное лицо</label>
        <input type="text" class="form-control" v-model="customer.representative" id="representative">
      </div>
      <button type="submit" class="btn btn-primary">Сохранить изменения</button>
    </form>
  </div>
</template>


<script>
import { FetchJsonPUT } from './utils.js';
import { FetchJsonGET } from './utils.js';

export default {
  data() {
    return {
      id: this.$route.params.id,
      customer: {} // Переменная для хранения данных о заказчиках
    };
  },
  created() {
    // Метод created вызывается при создании компонента
    // В этом методе можно выполнить запрос для получения данных о заказчиках

    // Например, запрос к API для получения информации о заказчике
    FetchJsonGET('/api/customer/' + this.id)
      .then(data => {
        this.customer = data; // присваиваем данные переменной customer
      })
      .catch(error => {
        console.error('Ошибка при получении данных о заказчиках:', error);
      });
  },
  methods: {
    updateCustomer() {
      // Отправка отредактированных данных о заказчике на бэкэнд

      FetchJsonPUT('/api/customer/' + this.id, this.customer)
        .then(data => {
        this.customer = data; // присваиваем данные переменной customer
        this.id = data.id;
        window.location.href = "/customers";
      })
        .catch(error => {
          console.error('Ошибка при обновлении данных о заказчике:', error);
        });
    }
  }
};
</script>

<style>
/* Ваш стиль */
</style>
