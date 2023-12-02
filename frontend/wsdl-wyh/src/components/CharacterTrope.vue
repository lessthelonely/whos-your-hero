<template>
    <div class="row" style="display: flex; flex-wrap: nowrap; flex-direction: row; width: 100%; padding: 0px;">
        <img class="image character-trope-img" :src="photo"
            style="padding: 0px; border-radius: 10px 0px 0px 10px; width: 20%; object-fit: cover; object-position: center top; background-image: asset-url(attr('photo'))" />
        <div style="width: 80%; padding: 0px;">
            <h6 style="height: 10%; border-radius: 0px 10px 0px 0px; margin: 0px; background-color: #212529; color: white; padding: 10px;">
                {{ iteration != "" ? iteration : name }}
            </h6>
            <p style="height: 90%; text-align: justify; background-color: #adb5bd; padding: 10px; border-radius: 0px 0px 10px 0px;">
                {{ description }}
            </p>
        </div>
    </div>
</template>


<script>
import { defineComponent } from 'vue'
import axios from 'axios'
import { Trope } from '../stores/Trope.js'
import { separateWordsByCapitalLetters } from '../assets/utils/utils.js'

export default defineComponent({
    props: {
        name: String,
        description: String,
        iteration: {
            type: String,
            default: ""
        },
    },


    data() {
        return {
            photo: String
        }
    },
    watch: {
        name: async function (newName) {
            console.log("name", this.name)
            var backend_name = this.name.toLowerCase().replace(" ", "_");
            console.log("backend_name", backend_name)

            await axios.get("http://localhost:8000/rdf-character/" + backend_name + "/photo")
                .then(response => {
                    this.photo = response.data["http://whosyourhero.com/heroes.owl#" + this.name.replace(" ", "")][0];
                }); {
                this.getName();
            }
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
                console.log("desc replace", description)
            }

            console.log("desc", description);

            return description;
        }
    },

    async beforeMount() {
        console.log("name", this.name)
        var backend_name = this.name.toLowerCase().replace(" ", "_");
        console.log("backend_name", backend_name)

        await axios.get("http://localhost:8000/rdf-character/" + backend_name + "/photo")
            .then(response => {
                this.photo = response.data["http://whosyourhero.com/heroes.owl#" + this.name.replace(" ", "")][0];
            });
    }
})
</script>