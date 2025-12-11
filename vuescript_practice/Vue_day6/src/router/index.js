import { createRouter, createWebHistory } from 'vue-router'
// 1. 상대경로 2. 절대경로
import HomeView from '@/views/HomeView.vue'
import UserView from '@/views/UserView.vue'
import LoginView from '@/views/LoginView.vue'

import UserHome from '@/components/UserHome.vue'
import UserPosts from '@/components/UserPosts.vue'
import UserProfile from '@/components/UserProfile.vue'

// 로그인 상태가 true
const isAuthenticated = true


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue'),
    },
    {
      path: '/user/:id', // url
      component: UserView, // views 디렉토리
      // beforeEnter : 라우트 가드
      beforeEnter: (to, from) => {
        console.log(from)
        console.log(to)
      },
      // components 디렉토리
      children: [
        {path: '', name: 'user', component: UserHome}, // http://localhost:5173/user/:id
        {path: 'profile', name: 'user-profile', component: UserProfile}, // http://localhost:5173/user/:id/profile
        {path: 'posts', name: 'user-posts', component: UserPosts}, // http://localhost:5173/user/:id/posts
      ]
    },
    {
      path: '/login', // url
      name: 'login', 
      component: LoginView, // views 디렉토리
      beforeEnter: (to, from) => {
        if (isAuthenticated === true) {
          console.log('이미 로그인 상태입니다.')
          // 내가 로그인 버튼 눌렀는데 이미 로그인되어있는 상태라면 -> 홈으로 이동
          return {name: 'home'}
        }
      }
    },
  ],
})

export default router
