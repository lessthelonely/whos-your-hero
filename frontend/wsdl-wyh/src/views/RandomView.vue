<template>
    <SplashScreen />
</template>

<script>
import axios from 'axios';
import { defineComponent } from 'vue'
import SplashScreen from './SplashScreen.vue';

export default defineComponent({
    components: {
        SplashScreen
    },

    data() {
        return {
            tropeNames: [],
            characterNames: ["emma_frost", "midnighter", "deadpool", "cassandra_cain", "wally_west", 'cyclops'],
            routes: ['character', 'trope']
        }
    },

    methods: {
    },

    async beforeMount() {
        await axios.get("http://localhost:8000/rdf-all/tropenames")
            .then(response => {
                this.tropeNames = response.data
            });

        var random, name
        if (Math.random() < 0.5) {
            name = "character"
            random = this.characterNames[Math.floor(Math.random() * this.characterNames.length)];
        } else {
            name = "trope"
            random = this.tropeNames[Math.floor(Math.random() * this.tropeNames.length)];
        }

        this.$router.push({ name: name + ' page', params: { id: random }})
    }

})
</script>