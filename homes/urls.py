from django.urls import path
from homes import views

app_name = 'homes'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('navera8e96fadc9fb10ede2d47018716d41fd.html/', views.NaverView.as_view(), name='naver'),
    path('test/', views.TestView.as_view(), name='test'),
    path('jq1/', views.jqview, name='jq1'),
    path('jq/<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('question/create/', views.question_create, name='question_create'),
    path('add/', views.QuestionView.as_view(), name='question'),
    path('jq/', views.JqView.as_view(), name='jq'),
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
