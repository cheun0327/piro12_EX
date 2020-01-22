import datetime
from django.shortcuts import render, redirect
from diary.models import Article

def list(request):
    start_date=datetime.datetime(2020, 1,18,7)
    end_date=datetime.datetime(2020, 1, 18, 8)
    queryset = Article.objects.all().filter(created_at__range=(start_date, end_date))
    # .all().order_by('-id') : id내림차순으로 정렬
    # 작성 시간으로 정렬
    # content내용으로 찾기 | content__icontains='abc'
    # title의 시작 문자열로 찾기
    return render(request,'list.html', {'articles':queryset})

def read(request, pk):
    article=Article.objects.get(id=pk)      # pk를 url에서 받아옴.
    return render(request, 'read.html', {'article': article})

def create(request):
    if request.method=='GET':
        return render(request, 'create.html', {})
    elif request.method=='POST':
        title=request.POST['title']
        #content입력 해도 되고 안해도 된다고 설정했으니까
        content=request.POST['content']
        article=Article.objects.create(title=title, content=content)
        # 글을 쓰고 제출하면 쓴 글 페이지로 넘어가는거 해주기 위해서
        # 객체 만드는 즉시 변수에 저장, return한다.

        return redirect('articles_read', article.id)
        # return render(request, 'read', ...)으로하면 url은 그대로인데 작성한 내용 있는 html파일 열린다.

def update(request, pk): # 어떤 글을 수정할 지 알아야하기 때문에 pk받아와야한다.
    article=Article.objects.get(id=pk)
    if request.method=='GET':
        return render(request, 'update.html', {'article':article})
    elif request.method=="POST":
        title=request.POST['title']
        content=request.POST['content']

        article.title=title
        article.content=content
        article.save()
        return redirect('articles_read', article.id)

def delete(request, pk):
    article=Article.objects.get(id=pk)
    if request.method=='GET':
        return redirect('articles_read', article.id)
    # 만약에 사용자가 url쓰다가 GET으로 삭제 페이지 가면 바로 삭제되기 때문에
    # GET에서는 delete기능 하면 안된다.
    # 예들들어 form으로 된 버튼을 누르면 POST요청 가서 그때 삭제되야한다.
    elif request.method=='POST':
        article.delete()
        return redirect('articles_list')
