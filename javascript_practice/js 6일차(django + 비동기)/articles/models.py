from django.db import models
from django.conf import settings

# Create your models here.
class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    # M : N 관계
    # 역참조 : user.article_set(1. user가 작성한 게시글 2. user가 좋아요 누른 게시글 --> 충돌)
    # related_name = 'like_articles'
    like_users = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name = 'like_articles'
    )
    
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(blank=True)

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# ORM
# DB는 SQL쿼리로 조작
# Django는 python
# : python 코드를 SQL쿼리로 변환해주는 도구
# 왜 ORM을 쓸까?
# 우리 사용하는 Django는 python // DB는 SQL
# QuerySet API
# : 이 구문을 사용하면 DB에 데이터를 접근하고, 조작(CRUD)할 수 있다.
# ex) Article.obects.all()


# Create (객체생성)
# 1. 첫 번째 방법

# article = Board()
# article.title = 'first'
# article.content = 'hello'
# article.save()

# 2. 두 번째 방법

# article = Board(title = 'second', content = 'hi')
# article.save()

# 3. 세 번째 방법

# Board.objects.create(title = 'third', content = 'byebye')

# Q) 우리는 객체를 생성할 때 1번, 2번, 3번 방법
# 몇번 방법을 써야할까?? // 몇번 방법을 지양해야할까??
# 3번 방법은 지양, 왜??
# 객체를 저장하기전에 데이터를 검증하고 그다음에 save()
# 검증단계 : 유효성 검사(validation check)... 등등


# Read (조회)

# 1. 전체 조회

# Board.objects.all()

# 2. 특정 조건으로 데이터 조회(filter)
# Board.objects.filter(title = 'first')
# Board.objects.filter(content__contains='he')
# Board.objects.filter(title__startswith='f')

# 조회한 객체가 없을경우 예외 발생 X

# 3. 단일 데이터 조회(get)
# Board.obejects.get(pk=1)
# Board.obejects.get(title='first')

# Board.obejects.get(title='fir') ---> 에러

# 조회한 객체가 없을경우 예외 발생 O
# 조회하는 객체가 두개 이상이다. 예외 발생 O
# 고유성을 보장하는 조회.

# Update (수정)
# article = Board.objects.get(pk=1)
# article.title = 'first1'
# article.save()


# Delete (삭제)

# article = Board.objects.get(pk=1)
# article.delete()

# 만약 새로운 객체를 생성하면 pk=1로 생성되는게 아니라
# pk=4로 생성된다.

# 추가적으로 QuerySetAPI 공부는 Django 공식문서 확인인