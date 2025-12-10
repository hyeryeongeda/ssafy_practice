// store/articles.js

import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

import axios from 'axios'

export const useArticleStore = defineStore('article', () => {
  
  // === state 영역 ====

  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'

  // === action 영역 ===
  const getArticles = function() {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`
    })
      .then(res =>{
        articles.value = res.data
      })
      .catch(err => console.log(err))
  }
  
  
  return { articles, API_URL, getArticles }
}, { persist: true })
