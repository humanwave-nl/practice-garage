import Vue from 'vue'
import Router from 'vue-router'
import Garages from '../components/garagelist'

Vue.use(Router)

export default new Router({
    routes: [
        {
            path: '/',
            name: 'home',
            component: Garages
        },
    ]
})
