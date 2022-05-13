import http from '../api'

export default {
    namespaced: true,
    state: {
        token: localStorage.getItem('token') || '',
        isUser: localStorage.getItem('user')||'',
        UserName: ""
    },
    getters: {
        User: state => state.isUser,
        UserName: state => state.UserName
    },
    mutations: {
        USER_SET (state, payload) {
            state.isUser = payload
            localStorage.setItem('user', state.isUser)
        },
        TOKEN_SET (state, payload) {
            state.token = payload.data.access
            localStorage.setItem('token', state.token)
        },
        NAME (state, payload) {
            state.UserName = payload
        }
    },
    actions: {
        loginUser (state, user) {
            return new Promise((resolve, reject) => {
                http.api.post('token', user).then((response) => {
                    state.commit('TOKEN_SET', response)
                    http.api.get('user_info').then((new_response) => {
                        state.commit('USER_SET', new_response.data.role)
                        state.commit('NAME', new_response.data.name)
                    })
                    resolve(response)
                }).catch((error) => {
                    reject(error)
                })
            })
        },
        logout ({ commit }) {
            commit('USER_SET', '')
            commit('NAME', '')
        }
    }
}
