from django.urls import path, include   
from . import views
# 원하는 뷰를 가져오는 형태
# from .views import index, memo_list, one_memo, memo_create,page1
# from polls import views
# from polls.views import lion, dubug_request

app_name = 'polls' 

urlpatterns = [
    path('', views.index, name='index'),
    path('memo/', views.memo_list, name="memo_list"),
    path('memo/<int:pk>/', views.memo_detail, name="memo_detail"),
    path('memo/create/', views.memo_create, name='memo_create'),
    path('accounts/', include('accounts.urls')),  #로그인
    path('memo/<int:pk>/delete/', views.memo_delete, name='memo_delete'),
]
