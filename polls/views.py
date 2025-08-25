# polls/views.py에 간단한 뷰 작성
from django.http import HttpResponse

# 장고 페이지 구성의 핵심심
from django.shortcuts import render
from .models import Article, Memo


# index에서 context 만들어서 보내기
def index(request):
    memos = Memo.objects.all()
    context = {
        "name": "tori",
        "title": "장고 학습",
        "memos": memos
    }
    return render(request,"polls/index.html",context=context)


# def blog_list(request):
#     return render

# def index(request):
#     return HttpResponse("안녕, polls!")

def lion(request):
    return HttpResponse("<hi>안녕.</hi>")


def good(request, name):
    return HttpResponse(f"{name}가 장고를 배웁니다!") 



#내가 request라는 객체가 생소한데, 안에 어떤 내용들이 있는지 확인해보고싶어. 
#이거를 하나의 뷰로 만들어서 웹에 표시해볼까?
#디버그 하는 역할이네 -> debug_request으로 이름짓자.

def debug_request(request):
    return HttpResponse("debug view")


def memo_list(self) :
  # 메모전체 가져오기
  # content 구성하기기
  return HttpResponse("작업중")







#view 만들기
# polls에 urls.py 작성
# path("경로", 뷰함수)

# config.urls.py
# path("아무거나경로", inclued(polls.urls))

# 브라우저에서 확인