import axios from "axios";

axios.defaults.withCredentials = true;
axios.defaults.xsrfHeaderName = "X-CSRFToken"
axios.defaults.xsrfCookieName = "XSRF-TOKEN"

const api = axios.create({
  baseURL:  'http://localhost:8000/',
});

export default api;