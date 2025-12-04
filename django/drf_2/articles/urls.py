from django.contrib import admin
from django.urls import path
from articles import views

# app_name = ? # 할필요 없다 왜? template 안쓸거니까

urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
    # 전체 댓글 조회
    path('comments/', views.comment_list),
    path('comments/<int:comment_pk>/', views.comment_detail),
    path('articles/<int:article_pk>/comments/', views.comment_create),
]
