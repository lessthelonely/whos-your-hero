<template>
    <div style="display: flex; justify-content: center;">
        <img :src="src" style="width: 85%; margin: 10px 0px;"/>
    </div>
</template>

<script>
import { defineComponent } from 'vue'

export default defineComponent({
    props: {
        src: {
            type: String,
            required: true
        }
    }
})
</script>