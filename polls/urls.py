from django.urls import path
from . import views

urlpatterns = [
    path('', views.index), # 기본 URL에서 index 뷰를 호출
    path('good/<str:name>/', views.good),  # good 뷰를 호출
    # path('debug/', views),  # debug 뷰를 호출
    path("debug/", views.debug_request),  # /polls/debug/ 로 접속
]
#url이 어떻게 뷰로 연결되는지 원리를 이해.