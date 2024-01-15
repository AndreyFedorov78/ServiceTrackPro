const url = "/api/customer/" + id // так как тут мы планируем работать с одним API то задем глобальную переменную с путем к API
const url_facility = "/api/facility/"
//содзаем объект vue
const customer_orders = new Vue({
    el: "#app", // привязываем объект к области div с id="app"
    delimiters: ["[[", "]]"], // переключаем шаблон с {{}} на [[]] чтобы не путь с python
    data: {
        /* две переменные для временного хранения вводимых данных*/
        id: id,
        customer: {},
        facilities: [],
        file_: null,
        file: null,

    },

    computed: {
        /* отфильтрованный список */


    },

    methods: {
        handleFileUpload() {
            this.file = this.$refs.file.files[0];
            // console.log(this.file.name)
        },
        async sendFile() {
            let formData = new FormData();
            formData.append('file', this.file);
            FetchFile('/api/file/' + this.id, formData).then(this.load());
        },

        zero(item, n) {
            return (zeroPad(item, n))
        },


        async load() {  // пример загрузки из API
            this.customer = await FetchJsonGET(url);
            this.facilities = await FetchJsonPOST(url_facility, {'id': this.id});
        }
    },

    async created() { // функция, которая вызывается при старте
        await this.load()
    },
})



