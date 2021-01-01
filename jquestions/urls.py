from django.urls import path
from jquestions import views

app_name = 'jquestions'

urlpatterns = [
    path('jq1/', views.jqview, name='jq1'),
    path('jq/<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    path('create/', views.question_create, name='question_create'),
    path('jq/', views.JqView.as_view(), name='jq'),
]
