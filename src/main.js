import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = true

Vue.prototype.$lang = "de"

/*let vm =*/ new Vue(
    {
        el: "#app",
        render: comp => comp(App),
    }
)
