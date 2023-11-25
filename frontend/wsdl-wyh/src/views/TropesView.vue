<template>
  <div class="row">
    <h3>Tropes</h3>
  </div>
  <div class="row" style="margin-top: 10px;">
    <ul style="columns: 4; list-style-type: none;">
      <li v-for="trope in tropes.sort()" :key="trope">
        <a class="trope-link" @click="goToPage(trope)" >
          {{ trope }}
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
import { separateWordsByCapitalLetters } from '../assets/utils/utils.js'
import axios from 'axios';

export default {
  components: {

  },

  data() {
    return {
      tropes: []
    }
  },

  methods: {
    goToPage(trope) {
      var tropeName = trope.split(' ').join('');
      this.$router.push({ name: 'trope page', params: { id: tropeName } })
    }
  },
  
  async beforeMount() {
  var tropeNames = [];
    await axios.get("http://localhost:8000/rdf-all/tropenames")
      .then(response => {
        tropeNames = response.data
      });

      for(var i = 0; i < tropeNames.length; i++) {
        this.tropes.push(separateWordsByCapitalLetters(tropeNames[i]));
      }      
    }
  
}
</script>



