import Vue from 'vue'
import App from './App.vue'
import axios from 'axios'
import { BootstrapVue } from 'bootstrap-vue'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import 'bootstrap/dist/css/bootstrap.css'

Vue.config.productionTip = false
Vue.use(BootstrapVue)
axios.defaults.baseURL = 'http://127.0.0.1:5000/'
new Vue({
  render: h => h(App)
}).$mount('#app')
