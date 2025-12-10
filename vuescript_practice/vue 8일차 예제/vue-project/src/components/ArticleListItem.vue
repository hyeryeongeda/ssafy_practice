<template>
  <div>
    <h5> {{ article.id }}</h5>
    <p>{{ article.title }}</p>
    <p>{{ article.content }}</p>
    <!-- 상세페이지 버튼 -->
    <RouterLink :to="{ name: 'DetailView', params: {id: article.id}}">
      [DETAIL]
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>

  defineProps({
    article: Object
  })

  import { RouterLink } from 'vue-router';
  
</script>
