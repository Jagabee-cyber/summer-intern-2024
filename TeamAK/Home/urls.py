from django.urls import path
from . import views
from .views import login_view

urlpatterns = [
    path("", views.show_login_page, name="loginPage"),
    path("createAccount/", views.createAccount, name="createAcc"),
    path("addProject/", views.addProject, name='addProject'),
    path("mainSelection/", views.mainSelection, name='mainSelec'),
    #path('google-redirect/', google_oauth_redirect, name='google_oauth_redirect'),
    path('landingPage/', views.landingPage, name='landingPage'),
    #path('login/', firebase_login, name='firebase_login'),
    path('login/', views.login_view, name='login'),
    path("galleryPage/", views.galleryPage, name='galleryPage'),
    path("viewProject/", views.viewProject, name='viewProject')
]