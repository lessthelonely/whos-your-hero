<template>
    <Visualizer :tropeData="this.tropeData" />
</template>
  
<script>
import { defineComponent } from 'vue'
import axios from 'axios'
import Visualizer from '../components/Visualizer.vue'

export default defineComponent({
    props: {

    },

    components: {
        Visualizer
    },

    data() {
        return {
            tropeData: Object
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

        separateWordsByCapitalLetters(inputString) {
            // Use a regular expression to split the string at capital letters
            inputString = inputString.replace(/_/g, ' ');

            // Use a regular expression to split the string at specific patterns
            var wordsArray = inputString.split(/(?=[A-Z][a-z])|(?<=[a-z])(?=[A-Z])/);

            // Join the array elements with space to form the final string
            var resultString = wordsArray.join(' ');

            return resultString;
        },
    },

    async beforeMount() {
        await axios.get("http://localhost:8000/rdf-all/trope")
            .then(response => {
                this.tropeData = response.data
            });
    }
})
</script>