import Vue from 'vue'
import Vuex from 'vuex'
import auth from './modules/auth'
import zayavka_polom from './modules/zayavka_polom'

Vue.use(Vuex)

export const store = new Vuex.Store({
    modules: {
        auth,
        zayavka_polom
    }
})