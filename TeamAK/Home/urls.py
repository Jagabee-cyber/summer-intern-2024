from django.urls import path
from . import views

urlpatterns = [
    path("", views.login, name="login"),
    path("createAccount/", views.createAccount, name="createAcc"),
    path("addProject/", views.addProject, name='addProj')
]