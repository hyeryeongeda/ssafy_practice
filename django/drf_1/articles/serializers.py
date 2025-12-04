from rest_framework import serializers

from .models import Article

# 홈페이지에서 쓸 시리얼라이저라 created_at, updated_at이 필요 없다.
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # 직렬화 하고자 하는 필드를 지정
        fields = (
            'id',
            'title',
            'content',
        )

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'