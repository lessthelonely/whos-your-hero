<template>
  <h1>

  </h1>
</template>

<script>
import { defineComponent } from 'vue'
import axios from 'axios'

export default defineComponent({
  data() {
    return {
      id: String,
      name: String
    }
  },

  async beforeMount() {
    this.id = this.$route.params.id

    this.name = '';
    
    var count = 0
    for (var n in this.id.replace('_', ' ').split(' ')) {
      this.name += n[0].toUpperCase() + n.slice(1)

      if (count == this.id.replace('_', ' ').split(' ').length - 1)
        this.name += ' '
    }

    await axios.get("http://localhost:8000/rdf-character/" + this.id + "/birthday")
      .then(response => {
        console.log(response.data)
      });
  }
})
</script>

