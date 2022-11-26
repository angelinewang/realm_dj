from django.urls import path

from . import views

urlpatterns = [
    path('parties/invited', views.PartiesInvitedList.as_view()),  # GET & POST 

    # These 2 are used for both Invited cards and Confirmed cards
    path('parties/host/<int:pk>/', views.HostView.as_view()),  # GET & POST
    path('parties/party/<int:pk>/', views.PartyView.as_view()),  # GET & POST

    path('parties/confirmed', views.PartiesConfirmedList.as_view()),  # GET & POST
    path('invite/<int:pk>/', views.CreateInvite.as_view())
]
