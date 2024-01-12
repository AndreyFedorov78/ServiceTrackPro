const url="/api/customers/" // так как тут мы планируем работать с одним API то задем глобальную переменную с путем к API
const url_facility="/api/facility/"
//содзаем объект vue
const customer_orders = new Vue({
    el: "#app", // привязываем объект к области div с id="app"
    delimiters: ["[[", "]]"], // переключаем шаблон с {{}} на [[]] чтобы не путь с python
    data: {
        /* две переменные для временного хранения вводимых данных*/
        edit_id:0,
        edit_title:"",
        facilities: [],
        filter_deleted:true, // скравать уделенные
        filter_title:"",  // строка поиска
        customers: [],
        f_list:[], // список развернутых проектов
        customer: { "id": 0, "name": "", "details": "", "representative": "", "active": true },

    },

    computed: {
        /* отфильтрованный список */
        customers_filtered(){
            // сортировка
            let result = this.customers.sort(function (a, b) {
                return (a.name > b.name) ? 1 : (a.name == b.name) ? 0 : -1
            });
            // скрытие удаленных
            if (this.filter_deleted){
                     result = result.filter((item) => item.active);
            }
            // поиск
            result = result.filter((item) => item.name.toLowerCase().includes(this.filter_title.toLowerCase())  || item.representative.toLowerCase().includes(this.filter_title.toLowerCase()));
            return result;
        },

    },

    methods: {
        facilities_by_customer(customerID){
            let result = this.facilities.filter(item => (item.customer==customerID));
            return result;
        },

        zero (item,n){
            return(zeroPad (item,n))
        },

        async del_item(region){
            region.active = !region.active;
            await this.edit(region);
        },

        async edit(item){
            this.customer = { "id": 0, "name": "", "details": "", "representative": "", "active": true };
            item  = await FetchJsonPUT(url, item);
            console.log(item)
            let flag = 1;
            this.customers.forEach((item_customer, index) => {
                if (item_customer.id==item.id){
                    item_customer=item;
                    flag = 0;
                }
            })
            if (flag) this.customers.push(item);
        },

        async load() {  // пример загрузки из API
            this.customers = await FetchJsonPOST(url,{});
            this.facilities = await FetchJsonPOST(url_facility,{});
        }
    },

async created() { // функция, которая вызывается при старте
        await this.load()
},
})