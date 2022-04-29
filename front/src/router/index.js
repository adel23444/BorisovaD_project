import Vue from 'vue'
import VueRouter from 'vue-router'
import {store} from "../store";

Vue.use(VueRouter)
const isAuth = (to, from, next) => {
    if (store.getters['auth/User']) {
        next()
        return
    }
    next('/login')
}
const routes = [
    {
        path: '/',
        name: 'Main_Wind',
        component: () => import('../views/Main_Wind'),
        beforeEnter: isAuth
    },
    {
        path: '/login',
        name: 'Login_Wind',
        component: () => import('../views/Login_Wind')
    },
    {
        path: '/new',
        name: 'New_Zayavka',
        component: () => import('../views/New_Zayavka'),
        beforeEnter: isAuth
    },
    {
        path: '/doc',
        name: 'MyDoc',
        component: () => import('../views/Doc_Wind'),
        beforeEnter: isAuth
    },
    {
        path: '/users',
        name: 'Users',
        component: () => import("../views/User_Wind"),
        beforeEnter: isAuth
    }
]

const router = new VueRouter({
    mode: 'history',
    routes
})

export default router