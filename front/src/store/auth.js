export default {
    namespaced: true,
    state: {
        isUser: localStorage.getItem('token')||'',
    },
    getters: {
        User: state => state.isUser,
    },
    mutations: {
        USER_SET (state, payload) {
            state.isUser = payload
            localStorage.setItem('token', state.isUser)
        }
    },
    actions: {
        loginUser ({ commit }, params) {
            commit('USER_SET', params)
        },

    }
}
