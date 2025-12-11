<template>

  <div>

    <!-- :class -> 만약 true일 경우 class 선택자를 적용 -->
    <!-- .is-done 적용 -->
    <span @click="store.updateTodo(todo.id)" :class="{'is-done':todo.isDone}">
      {{ todo.text }}
    </span>

    <button @click="store.deleteTodo(todo.id)">Delete</button>
  </div>

</template>

<script setup>

  import { useCounterStore } from '@/stores/counter';

  const store = useCounterStore()

  defineProps({
    todo: Object
  })

</script>


<style scoped>
  /* 취소선 */
  /* 클래스 선택자 */
  .is-done {
    text-decoration: line-through;
  }
</style>
