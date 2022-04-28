export default {
    namespaced: true,
    state: {
        isUser: localStorage.getItem('token')||'',
        UserName: ""
    },
    getters: {
        User: state => state.isUser,
        UserName: state => state.UserName
    },
    mutations: {
        USER_SET (state, payload) {
            state.isUser = payload
            localStorage.setItem('token', state.isUser)
        },
        NAME (state, payload) {
            state.UserName = payload
        }
    },
    actions: {
        loginUser ({ commit }, params) {
            commit('USER_SET', params["token"])
            commit('NAME', params["name"])
        },
        logout ({ commit }) {
            commit('USER_SET', '')
            commit('NAME', '')
        }
    }
}
