
//содзаем объект vue
const customer_orders = new Vue({
    el: "#app", // привязываем объект к области div с id="app"
    delimiters: ["[[", "]]"], // переключаем шаблон с {{}} на [[]] чтобы не путь с python
    data: {  // тут будут наши переменные которые мы будем использовать в шаблоне
             // в них будем грузить данные по API
        edit_id:0,
        edit_title:"",
        filter_title:"",
        regions: [],
        region: {
            title: "",
            id:0
        }

    },

    computed: { // тут будут вычисляемые поля
        regions_filtered(){
            let result = this.regions.sort(function (a, b) {
                return (a.title > b.title) ? 1 : (a.title == b.title) ? 0 : -1
            });
            result = result.filter((item) => item.title.toLowerCase().includes(this.filter_title.toLowerCase()));
            return result;
        },

    },
    filter: { // тут будут фильтры вывода переменных

    },
    methods: { // методы (функции) объекта
        async edit(region){
            this.region={title: "", id:0};
            if (region.id==0) region.id=parseInt(Math.random()*100)
            let flag = 1;
            this.regions.forEach((item, index) => {
                if (item.id==region.id){
                    item.title=region.title;
                    flag = 0;
                }
            })
            if (flag) this.regions.push(region);

        },


        async load() {  // пример загрузки из API
            const url = "/sp/API/XXXXXX/";
            const request_data = {request_dat: 'somthing'}
        //    this.example_data_array = await FetchJsonPOST(url, request_data);
        }
    },

async created() { // функция, которая вызывается при старте
        await this.load()
},
})