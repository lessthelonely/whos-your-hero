import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import VueSidebarMenu from 'vue-sidebar-menu'
import App from './App.vue'

import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'
import router from './router/index.js'

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faQuestion, faUser, faPeopleGroup } from '@fortawesome/free-solid-svg-icons'

import bootstrap from 'bootstrap/dist/css/bootstrap.min.css'
import bootstrapjs from 'bootstrap/dist/js/bootstrap.min'

/* add icons to the library */
library.add(faQuestion, faUser, faPeopleGroup)

/* add font awesome icon component */


const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(VueSidebarMenu)
app.use(createPinia())
app.use(router)

app.mount('#app')
