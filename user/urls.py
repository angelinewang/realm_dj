from django.urls import path

from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    path('signup/', csrf_exempt(views.RegisterView.as_view())), # POST only
    path('login/', csrf_exempt(views.LoginView.as_view()),), # GET & POST 
    path('profile/<int:pk>/', views.ProfileDetail.as_view()), # GET & POST 
    path('guests/browse/<int:pk>/', views.GuestsBrowse.as_view()), # GET only, when user state is guest
    # User state is evaluated in the backend, if user is guest, get all users not himself, if user is host, get all users not himself and not already a guest_id tied to an invite tied to the host's most recent party entry 
#     # GET only, when user state is guest
#     path('guests/browse/<int:pk>/hostmode', views.GuestsBrowseHostMode.as_view()),
] 
# ]
