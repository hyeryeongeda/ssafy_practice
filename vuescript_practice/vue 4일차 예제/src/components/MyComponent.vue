<template>

  <div>
    <h1>MyComponent.vue</h1>
  </div>

  <MyComponentItem/>
  <MyComponentItem/>
  <MyComponentItem/>

</template>


<script setup>

  import MyComponentItem from '@/components/MyComponentItem.vue';

</script>


<style scoped>

  h1 {
    color: aqua;
  }

</style>