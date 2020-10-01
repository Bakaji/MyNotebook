import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import {FontAwesomeIcon} from '@fortawesome/vue-fontawesome'
import {library} from '@fortawesome/fontawesome-svg-core'
import {
    faAngleRight,
    faCaretDown,
    faCaretUp,
    faEllipsisV,
    faBars
} from '@fortawesome/free-solid-svg-icons'

library.add(faEllipsisV, faCaretDown, faCaretUp, faAngleRight, faBars);

Vue.config.productionTip = false;

if (process.env.NODE_ENV === "development") {
    //TODO remove those lines for production
    const t = "e63281fcefbbf2606f49f9771eab4cc057e35b66";
    axios.defaults.headers.common['Authorization'] = `Token ${t}`
}

Vue.component('font-awesome-icon', FontAwesomeIcon);

new Vue({
    router,
    store,
    render: h => h(App)
}).$mount('#app');
