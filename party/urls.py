from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:pk>/', views.PartyPost.as_view()),  # POST only
]
