import { createRouter, createWebHistory } from 'vue-router'
import store from '../store'

import HomeView from '../views/HomeView.vue'
import LogIn from '../views/LogIn.vue'
import Alunos from '../views/Alunos.vue'
import CadastrarAluno from '../views/CadastrarAluno.vue'
import Painel from '../views/Painel.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView,
    meta: {
      requireLogin: true,
    }
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
  },
  {
    path: '/painel',
    name: 'Painel',
    component: Painel,
    meta: {
      requireLogin: true,
      title: 'Painel'

    }
  },
  {
    path: '/cadastar-aluno',
    name: 'CadastrarAluno',
    component: CadastrarAluno,
    meta: {
      requireLogin: true,
      title: 'Cadastrar Aluno'

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
