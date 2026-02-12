from django.urls import path
from . import views
urlpatterns = [
    path("", views.add,name="add"),
    path("", views.delete,name="delete"),
    path("", views.update,name="update"),
    path("", views.checkout,name="checkout"),
]