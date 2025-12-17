import { createRouter, createWebHistory } from 'vue-router'

import Home from './components/Home.vue'
import Create from './components/Create.vue'
import ArticlesDetails from './components/ArticlesDetails.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/create',
    name: 'create',
    component: Create
  },
  {
    path: '/details/:id',
    name: 'details',
    component: ArticlesDetails,
    props: true
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
