from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    # on_delete=models.CASCADE : 만약 회원이 탈퇴하면 게시글도 함께 삭제된다
    # Many-to-one 관계가 성립
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True)
    # User가 작성한 게시글 : user.article_set (역참조)
    # User가 좋아요 누른 게시글 : user.like_artilces
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name = "like_articles"
    )

class Comment(models.Model):
    # 게시글과 댓글 관계 (Many-to-one), 게시글 삭제되면 댓글도 삭제
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # 작성자(회원)과 댓글 관계 (Many-to-one), 회원 탈퇴하면 댓글도 삭제
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
