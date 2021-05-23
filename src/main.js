import Vue from 'vue'
import App from './App.vue'

Vue.config.productionTip = false

new Vue({
    render: h => h(App),
    data : {
        title: "Undergraduate student at the University of Bonn"
    }
}).$mount('#app')
