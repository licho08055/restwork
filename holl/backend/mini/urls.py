from django.urls import path
from .views import alter_view,detail_view,create_view, List_VIew,Detail_View,MixinsView


urlpatterns=[
    path('', MixinsView.as_view()),
    path('<int:pk>/',   MixinsView.as_view()),
    path('create/',  MixinsView.as_view()),
    path('<int:pk>/update/',  MixinsView.as_view()),
    path('<int:pk>/delete/',  MixinsView.as_view()),
]