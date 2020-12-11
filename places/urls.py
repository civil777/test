from django.urls import path
from . import views

app_name = "places"

urlpatterns = [
    path("<int:pk>/", views.RoomDetail.as_view(), name="detail"),
    path("", views.HomeView.as_view(), name="places"),
]
