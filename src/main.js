import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = true


/*let vm = */new Vue(
    {
        el: "#app",
        render: comp => comp(App),
    }
)
