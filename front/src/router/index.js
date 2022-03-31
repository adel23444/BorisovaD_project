import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)
const routes = [
    {
        path: '/',
        name: 'Main_Wind',
        component: () => import('../views/Main_Wind')
    },
    {
        path: '/login',
        name: 'Login_Wind',
        component: () => import('../views/Login_Wind')
    },
    {
        path: '/new',
        name: 'New_Zayavka',
        component: () => import('../views/New_Zayavka')
    }
]

const router = new VueRouter({
    mode: 'history',
    routes
})

export default router