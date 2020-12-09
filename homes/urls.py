from django.urls import path
from homes import views

app_name = 'homes'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('test/', views.TestView.as_view(), name='test'),
    path('add/', views.QuestionView.as_view(), name='question'),
]
