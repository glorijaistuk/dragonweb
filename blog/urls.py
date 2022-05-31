from django.urls import path
from . import views

urlpatterns = [
    path("", views.loginPage, name="login"),
    path("register/", views.registerPage, name="register"),
    
    path("pocetna-stranica",views.HomeView.as_view(), name="pocetna-stranica"),
    path("community",views.CommunityView.as_view(), name="community"),
    path("support",views.SupportView.as_view(), name="support"),
    
    path("logout/", views.logoutUser, name="logout"),
    
]


