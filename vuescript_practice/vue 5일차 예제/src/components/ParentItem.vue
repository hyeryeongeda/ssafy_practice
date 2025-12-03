<template>

  <p>{{ myProp.id }}</p>
  <p>{{ myProp.name }}</p>

</template>

<script setup>

  //  my-prop(케밥케이스) -> myProp(카멜케이스)
  defineProps({
    myProp: Object
  })

</script>

<style scoped>


</style>