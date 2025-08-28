from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Memo
from .forms import MemoModelForm
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib import messages

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
    """모든 메모 목록 - 누구나 볼 수 있음"""
    memos = Memo.objects.all()
    return render(request, 'polls/memo_list.html', {'memos': memos})

@login_required
def memo_list(request):
    """내 메모만 보기"""
    memos = Memo.objects.filter(author=request.user)
    return render(request, 'polls/memo_list.html', {
        'memos': memos,
        'title': '내 메모'
    })

# def memo_list(request):
#     """
#     메모 목록 보기.
#     로그인 시 자신의 메모만, 비로그인 시 모든 메모를 보여줍니다.
#     """
#     if request.user.is_authenticated:
#         # 사용자가 로그인한 경우
#         memos = Memo.objects.filter(author=request.user)
#         title = f"{request.user.username}님의 메모"
#     else:
#         # 사용자가 로그인하지 않은 경우
#         memos = Memo.objects.all()
#         title = "모든 메모"

#     return render(request, 'polls/memo_list.html', {
#         'memos': memos,
#         'title': title
#     })


@login_required  # 로그인해야 작성 가능
def memo_create(request):
    """메모 작성 - 로그인 필수"""
    if request.method == 'POST':
        form = MemoModelForm(request.POST)
        if form.is_valid():
            memo = form.save(commit=False) # 일단 멈춤춤
            memo.author = request.user  # 작성자 자동 저장!
            memo.save()
            messages.success(request, '메모가 작성되었습니다.')
            return redirect('polls:memo_detail', pk=memo.pk)
    else:
        form = MemoModelForm()

    return render(request, 'polls/memo_form.html', {'form': form})

# def memo_create(request):
#     if request.method == "POST":   # 사용자가 저장 버튼 눌렀을 때
#         form = MemoForm(request.POST)   # 입력된 데이터 담기
#         if form.is_valid():             # 데이터가 올바르면
#             form.save()                 # DB에 저장
#             return redirect('polls:memo_list') # 저장 후 메모 목록 페이지로 이동
#     else:
#         form = MemoForm()  # 처음 들어올 때는 빈 폼

#     return render(request, 'polls/memo_create.html', {'form': form})

    # 아래가 원래 코드 
    # if request.method == 'POST':
    #     title = request.POST.get('title', 'no_title')
    #     content = request.POST.get('content', 'no content')
    #     is_important = request.POST.get('is_important') == 'on'
    #     Memo.objects.create(title=title, content=content, is_important=is_important)
    #     return redirect('polls:memo_list')
    # else:
    #     return render(request, 'polls/memo_create.html')

@login_required
def memo_update(request, pk):
    """메모 수정 - 작성자만 가능"""
    memo = get_object_or_404(Memo, pk=pk)

    # 작성자 확인
    if memo.author != request.user:
        messages.error(request, '자신의 메모만 수정할 수 있습니다.')
        return redirect('polls:memo_detail', pk=pk)

    if request.method == 'POST':
        form = MemoModelForm(request.POST, instance=memo)
        if form.is_valid():
            form.save()
            messages.success(request, '메모가 수정되었습니다.')
            return redirect('polls:memo_detail', pk=pk)
    else:
        form = MemoModelForm(instance=memo)

    return render(request, 'polls/memo_form.html', {
        'form': form,
        'is_update': True
    })




@login_required
def memo_delete(request, pk):
    """메모 삭제 - 작성자만 가능"""
    memo = get_object_or_404(Memo, pk=pk)

    # 작성자 확인
    if memo.author != request.user:
        raise PermissionDenied('삭제 권한이 없습니다.')

    if request.method == 'POST':
        memo.delete()
        messages.success(request, '메모가 삭제되었습니다.')
        return redirect('polls:memo_list')

    return render(request, 'polls/memo_confirm_delete.html', {'memo': memo})

def memo_detail(request, pk):
    """메모 상세 보기 - 누구나 볼 수 있음"""
    memo = get_object_or_404(Memo, pk=pk)
    return render(request, 'polls/memo_detail.html', {'memo': memo})

def page1(request):
    return render(request, 'polls/page1.html')