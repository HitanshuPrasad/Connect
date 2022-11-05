from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('signup_client/',views.signup_client,name="signup_client"),
    path('signup_professional/',views.signup_professional,name="signup_professional"),
    
    path('login_client/',views.login_client,name="login_client"),
    path('login_professional/',views.login_professional,name="login_professional"),
    
    path('logout/',views.Logout,name="logout"),
    
    path('profile_client/',views.profile_client,name="profile_client"),
    path('profile_professional/',views.profile_professional,name="profile_professional"),
    
    path('home_professional/',views.home_professional,name="home_professional"),
    path('home_client/',views.home_client,name="home_client"),
        
    path('search_client/',views.search_client,name="search_client"),
    path('search_professional/',views.search_professional,name="search_professional"),
  
]