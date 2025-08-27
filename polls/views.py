from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Memo
from .forms import MemoForm 

def index(request):
    return render(request, "polls/index.html")



def lion(request, name):
    return HttpResponse(f"{name}가 장고를 배웁니다!!")

def dubug_request(request):
    content = f"""이것이 request가 가지고 있는 정보의 예시입니다.<br>
    request.path = {request.path}    <br>
    request.method = {request.method}    <br>
    request.META.REMOTE_ADDR = {request.META.get('REMOTE_ADDR', 'Unknown')}    <br>
    """
    return HttpResponse(content)

def memo_list(request):
    memos = Memo.objects.all().order_by('-id')
    return render(request, 'polls/memo_list.html', {'memos': memos})

def memo_create(request):
    if request.method == "POST":   # 사용자가 저장 버튼 눌렀을 때
        form = MemoForm(request.POST)   # 입력된 데이터 담기
        if form.is_valid():             # 데이터가 올바르면
            form.save()                 # DB에 저장
            return redirect('polls:memo_list') # 저장 후 메모 목록 페이지로 이동
    else:
        form = MemoForm()  # 처음 들어올 때는 빈 폼

    return render(request, 'polls/memo_create.html', {'form': form})

    # 아래가 원래 코드 
    # if request.method == 'POST':
    #     title = request.POST.get('title', 'no_title')
    #     content = request.POST.get('content', 'no content')
    #     is_important = request.POST.get('is_important') == 'on'
    #     Memo.objects.create(title=title, content=content, is_important=is_important)
    #     return redirect('polls:memo_list')
    # else:
    #     return render(request, 'polls/memo_create.html')

def one_memo(request, memo_id):
    memo = Memo.objects.get(id=memo_id)
    return render(request, 'polls/memo_detail.html', {'memo': memo})

def page1(request):
    return render(request, 'polls/page1.html')
