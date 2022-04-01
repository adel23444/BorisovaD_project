export default {
    namespaced: true,
    state: {
        isUser: false,
        isBukh: false,
        isAdmin: false,
        isZavHoz: false
    },
    getters: {
        isUser: state => state.isUser,
        isAdmin: state => state.isAdmin,
        isBukh: state => state.isBukh,
        isZavHoz: state => state.isZavHoz
    },
    mutations: {
        USER_SET (state, payload) {
            state.isUser = payload
        },
        BUKH_SET (state, payload) {
            state.isBukh = payload
        },
        ADMIN_SET (state, payload) {
            state.isAdmin = payload
        },
        ZAVHOZ_SET (state, payload) {
            state.isZavHoz = payload
        }
    },
    actions: {
        loginUser ({ commit }, params) {
            commit('USER_SET', params)
            console.log('user')
        },
        loginAdmin ({ commit }, params) {
            commit('ADMIN_SET', params)
            console.log('admin')
        },
        loginBukh ({ commit }, params) {
            commit('BUKH_SET', params)
            console.log('bukh')
        },
        loginZav ({ commit }, params) {
            commit('ZAVHOZ_SET', params)
        }
    }
}
