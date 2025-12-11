from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

# from .models import User
# 직접 참조

# 간접 참조
# get_user_model ---> 커스텀 User 모델을 자동을 변환
# User 모델을 변경하더라도 폼을 수정할 필요가 없다.

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        # model = User # 직접 참조
        model = get_user_model() # 간접참조

class CustomUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        # 모든 필드가 다 조회
        model = get_user_model()
        # 정보 변경할 필드만 가져오기
        fields = ('first_name', 'last_name', 'email')