from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework import status
from .models import Article, Comment
from .serializers import ArticleListSerializer, ArticleSerializer, CommentSerializer

from django.db.models import Count

# 404 : Not found
# 4xx : 클라이언트 에러
# 5xx : 서버 에러

from django.shortcuts import get_object_or_404, get_list_or_404

# object : 단일 객체 조회
# list : 전체 객체 조회 

@api_view(['GET', 'POST'])
def article_list(request):
    # 전체 게시글 조회
    if request.method == 'GET':
        articles = get_list_or_404(Article)
        # 모든 게시글 조회하고 ---> 직렬화
        # many=True : 여러개의 객체(다중데이터)일때
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        # request.data ---> title과 content
        serializer = ArticleSerializer(data=request.data)
        # raise_exception=True : 유효하지 않을 경우 예외 발생
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # 데이터 생성을 성공/실패 HTTP_201, HTTP_400
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            

# GET : 조회, DELETE : 삭제, PATCH : 일부 수정, PUT : 전체 수정
@api_view(['GET', 'DELETE', 'PATCH'])
def article_detail(request, article_pk):
    # 단일 게시글을 DB에서 조회
    # annotate() : "계산된 필드"를 추가하는 함수
    # Count('comment') : article에 연결된 comment개수를 세어주는 함수
    article = get_object_or_404(
        Article.objects.annotate(num_of_comments=Count('comment')),
        pk=article_pk
    )
    # 단일 게시글 조회
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)
    
    # 게시글 삭제
    if request.method == 'DELETE':
        article.delete()
        # 상태 코드 HTTP_204 : 성공하고, 반환할 콘텐츠가 없음 
        return Response(status = status.HTTP_204_NO_CONTENT)
    
    # 게시글 수정
    if request.method == "PATCH":
        # request.data : 클라이언트가 입력한 title 또는 content
        # partial=True : 부분 업데이트 허용
        serializer = ArticleSerializer(
            article, data=request.data, partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
            # raise_exception=True 때문에 아래처럼 소스코드를 작성 안해도 된다.
            # return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def comment_list(request):
    # 댓글이 하나도 없으면(DB가 비어있으면) 404에러
    comments = get_list_or_404(Comment)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

# 댓글 상세 페이지 ---> 생성X, 조회, 수정, 삭제
@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if request.method == 'GET': # 단일 댓글 조회
        serializer = CommentSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        # request.data : 우리가 postman에 입력한 content
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
@api_view(['POST'])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # request.data : 사용자가 입력한 content
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)