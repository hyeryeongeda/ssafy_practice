<template>
  <header>
    <nav>
      <RouterLink :to="{ name : 'ArticleView'}"> 전체 게시글</RouterLink>
    </nav>
  </header>
  <RouterView />
</template>

<script setup>
  import { RouterView, RouterLink } from 'vue-router'
</script>

<style scoped>
</style>
