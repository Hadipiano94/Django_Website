from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name='home'),
    path("list/", views.tdlist, name='list'),
    path("create/", views.create, name='create'),
    path("<str:name>/", views.show_tels, name='show_tels'),
    path("telephones/", views.show_tels, name='show_all_tels'),
]
