from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_expense, name="add_expense"),
    path("view/", views.view_expenses, name="view_expenses"),
]