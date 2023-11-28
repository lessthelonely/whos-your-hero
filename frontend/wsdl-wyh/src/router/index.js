import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/HomeView.vue')
    },
    {
      path: '/about',
      name: 'about',
      component: () => import('../views/AboutView.vue')
    },
    {
      path: '/characters',
      name: 'characters',
      component: () => import('../views/CharactersView.vue')
    },
    {
      path: '/character/:id',
      name: 'character page',
      component: () => import('../views/CharacterView.vue')
    },
    {
      path: '/trope/:id',
      name: 'trope page',
      component: () => import('../views/TropeView.vue')
    },
    {
      path: '/tropes/',
      name: 'tropes page',
      component: () => import('../views/TropesView.vue')
    },
    {
      path: '/graph',
      name: 'graph page',
      component: () => import('../views/GraphView.vue')
    },
    {
      path: '/random',
      name: 'random page',
      component: () => import('../views/RandomView.vue')
    }
  ]
})

export default router
