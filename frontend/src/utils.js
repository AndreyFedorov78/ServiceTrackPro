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


export function getToken() {
  return   getCookie('csrftoken');
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

export async function FetchJsonGET(url) {
  return await FetchJSON(url, "GET", null);
}

export async function FetchJsonPOST(url, data) {
  return await FetchJSON(url, "POST", data);
}

export async function FetchJsonDELETE(url, data) {
  return await FetchJSON(url, "DELETE", data);
}

export async function FetchJsonPUT(url, data) {
  return await FetchJSON(url, "PUT", data);
}