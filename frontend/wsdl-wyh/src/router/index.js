import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
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
    }
  ]
})

export default router
