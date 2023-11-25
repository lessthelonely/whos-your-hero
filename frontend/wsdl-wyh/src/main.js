import './assets/main.css'

import { createApp } from 'vue'
import { createPinia } from 'pinia'
import "bootstrap/dist/css/bootstrap.min.css"
import "bootstrap"
import VueSidebarMenu from 'vue-sidebar-menu'
import App from './App.vue'

import cytoscape from 'cytoscape'
import spread from 'cytoscape-spread'

import 'vue-sidebar-menu/dist/vue-sidebar-menu.css'
import router from './router/index.js'

cytoscape.use(spread);

/* import the fontawesome core */
import { library } from '@fortawesome/fontawesome-svg-core'

/* import font awesome icon component */
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

/* import specific icons */
import { faQuestion, faUser, faPeopleGroup, faDiagramProject } from '@fortawesome/free-solid-svg-icons'

/* add icons to the library */
library.add(faQuestion, faUser, faPeopleGroup, faDiagramProject)

/* add font awesome icon component */


const app = createApp(App)
app.component('font-awesome-icon', FontAwesomeIcon)
app.use(VueSidebarMenu)
app.use(createPinia())
app.use(router)
app.use(cytoscape)

app.mount('#app')
