import Vue from 'vue'
import App from './App.vue'
<<<<<<< HEAD
=======
import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

// Make BootstrapVue available throughout your project
Vue.use(BootstrapVue)
// Optionally install the BootstrapVue icon components plugin
Vue.use(IconsPlugin)
>>>>>>> 1fb72973e2161ae326ec8c2d038ff8da4e59b22f

Vue.config.productionTip = false

new Vue({
  render: h => h(App),
}).$mount('#app')
