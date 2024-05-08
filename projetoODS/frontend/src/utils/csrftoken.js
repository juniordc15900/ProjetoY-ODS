import axios from "axios";

// const getCSRFToken = () => {
//   const csrfTokenElement = document.querySelector("[name=csrfmiddlewaretoken]");
//   if (csrfTokenElement) {
//     return csrfTokenElement.value;
//   } else {
//     console.error("CSRF token not found in the DOM");
//     return null;
//   }
// };

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i];
      // Does this cookie string begin with the name we want?
      if (cookie.substring(1, name.length + 1) === name) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 2));
        break;
      }
    }
  }
  return cookieValue;
}

const axiosInstance = axios.create({
  baseURL: "http://localhost:8000/",
  timeout: 5000,
  headers: {
    "Content-Type": "application/json",
  },
});

axiosInstance.defaults.xsrfHeaderName = "X-CSRFTOKEN";
axiosInstance.defaults.xsrfCookieName = "csrftoken";

axiosInstance.interceptors.request.use((config) => {
  const csrfToken = getCookie("csrftoken");
  if (csrfToken) {
    config.headers["X-CSRFTOKEN"] = csrfToken;
  }
  return config;
});

export default axiosInstance;
