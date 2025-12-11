import { defineStore } from 'pinia'
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import axios from 'axios'

export const useAccountStore = defineStore('account', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const token = ref(null)

  const router = useRouter()

  // 회원가입
  const signUp = function (payload) {
    const username = payload.username
    const password1 = payload.password1
    const password2 = payload.password2
    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username: username,
        password1: password1,
        password2: password2,
      }
    })
      .then((res) => {
        console.log('회원가입 완료')
        const password = password1
        logIn({username, password})
      })
      .catch((err) => {
        console.log(err.response.data)
      })

  }

  // 로그인
  // 로그인 버튼 누르고 username과 password 인자로 넘겼다.
  const logIn = function (payload) {
    // 구조분해 할당
    const { username, password } = payload

    axios ({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then(res => {
        // console.log(res.data)
        console.log("로그인이 되었습니다.")
        token.value = res.data.key
        // 홈페이지로 이동
        router.push({name: 'ArticleView'})
      })
      .catch(err => console.log(err))
    }

    const isLogin = computed(() => {
      // 토큰이 있으면(로그인되었으면) true 반환, 아니면 false 반환
      return token.value? true : false
    })

    const logOut = function() {
      axios ({
        method: 'post',
        url: `${API_URL}/accounts/logout/`
      })
       .then(res => {
          // 로그아웃
          token.value = null
          // 로그인 페이지로 이동
          router.push({name: 'LogInView'})
       })
       .catch(err => console.log(err))
    }
  
  // 페이지 전환과 관련해서 로그인 여부 isLogin -> 라우터(index.js) 소스코드에 사용하려고
  return { signUp, logIn, token, isLogin, logOut }
}, { persist: true })