<template>

  <p> {{ myMsg }}</p>
  <p> {{ dynamicProps }}</p>

  <button @click="emitArgs">추가 인자 전달</button>

  <button @click="buttonClick">버튼 클릭</button>

  <!-- updateName는 emit 받은걸까? -->
  <!-- updateName 함수 -->
  <ParentGrandChild
    :my-msg="myMsg"
    @update-name="updateName"
  />

</template>

<script setup>

  import ParentGrandChild from '@/components/ParentGrandChild.vue';

  // 내려받은 props : defineProps
  // Parent의 my-msg : 케밥케이스
  // ParentChild myMsg : 카멜케이스
  defineProps({
    myMsg: String,
    dynamicProps: String,
  })

  // defineEmits : 이벤트 발신
  const emit = defineEmits(['emitArgs', 'someEvent', 'updateName'])

  const emitArgs = function () {
    emit('emitArgs', 1, 2, 3)
  }

  const buttonClick = function() {
    emit('someEvent')
  }

  const updateName = function () {
    emit('updateName')
  }

</script>

<style scoped>


</style>