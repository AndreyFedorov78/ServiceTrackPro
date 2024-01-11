
//содзаем объект vue
const customer_orders = new Vue({
    el: "#app", // привязываем объект к области div с id="app"
    delimiters: ["[[", "]]"], // переключаем шаблон с {{}} на [[]] чтобы не путь с python
    data: {  // тут будут наши переменные которые мы будем использовать в шаблоне
             // в них будем грузить данные по API
        example_data_array: [],
        some_other_var: 1,
    },

    computed: { // тут будут вычисляемые поля

    },
    filter: { // тут будут фильтры вывода переменных

    },
    methods: { // методы (функции) объекта

        async load() {  // пример загрузки из API
            const url = "/sp/API/XXXXXX/";
            const request_data = {request_dat: 'somthing'}
            this.example_data_array = await FetchJsonPOST(url, request_data);
        }
    },

async created() { // функция, которая вызывается при старте
        await this.load()
},
})