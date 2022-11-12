from django.urls import path

from . import views

urlpatterns = [
    path('signup/', views.RegisterView.as_view()), # POST only
    path('login/', views.LoginView.as_view()), # GET & POST 
    path('profile/', views.ProfileDetail.as_view()), # GET & POST 
    path('guests/', views.GuestsList.as_view()), # GET only 
]
