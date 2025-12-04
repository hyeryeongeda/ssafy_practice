from django.shortcuts import render, redirect

# 현재 디렉토리의 models.py로 부터 Board 모델을 가져오겠다. 
from .models import Article

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

    context = {
        'article' : article
    }

    return render(request, 'articles/detail.html', context)


from .forms import ArticleForm

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
            article = form.save() # DB에 저장
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
def delete(request, pk):
    # QuerySetAPI
    article = Article.objects.get(pk=pk)
    article.delete()

    return redirect('articles:index')


# 페이지 렌더링 + 리다이렉트(create와 차이 : 기존에 있던 게시글을 변경)
def update(request, pk):
    article = Article.objects.get(pk=pk)

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
    # GET요청 일때
    context = {
        'article' : article,
        'form' : form
    }
    # 데이터 변경이 x
    return render(request, 'articles/update.html', context)