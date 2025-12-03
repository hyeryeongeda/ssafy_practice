<template>

  <h1>App.vue</h1>
  <!-- 자식컴포넌트 -->
  <!-- self-closing 태그 -->
  <MyComponent/>

</template>

<!-- createApp함수의 setup함수와 같은 기능 -->
<!-- 차이점 : return이 없다 -->

<script setup>
  // 컴포넌트를 불러오는 방법 2가지
  // 1. 상대경로 - 잘 안쓴다
  // import MyComponent from './components/MyComponent.vue';
  // 2. src를 별칭 : @
  import MyComponent from '@/components/MyComponent.vue';

</script>


<!-- scoped : App.vue 안에서만 style(css)가 적용될수 있게 -->
<style scoped>

  h1 {
    color: red;
  }

</style>


