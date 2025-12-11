<template>

  <ParentChild
    @emit-args="getNumbers"
    @some-event="someCallback"
    @update-name="updateName"
    my-msg="message"
    :dynamic-props="name"
  />

  <ParentItem
    v-for="item in items"
    :key="item.id"
    :my-prop="item"
  />


</template>

<script setup>

  
  import {ref} from 'vue'
  import ParentChild from '@/components/ParentChild.vue';
  import ParentItem from '@/components/ParentItem.vue';

  const name = ref('Bob')

  const items = ref([
    {id: 1, name: '사과'},
    {id: 2, name: '샤인머스켓'},
    {id: 3, name: '블루베리'},
  ])

  // 추가인자로 1, 2, 3 emit했음
  // 1, 2, 3 -> ...args -> [1, 2, 3]
  const getNumbers = function(...args) {
    alert(`ParentChild 발신한 추가인자 ${args} 수신했다.`)
  }

  const someCallback = function() {
    alert('ParentChild가 발신한 이벤트 수신했다.')
  }

  const updateName = function() {
    name.value = 'Bella'
  }

</script>

<style scoped>


</style>