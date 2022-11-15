from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.PartyPost.as_view()),  # POST only
]
