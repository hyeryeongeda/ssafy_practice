<template>
  <div>

    <h1>LogIn Page</h1>

    <!-- form태그에 아이디, 패스워드 입력하고 로그인 버튼을 누른다 -> logIn함수가 실행-->
    <form @submit.prevent="logIn">
      <label for="username">아이디 : </label> <br>
      <input type="text" id="username" v-model.trim="username"> <br>

      <label for="password">패스워드 : </label> <br>
      <input type="password" id="password" v-model.trim="password"> <br>

      <input type="submit" value="로그인">

    </form>

  </div>

</template>

<script setup>
  import { ref } from 'vue';
  import { useAccountStore } from '@/stores/accounts';

  const accountStore = useAccountStore()

  const username = ref(null)
  const password = ref(null)

  // logIn 함수 실행되면 피냐의 logIn함수가 실행(username, password를 인자로 넘긴다)
  const logIn = function () {
    const payload = {
      username : username.value,
      password : password.value,
    }
    accountStore.logIn(payload)
  }

</script>

<style>

</style>
