import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = true

Vue.prototype.$lang = "en"
Vue.prototype.$theme = "light"

/*let vm =*/ new Vue(
    {
        el: "#app",
        render: comp => comp(App),
    }
)
