from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST

# 현재 디렉토리의 models.py로 부터 Board 모델을 가져오겠다. 
from .models import Article, Comment

def index(request):
    # QuerySetAPI ---> Read, 전체 데이터 조회 : Board.objects.all()
    articles = Article.objects.all()

    context = {
        'articles' : articles,
    }

    return render(request, 'articles/index.html', context)

def detail(request, pk):
    # QuerySet API : 단일 데이터 조회 : get
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    # 별표 다섯개!!!! 역참조
    comments = article.comment_set.all()
    context = {
        'article' : article,
        'comment_form' : comment_form,
        'comments' : comments,
    }

    return render(request, 'articles/detail.html', context)


from .forms import ArticleForm, CommentForm

@require_http_methods(['GET', 'POST'])
def create(request):
    # GET 방식 : url에 노출 --- 데이터 조회, 검색
    # POST 방식 : url에 노출 x(보안성) --- 데이터 생성, 수정, 삭제
    # POST방식이 짱이지만 GET방식을 쓰는 이유
    # GET방식에 비해 POST방식 훨씬 복잡하다. : ex) (csrf토큰) - (보안토큰)
    
    # 내가(클라이언트가) 게시글 생성 버튼(submit버튼)을 눌렀을 때
    if request.method == 'POST':
        # request.POST : 클라이언트가 POST방식으로 전송한 폼데이터
        # request.FILES : 클라이언트가 업로드한 모든 파일
        form = ArticleForm(request.POST, request.FILES)
        # 유효성 검사
        if form.is_valid(): # 유효성 검사에 성공
            # DB에 바로 저장 ---> request.user정보(중간 단계를 거쳐 저장)
            article = form.save(commit=False)
            # 로그인한 사용자(request.user)
            article.user = request.user
            # DB에 저장
            article.save()  
            # 데이터가 변경 되었기 때문에 redirect
            return redirect('articles:detail', article.pk)

    # 버튼 누르기 전에 or 다른 버튼을 눌렀을떄(다른 method)
    else:
        form = ArticleForm()
    # GET요청일때(+실패 했을 때)
    # 빈 폼
    context = {
        'form' : form
    }
    return render(request, 'articles/create.html', context)


# 단일 게시글 조회 후 삭제
@login_required
@require_POST
def delete(request, pk):
    # 게시글 조회 후 삭제
    article = Article.objects.get(pk=pk)
    # 내가 쓴 글만 내가 삭제할 수 있다.
    if request.user == article.user:
        article.delete()

    return redirect('articles:index')


# 페이지 렌더링 + 리다이렉트(create와 차이 : 기존에 있던 게시글을 변경)
@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    # request.user : 현재 로그인 되어있는 유저
    # article.user : 게시글을 작성한 유저
    if request.user == article.user:
        # submit 버튼 눌렀을떄
        if request.method == 'POST':
            # 기존 게시글의 데이터(instanc=article)
            form = ArticleForm(request.POST, request.FILES, instance=article)
            # 유효성 검사
            if form.is_valid():
                form.save() # 유효성 검사 성공하면 DB에 저장
                # 데이터 변경 되었으니 redirect
                return redirect('articles:detail', article.pk)
        # submit 버튼을 누르기전 or 다른버튼 눌렀을 때
        else:
            # 기존의 게시글의 글
            form = ArticleForm(instance=article) 
    # 게시글을 작성하지않은 다른 사용자가 update 버튼을 눌렀을떄
    else:
        return redirect('articles:index')
    # GET요청일떄
    context = {
        'article' : article,
        'form' : form,
    }
    return render(request, 'articles/update.html', context)



@login_required
@require_POST
def comments_create(request, pk):
    # 게시글 조회
    article = Article.objects.get(pk=pk)
    # 댓글 조회
    comment_form = CommentForm(request.POST)
    # 유효성 검사 성공
    if comment_form.is_valid():
        # commit = False : DB에 바로 저장하지않고 추가 작업 후 저장
        comment = comment_form.save(commit=False)
        # 참조 1. 게시글 객체
        comment.article = article
        # 2. 로그인한 사용자(request.user)
        comment.user = request.user
        comment.save()
        return redirect('articles:detail', article.pk)
    # 유효성 검사 실패
    context = {
        'article' : article,
        'comment_form' : comment_form
    }
    return render(request, 'articles/detail.html', context)

@login_required
@require_POST
def comments_delete(request, article_pk, comment_pk):
    comment = Comment.objects.get(pk=comment_pk)
    # 로그인사용자 == 댓글작성한유저
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail', article_pk)

from django.http import JsonResponse

@login_required
def likes(request, article_pk):
    # 단일 게시글 조회
    article = Article.objects.get(pk=article_pk)
    # 좋아요 <-> 좋아요 취소
    # 현재 로그인한 user가 이미 좋아요를 눌렀다면
    if request.user in article.like_users.all():
        # 좋아요 취소(user를 제거)
        article.like_users.remove(request.user)
        is_liked = False
    else:
        # 좋아요 추가(user를 추가)
        article.like_users.add(request.user)
        is_liked = True
    
    context = {
        'is_liked': is_liked
    }
    return JsonResponse(context)
    