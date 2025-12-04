from django.urls import path

# . : 현재 디렉토리리
from . import views

# {% url namespace:name %}
# app_name = 'namespace'
app_name = 'articles'

urlpatterns = [
    # READ
    # 전체 게시글 조회
    path('', views.index, name = 'index'),
    # 단일 게시글 조회
    # variable routing <데이터타입:변수>
    path('<int:pk>/', views.detail, name = 'detail'),

    #CREATE
    # 랜더링 + 리다이렉트(views.py)
    path('create/', views.create, name = 'create'),

    # 단일 게시글 조회 후 삭제
    # variable routing
    path('<int:pk>/delete/', views.delete, name='delete'),

    #UPDATE
    #단일 게시글 조회 후 수정
    # variable routing
    # 페이지 렌더링 + 리다이렉트
    path('<int:pk>/update/', views.update, name='update'),

    path('<int:pk>/comments/', views.comments_create, name = 'comments_create'),
    path(
        '<int:article_pk>/comments/<int:comment_pk>/delete/',
        views.comments_delete,
        name = 'comments_delete'
    ),
    path('<int:article_pk>/likes/', views.likes, name = 'likes'),
]
