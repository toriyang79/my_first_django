from django.urls import path
# from . import views
# 원하는 뷰를 가져오는 형태
from .views import lion, dubug_request
# from polls import views
# from polls.views import lion, dubug_request

urlpatterns = [   
    path('tiger/<str:name>/', lion),
    path('debug/', dubug_request)
]
# url이 어떻게 뷰로 연결되는지 원리를 이해.
