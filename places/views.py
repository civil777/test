from django.views.generic import ListView, DetailView
from django.core.paginator import Paginator
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 8

    ordering = "created"
    context_object_name = "places"


class RoomDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Room


