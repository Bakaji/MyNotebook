export default {
    state: {
        __state_add_collection_modal: false,
        __state_edit_collection_modal: false,

    },
    getters: {
        AddCollectionModalVisible: (state) => state.__state_add_collection_modal,
        EditCollectionModalVisible: (state) => state.__state_edit_collection_modal,
    },
    mutations: {
        setAddCollectionModal: (state, value) => {
            state.__state_add_collection_modal = value;
            return state;
        }, setEditCollectionModal: (state, value) => {
            state.__state_edit_collection_modal = value;
            return state;
        },
    },
    actions: {
        showAddCollectionModal: ({commit}) => {
            commit('setAddCollectionModal', true)
        },
        hideAddCollectionModal: ({commit}) => {
            commit('setAddCollectionModal', false)
        },
        showEditCollectionModal: ({commit}) => {
            commit('setEditCollectionModal', true)
        },
        hideEditCollectionModal: ({commit}) => {
            commit('setEditCollectionModal', false)
        },
        setAddCollectionErrors: ({commit}, data) => {
            console.log(data);
            let a = false;
            if (a) {
                commit("setErrors")//TODO add errors handlers
            }
        },
    },
}