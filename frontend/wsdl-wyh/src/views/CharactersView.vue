<template>
  <div class="row" style="justify-content: center;">
    <CharacterCard v-for="c in characters.slice(0, 3)" v-bind:key="c.key" :name="c.name" :image="c.image" />
  </div>
  <div class="row" style="justify-content: center; margin-top: 50px;">
    <CharacterCard v-for="c in characters.slice(3, 5)" v-bind:key="c.key" :name="c.name" :image="c.image" />
  </div>
</template>

<script>
import CharacterCard from '../components/CharacterCard.vue'

export default {
  components: {
    CharacterCard
  },

  data() {
    return {
      characters: [
        {key: "emma_frost", name: 'Emma Frost', image: 'images/image 1.png'},
        {key: "midnighter", name: 'Midnighter', image: 'images/image 2.png'},
        {key: "deadpool", name: 'Deadpool', image: 'images/image 3.png'},
        {key: "cassandra_cain", name: 'Cassandra Cain', image: 'images/image 4.png'},
        {key: "wally_west", name: 'Wally West', image: 'images/image 5.png'},

      ]
    }
  },

  setup() {
    return {}
  },
}
</script>



