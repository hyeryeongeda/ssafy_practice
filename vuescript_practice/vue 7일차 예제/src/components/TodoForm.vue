<template>

  <div>
    <!-- 할일 추가 할때마다 새로고침 막기(prevent) -->
    <form @submit.prevent="createTodo(todoText)" ref="formElem">
      <!-- 양방향 바인딩 -->
      <input type="text" v-model="todoText">
      <input type="submit">
    </form>
  </div>

</template>


<script setup>
  import {ref} from 'vue'
  import { useCounterStore } from '@/stores/counter';
  const store = useCounterStore()
  // 할일
  const todoText = ref('')
  const formElem = ref(null)

  // create함수
  const createTodo = function(todoText) {
    // 중앙저장소의 addTodo함수 가져오기
    store.addTodo(todoText)
    // 할일 추가 될때마다 폼 초기화
    formElem.value.reset()
  }

</script>

<style scoped>


</style>