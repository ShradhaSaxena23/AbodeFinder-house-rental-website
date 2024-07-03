from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage,name="home_page"),
    path('about', views.about,name="about_page"),
    path('add_home', views.add_home, name="add_home_page"),
    path('detail_page/<slug:slug>/', views.detail_page, name='detail_page'),
    path('signin_page', views.signin_page, name="signin_page"),
    path('login_page', views.login_page, name="login_page"),
    
    path('logout_page', views.logout_page, name="logout_page")
]