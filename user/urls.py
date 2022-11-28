from django.urls import path

from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('signup/', csrf_exempt(views.RegisterView.as_view())), # POST only
    path('login/', csrf_exempt(views.LoginView.as_view()),), # GET & POST 
    path('profile/<int:pk>/', views.ProfileDetail.as_view()), # GET & POST 
    path('guests/browse', views.GuestsBrowse.as_view()), # GET only 
]
