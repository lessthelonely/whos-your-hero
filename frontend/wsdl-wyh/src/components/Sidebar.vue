<template>
    <sidebar-menu :menu="menu" collapsed="true" />
</template>
  
<script>
import { defineComponent } from 'vue'
import { RouterLink, RouterView } from 'vue-router'
import Logo from './Logo.vue'

export default defineComponent({
    components: {
        RouterLink,
        RouterView
    },

    data() {
        return {
            menu: [
                {
                    component: Logo,
                    props: {
                        src: '/images/logo.svg'
                    }
                    // props: componentProps
                    // hidden: false
                    // hiddenOnCollapse: true
                },
                {
                    header: 'Navigation',
                    hiddenOnCollapse: true,
                },
                {
                    href: '/about',
                    title: 'About',
                    icon: {
                        element: 'font-awesome-icon',
                        attributes: {
                            icon: 'question'
                        },
                    },
                },
                {
                    href: '/characters',
                    title: 'Characters',
                    icon: {
                        element: 'font-awesome-icon',
                        attributes: {
                            icon: 'people-group'
                        },
                    },
                },
                {
                    href: '/graph',
                    title: 'Graph',
                    icon: {
                        element: 'font-awesome-icon',
                        attributes: {
                            icon: 'diagram-project',
                        }
                    }
                },
            ],
        }
    }
})

</script>
  