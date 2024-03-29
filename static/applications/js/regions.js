const url="/api/region/" // так как тут мы планируем работать с одним API то задем глобальную переменную с путем к API

//содзаем объект vue
const customer_orders = new Vue({
    el: "#app", // привязываем объект к области div с id="app"
    delimiters: ["[[", "]]"], // переключаем шаблон с {{}} на [[]] чтобы не путь с python
    data: {
        /* две переменные для временного хранения вводимых данных*/
        edit_id:0,
        edit_title:"",
        filter_deleted:true, // скравать уделенные
        filter_title:"",  // строка поиска
        regions: [],      // массив данных
        region: {        //  переменная для создания нового элемента
            title: "",
            id:0,
            active: true
        }
    },

    computed: {
        /* отфильтрованный список */
        regions_filtered(){
            // сортировка
            let result = this.regions.sort(function (a, b) {
                return (a.title > b.title) ? 1 : (a.title == b.title) ? 0 : -1
            });
            // скрытие удаленных
            if (this.filter_deleted){
                     result = result.filter((item) => item.active);
            }
            // поиск
            result = result.filter((item) => item.title.toLowerCase().includes(this.filter_title.toLowerCase()));
            return result;
        },

    },

    methods: {
        zero (item,n){
            return(zeroPad (item,n))
        },

        async del_item(region){
            region.active = !region.active;
            await this.edit(region);
        },

        async edit(region){
            this.region={title: "", id:0};
            region  = await FetchJsonPUT(url, region);
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
            this.regions = await FetchJsonPOST(url, {});
        }
    },

async created() { // функция, которая вызывается при старте
        await this.load()
},
})