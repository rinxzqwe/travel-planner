from django.urls import path
from . import views

app_name = "planner"

urlpatterns = [
    path("", views.index, name="index"),
    path("save/", views.save_preferences, name="save"),
    path("reset/", views.reset_preferences, name="reset"),
    path("countries/", views.countries_list, name="countries"),
]