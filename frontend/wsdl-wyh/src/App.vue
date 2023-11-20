<template>
  <div style="display: block; flex-direction: row">
    <div>
      <Sidebar @update:collapsed="onToggleCollapse" />
    </div>
    <div id="main">
      <RouterView />
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import Sidebar from './components/Sidebar.vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'

export default defineComponent({
  components: {
    RouterLink,
    RouterView,
    Sidebar,
    FontAwesomeIcon
  },

  data() {
    return {}
  },

  methods: {
    onToggleCollapse() {
      document.getElementById("main").classList.toggle("collapsed")
    }
  }
})

</script>
