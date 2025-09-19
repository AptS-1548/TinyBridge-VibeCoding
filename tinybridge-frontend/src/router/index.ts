import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      redirect: '/links'
    },
    {
      path: '/links',
      name: 'links',
      component: () => import('../views/LinksView.vue'),
    },
    {
      path: '/create',
      name: 'create-link',
      component: () => import('../views/CreateLinkView.vue'),
    },
    {
      path: '/links/:id',
      name: 'link-detail',
      component: () => import('../views/LinkDetailView.vue'),
    },
  ],
})

export default router
