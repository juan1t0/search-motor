from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('<str:word>/results/', views.results, name='results'),
  path('papers/<str:id>/', views.see_paper, name='papers'),
]