from django.urls import path
from homes import views

app_name = 'homes'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('navera8e96fadc9fb10ede2d47018716d41fd.html/', views.NaverView.as_view(), name='naver'),
    path('test/', views.TestView.as_view(), name='test'),
    path('add/', views.QuestionView.as_view(), name='question'),

    path('g1/', views.T1View.as_view(), name='t1'),
    path('g2/', views.T2View.as_view(), name='t2'),
    path('g3/', views.T3View.as_view(), name='t3'),
    path('g4/', views.T4View.as_view(), name='t4'),
    path('g5/', views.T5View.as_view(), name='t5'),
    path('a1/', views.Q1View.as_view(), name='q1'),
    path('a2/', views.Q2View.as_view(), name='q2'),
    path('b1/', views.W1View.as_view(), name='w1'),
    path('b2/', views.W2View.as_view(), name='w2'),
]
