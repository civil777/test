from django.urls import path
from homes import views

app_name = 'homes'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('test/', views.TestView.as_view(), name='test'),
    path('add/', views.QuestionView.as_view(), name='question'),
    path('g1/', views.T1View.as_view(), name='t1'),
    path('g2/', views.T2View.as_view(), name='t2'),
    path('g3/', views.T3View.as_view(), name='t3'),
    path('g4/', views.T4View.as_view(), name='t4'),
    path('g5/', views.T5View.as_view(), name='t5'),
]
