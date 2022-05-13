import http from '../api'

export default {
    namespaced: true,
    state: {
        my_zayavka: [],
        zayavka: []
    },
    getters: {
        My_zayavka_canc: state => state.my_zayavka,
        Zayavka_canc: state => state.zayavka
    },
    mutations: {
        MY_ZAYAVKA_SET (state, payload) {
            state.my_zayavka = payload.data
        },
        ZAYAVKA_SET (state, payload) {
            state.zayavka = payload.data
        },
    },
    actions: {
        get_my_zayavka ({ commit }) {
            return new Promise((resolve, reject) => {
                http.api.get('zayavka_canc/my/').then((response) => {
                    commit('MY_ZAYAVKA_SET', response)
                    resolve(response)
                }).catch((error) => {
                    reject(error)
                })

            })
        },
        get_zayavka ({ commit }) {
            return new Promise((resolve, reject) => {
                http.api.get('zayavka_canc/').then((response) => {
                    commit('ZAYAVKA_SET', response)
                    resolve(response)
                }).catch((error) => {
                    reject(error)
                })

            })
        },
    }
}
