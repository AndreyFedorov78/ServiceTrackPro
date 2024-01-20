const url = "/api/customer/" + id // так как тут мы планируем работать с одним API то задем глобальную переменную с путем к API
const url_facility = "/api/facility/"

new Vue({
    el: "#app", // привязываем объект к области div с id="app"
    delimiters: ["[[", "]]"], // переключаем шаблон с {{}} на [[]] чтобы не путь с python
    data: {
        id: id,
        facility: {},
        users: [],
        regions: [],
        uploadedFiles: [],
        imgs:[],
        openDate: null,
        lastServiceDate: null,

    },

    computed: {
        /* отфильтрованный список */


    },

    methods: {
        zero(item, n) {
            return (zeroPad(item, n))
        },
        img_del(item) {
            console.log(item);
            FetchJsonDELETE(' /api/get_file/'+item.file,{}).then(()=>this.load_img())
        },
        handleDrop(event) {
            event.preventDefault();
            const files = event.dataTransfer.files;
            this.handleFiles(files);
        },
        handleFileSelect(event) {
            const files = event.target.files;
            this.handleFiles(files);
        },
        handleFiles(files) {
            for (let i = 0; i < files.length; i++) {
                const allowedExtensions = ["jpg", "jpeg", "png", "gif"]; // Допустимые расширения
                const fileName = files[i].name.toLowerCase();
                const fileExtension = fileName.split(".").pop();

                if (allowedExtensions.includes(fileExtension)) {
                    this.uploadedFiles.push(files[i]);
                } else {
                    console.warn(`Файл ${fileName} не является изображением и не будет добавлен.`);
                }
            }
            this.uploadFiles()
        }
        ,
        uploadFiles() {
            let files = this.uploadedFiles;

            // Функция для создания замыкания
            const deleteFileFromList = (fileToDelete) => {
                this.uploadedFiles = this.uploadedFiles.filter(value => value !== fileToDelete);
            };

            for (let i = 0; i < files.length; i++) {
                let formData = new FormData();
                formData.append('file', files[i]);

                FetchFile('/api/facility_img_upload/' + this.id, formData)
                    .then((result) => {
                        this.load_img();
                        deleteFileFromList(files[i]);
                    })
                    .catch(error => {
                        deleteFileFromList(files[i]);
                        console.error("Ошибка при загрузке файла:", error);
                    });
            }
        },
        localDate(date){
            return (localFormatDate(date));
        },

        async load() {  // пример загрузки из API
            this.facility = await FetchJsonPOST(url_facility + this.id, {});
            this.openDate = convertToDate(this.facility.openDate)
            this.lastServiceDate = convertToDate(this.facility.lastServiceDate)
            this.users = await FetchJsonGET('/api/users/');
            this.regions = await FetchJsonGET('/api/region/');
            this.load_img();
        },
         async load_img() {
            this.imgs = await FetchJsonGET('/api/facility_img_upload/' + this.id);
         },

    },

    async created() { // функция, которая вызывается при старте
        await this.load()
    }
    ,
})



