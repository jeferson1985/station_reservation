import { createApp } from 'vue'
import './index.css'
import 'v-calendar/style.css';
import App from './App.vue'
import router from './router'
import VCalendar from 'v-calendar';

const app = createApp(App)
app.use(router)
app.mount('#app')
app.use(VCalendar)

