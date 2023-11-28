<template>
  <SplashScreen v-if="!loaded" />
  <div v-else>
    <div style="display: flex; margin-bottom: 15px;">
      <div class="header">
        <h1 style="font-weight: bold;">
          {{ trope.name }}
        </h1>
        <p style="text-align: justify; padding-right: 10px;" v-html="trope.description">
        </p>
      </div>
    </div>

    <div style="display: flex; flex-direction: column;">
      <h4 style="margin-bottom: 10px;">Seen on...</h4>
      <CharacterTrope v-for="(value, key) in characterTropes" :name="key" :description="value" />
    </div>
  </div>
</template>

<script>
import { defineComponent } from 'vue'
import axios from 'axios'
import { Trope } from '../stores/Trope.js'
import CharacterTrope from '../components/CharacterTrope.vue'
import { separateWordsByCapitalLetters } from '../assets/utils/utils.js'
import SplashScreen from './SplashScreen.vue'

export default defineComponent({
  components: {
    CharacterTrope,
    SplashScreen
  },

  data() {
    return {
      trope: Trope,
      characterTropes: {},
      loaded: false
    }
  },

  methods: {
    getName() {
      switch (this.id) {
        case "cassandra_cain":
          this.name = "Cassandra Cain"
          return "CassandraCain"
          break;
        case "emma_frost":
          this.name = "Emma Frost"
          return "EmmaFrost"
          break;
        case "wally_west":
          this.name = "Wally West"
          return "WallyWest"
          break;
        case "deadpool":
          this.name = "Deadpool"
          return "Deadpool"
          break;
        case "midnighter":
          this.name = "Midnighter"
          return "Midnighter"
          break;
        default:
          throw console.error("Character not found");
      }
    },

    parseDescription(description) {
      let urlsWithBraces = [...description.match(/(?<!\\)(\[.*?(?<!\\)\])/g)]

      let urls = urlsWithBraces.map(urlWithBraces => {
        let urlWithoutBraces = urlWithBraces.substring(1, urlWithBraces.length - 1);
        let urlWithoutQuotation = urlWithoutBraces.substring(1, urlWithoutBraces.length - 1);

        return urlWithoutQuotation
      });

      description = description.split('["').join('').split('"]').join('');

      for (var i = 0; i < urls.length; i++) {
        var newLink = `<a href="${urls[i]}" style="font-style: normal;"><sup>ref</sup></a>`;
        description = description.replace(" " + urls[i], newLink);
      }

      return description;
    }
  },

  async beforeMount() {
    this.id = this.$route.params.id

    await axios
      .get("http://localhost:8000/rdf-trope/" + this.id)
      .then(response => {

        this.trope = new Trope(separateWordsByCapitalLetters(this.id), this.parseDescription(response.data[this.id]));

      });

    await axios
      .get("http://localhost:8000/rdf-all/trope/" + this.id)
      .then(response => {
        for (var property in response.data) {
          this.characterTropes[separateWordsByCapitalLetters(property)] = response.data[property]
        }

        this.loaded = true
      });
  }
})
</script>