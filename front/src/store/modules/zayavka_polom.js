import http from '../api'

export default {
    namespaced: true,
    state: {
        zayavka: []
    },
    getters: {
        Zayavka_polomka: state => state.zayavka
    },
    mutations: {
        ZAYAVKA_SET (state, payload) {
            state.zayavka = payload.data
            console.log(state.zayavka)
        },
    },
    actions: {
        get_zayavka ({ commit }) {
            return new Promise((resolve, reject) => {
                http.api.get('zayavka_polomka/my/').then((response) => {
                    commit('ZAYAVKA_SET', response)
                    resolve(response)
                }).catch((error) => {
                    reject(error)
                })

            })
        }
    }
}
