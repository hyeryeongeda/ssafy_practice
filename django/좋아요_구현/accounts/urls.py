from django.urls import path

# . : 현재 디렉토리리
from . import views

# {% url namespace:name %}
# app_name = 'namespace'
app_name = 'accounts'

urlpatterns = [
    path('login/', views.login, name = 'login'),
    path('logout/', views.logout, name = 'logout'),
    path('signup/', views.signup, name = 'signup'), # 회원가입
    # request : 이미 로그인 되어있는 user의 데이터
    path('delete/', views.delete, name = 'delete'), # 회원탈퇴
    path('update/', views.update, name = 'update'), # 회원정보변경
]
