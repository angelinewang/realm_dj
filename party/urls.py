from django.urls import path
from . import views

urlpatterns = [
    path('post/<int:pk>/', views.PartyPost.as_view()),  # POST only

    # Used as: Precursor to createinvite/ API
    # Grabs party_id of latest party associated to user
    path('myparties/<int:pk>/', views.MyPartiesView.as_view()) 
]
