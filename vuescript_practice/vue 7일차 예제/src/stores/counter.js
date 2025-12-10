import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useCounterStore = defineStore('counter', () => {

  // === state 영역 ===

  // 할일의 pk값(id값)
  let id = 0
  // 할일의 목록 todo
  const todos = ref([])

  // === action 영역 ====
  // create
  const addTodo = function (todoText) {
    todos.value.push({
      id: id++,
      text: todoText, // 사용자가 작성한 일
      isDone: false // 완료 여부
    })
  }
  
  // update(취소선-할일체크)
  const updateTodo = function (todoId) {
    // forEach와 map의 차이? -> map은 배열을 순회하면서 새로운 배열을 반환
    todos.value = todos.value.map((todo) => {
      if (todo.id === todoId) {
        // false -> true, true -> false
        todo.isDone = !todo.isDone
      }
      return todo
    })

  }

  const deleteTodo = function (todoId) {
    // 마우스로 클릭한 항목의 인덱스를 index변수에 할당
    const index = todos.value.findIndex((todo) => todo.id === todoId)
    // index 번째의 항목을 제거 -> splice
    todos.value.splice(index, 1) // 1개 제거
  }


  // === getter 영역 ===
  // computed : 완료된 할일의 개수를 계산
  const doneTodoCount = computed(() => {
    // isDone이 true인것만 모아서 새 배열을 만들기 (filter)
    const doneTodos = todos.value.filter((todo) => todo.isDone)
    // 배열의 길이를 반환
    return doneTodos.length
  })



  return { todos, addTodo, doneTodoCount, updateTodo, deleteTodo }
}, {persist: true}) // 새로고침해도 데이터 유지
