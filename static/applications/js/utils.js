function getCookie(name) {
    const cookieName = name + '=';
    const cookieArray = document.cookie.split(';');

    for (let i = 0; i < cookieArray.length; i++) {
        let cookie = cookieArray[i];
        while (cookie.charAt(0) === ' ') {
            cookie = cookie.substring(1);
        }
        if (cookie.indexOf(cookieName) === 0) {
            return decodeURIComponent(cookie.substring(cookieName.length, cookie.length));
        }
    }
    return null;
}


function getToken() {
    return getCookie('csrftoken');
}


async function FetchJSON(url, method, data) {
    const headers = {
        "Content-Type": "application/json",
        charset: "utf-8",
        "X-CSRFToken": getToken(),
    };

    try {
        let header = {};
        if (method == "GET") {
            header = {
                method: method,
                headers: headers,
            };
        } else {
            header = {
                method: method,
                headers: headers,
                body: JSON.stringify(data),
            };
        }

        const response = await fetch(url, header);

        if (response.ok) {
            const responseData = await response.json();
            return responseData;
        } else {
            return null;
        }
    } catch (error) {
        return null;
    }
}

async function FetchJsonGET(url) {
    return await FetchJSON(url, "GET", null);
}

async function FetchJsonPOST(url, data) {
    return await FetchJSON(url, "POST", data);
}

async function FetchJsonDELETE(url, data) {
    return await FetchJSON(url, "DELETE", data);
}

async function FetchJsonPUT(url, data) {
    return await FetchJSON(url, "PUT", data);
}


// перевод даты из строки в дату
function convertToDate(dateString) {
    if (dateString == null) return null
    const [year, month, day] = dateString.split('-');
    // Месяцы в JavaScript начинаются с 0, поэтому вычитаем 1 из месяца
    return new Date(year, month - 1, day);
}

function formatDate(date) {
    if (date == null) return null
    const year = date.getFullYear();
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const day = date.getDate().toString().padStart(2, '0');
    return `${year}-${month}-${day}`;
}
function localFormatDate(date) {
    if (date == null) return null
    const year = date.getFullYear();
    const month = (date.getMonth() + 1).toString().padStart(2, '0');
    const day = date.getDate().toString().padStart(2, '0');
    return `${day}/${month}/${year}`;
}

function zeroPad(value, n) {
    let str = '' + value;
    while (str.length < n) {
        str = '0' + str;
    }
    return str;
}


async function FetchFile(url, data) {
    const headers = {
        //'Content-Type': 'multipart/form-data',
        "X-CSRFToken": getToken(),
    };
    let response = await fetch(url, {
        method: "post",
        headers: headers,
        body: data,
    });

    return response
}
