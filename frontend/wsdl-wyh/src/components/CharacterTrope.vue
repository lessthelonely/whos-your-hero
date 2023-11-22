<template>
    <div class="row" style="width: 100%; padding-left: 12px;">
        <div class="col-md-2" style="width: 20%; padding: 0px;">
            <div class="display: flex; width: 100%; height: 100%; padding: 0px;">
                <img class="character-trope-img" :src="photo"
                    style="border-radius: 10px 0px 0px 10px; width: 100%; object-fit: cover; object-position: center top;" />
            </div>

        </div>
        <div class="col-md-8" style="width: 80%; padding: 0px;">
            <h6
                style="border-radius: 0px 10px 0px 0px; margin: 0px; background-color: #212529; color: white; padding: 10px;">
                {{ name }}
            </h6>
            <p
                style="height: 150px; text-align: justify; background-color: #adb5bd; padding: 10px; border-radius: 0px 0px 10px 0px;">
                {{ description }}
            </p>
        </div>
    </div>
</template>


<script>
import { defineComponent } from 'vue'
import axios from 'axios'
import { Trope } from '../stores/Trope.js'

export default defineComponent({
    props: {
        name: String,
        description: String,
    },


    data() {
        return {
            photo: String
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
                console.log("desc replace", description)
            }

            console.log("desc", description);

            return description;
        }
    },

    async beforeMount() {
        var backend_name = this.name.toLowerCase().replace(" ", "_");
        console.log("backend_name", backend_name)
        await axios.get("http://localhost:8000/rdf-character/" + backend_name + "/photo")
            .then(response => {
                this.photo = response.data["http://whosyourhero.com/heroes.owl#" + this.name.replace(" ", "")][0];
            });
    }
})
</script>