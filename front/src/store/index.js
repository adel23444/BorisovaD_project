import Vue from 'vue'
import Vuex from 'vuex'
import auth from './modules/auth'
import zayavka_polom from './modules/zayavka_polom'
import zayavka_trans from "./modules/zayavka_trans"
import zayavka_canc from "./modules/zayavka_canc"

Vue.use(Vuex)

export const store = new Vuex.Store({
    modules: {
        auth,
        zayavka_polom,
        zayavka_trans,
        zayavka_canc
    }
})