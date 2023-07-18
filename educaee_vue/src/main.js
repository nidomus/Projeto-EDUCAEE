import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import { library } from '@fortawesome/fontawesome-svg-core'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

import { faCamera } from '@fortawesome/free-solid-svg-icons'

import axios from 'axios'

library.add(faCamera)

axios.defaults.baseURL = 'http://127.0.0.1:8000'

createApp(App).use(store).component('font-awesome-icon', FontAwesomeIcon).use(router).mount('#app')
