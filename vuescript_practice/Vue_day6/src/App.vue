<template>
  <header>
    <div class="wrapper">
      <nav>
        <!-- RouterLink : html의 a태그와 비슷하지만 차이점 - 페이지의 새로고침 없이 SPA방식으로 페이지 전환 -->
        <!-- :to="" 속성으로 이동할 경로를 지정 -->
        <RouterLink :to="{name: 'home'}">Home</RouterLink>
        <RouterLink :to="{name: 'about'}">About</RouterLink>
        <RouterLink :to="{name: 'user', params: {id: userId}}">User</RouterLink>
        <RouterLink :to="{name: 'login'}">Login</RouterLink>
      </nav>
    </div>

  </header>

  <!-- RouterView : 페이지가 랜더링되는 위치 -->
  <RouterView />
</template>


<script setup>

  import { RouterLink, RouterView } from 'vue-router'
  import { ref } from 'vue'
  const userId = ref(1)

</script>



<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
