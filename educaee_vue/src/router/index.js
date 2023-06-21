import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'

import HomeView from '../views/HomeView.vue'
import LogIn from '../views/LogIn.vue'
import Alunos from '../views/Alunos.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/alunos',
    name: 'Alunos',
    component: Alunos,
    meta: {
      requireLogin: true,
      title: 'Alunos'

    }
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  const title = to.meta.title
  if (title) {
    document.title = title
  }
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next('/log-in')

  } else {

    next()
  }
})

export default router
