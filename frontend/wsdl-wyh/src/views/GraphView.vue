<template>
    <SplashScreen v-if="!loaded" />
    <Visualizer :graphData="this.graphData" v-else />
</template>
  
<script>
import { defineComponent } from 'vue'
import axios from 'axios'
import Visualizer from '../components/Visualizer.vue'
import SplashScreen from './SplashScreen.vue'

export default defineComponent({
    props: {

    },

    components: {
        Visualizer,
        SplashScreen
    },

    data() {
        return {
            loaded: false,
            graphData: Object,
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
        let tropeData;
        let powerData;
        let storyArcData;
        let mediaData;
        await axios.get("http://localhost:8000/rdf-all/trope")
            .then(response => {
                tropeData = response.data
            });
        await axios.get("http://localhost:8000/rdf-all/power")
            .then(response => {
                powerData = response.data
            });
        await axios.get("http://localhost:8000/rdf-all/storyArc")
            .then(response => {
                storyArcData = response.data
            });
        await axios.get("http://localhost:8000/rdf-all/media")
            .then(response => {
                mediaData = response.data
            });

        this.graphData = {
            "tropeData": tropeData,
            "powerData": powerData,
            "storyArcData": storyArcData,
            "mediaData": mediaData
        }
    },

    mounted() {
        this.loaded = true
    }
})
</script>