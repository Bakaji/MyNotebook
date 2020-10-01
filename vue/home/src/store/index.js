import Vue from 'vue'
import Vuex from 'vuex'
import NavigationModule from './modules/navigation_module'
import CollectionModule from './modules/collections_memos'
import ModalsModule from './modules/modals'

Vue.use(Vuex);

export default new Vuex.Store({
    modules: {
        NavigationModule,
        CollectionModule,
        ModalsModule
    }
})
