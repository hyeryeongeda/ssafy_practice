<template>

    <div>
        <RouterLink :to="{ name: 'user-profile'}">Profile</RouterLink>
        <RouterLink :to="{ name: 'user-posts'}">Posts</RouterLink>

        <h1>UserView</h1>
        <h2>{{ userId }}번의 User 페이지</h2>

        <button @click="goHome">Home</button>

        <button @click="routeUpdate"> 99번의 유저 페이지 </button>
    </div>    

    <!-- 페이지가 랜더링 -->
    <RouterView/>

</template>


<script setup>

    import { ref } from 'vue'

    import { RouterLink, RouterView } from 'vue-router'

    // useRoute: read-only , useRouter: 라우트 전환을 위한 API
    import { useRoute, useRouter } from 'vue-router'
    // 가드 Leave : 페이지 나갈때, Update : 페이지 url 변경 될 때
    import { onBeforeRouteLeave, onBeforeRouteUpdate } from 'vue-router'

    const route = useRoute()
    const router = useRouter()

    const userId = ref(route.params.id)

    const goHome= function() {
        // push? replace? 차이
        // push : 히스토리에 추가 되기때문에 이전페이지로 돌아갈 수 있음(뒤로가기됨)
        // replace : 히스토리에 추가되지 않기때문에 이전페이지로 돌아갈 수 없음(뒤로가기안됨)
        router.replace({name: 'home'})
    }

    const routeUpdate = function() {
        router.push({ name:'user', params: {id:99}})
    }

    // from: 1번 유저 -> to: 99번 유저 
    onBeforeRouteUpdate((to, from) => {
        userId.value = to.params.id
    })

    // 홈페이지로 이동할때(페이지 나갈때) -> 이 페이지를 정말 나가시겠습니까?
    onBeforeRouteLeave((to, from) => {
        // alert <-> confirm 차이
        // confirm은 yes or no 선택
        const answer = window.confirm('이 페이지를 정말 나가시겠습니까?')
        if (answer === false) {
            return false // 페이지 이동 X
        }
    })


</script>


<style scoped>


</style>