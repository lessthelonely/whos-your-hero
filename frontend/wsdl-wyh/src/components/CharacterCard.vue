<template>
    <div class="card character-card" style="width: 300px; height: 300px; padding: 0px; margin-right: 50px;" @click="this.redirect()">
        <img :src="image" style="width: 100%; border-radius: 20px; padding: 0px; width: 300px; height: 300px; object-fit: cover;" />
        <div class="card-img-overlay"
            style="bottom: 0; top: 240px; text-align: center; justify-self: center; align-self: center; font-size: 20px; color: white;">
            <p style="font-weight: bold; color: white; font-size: 24px; text-shadow: black 1px 0 10px;">
                {{ name }}
            </p>
        </div>
    </div>
</template>

<script >
import { defineComponent } from 'vue'

export default defineComponent({
    props: {
        name: String,
        image: String,
    },

    components: {
    },

    data() {
        return {}
    },

    methods: {
        redirect() {
            var route = this.name.toLowerCase().replace(' ', '_')

            this.$router.push({ name: 'character page', params: { id: route} })
        }
    }
})
</script>