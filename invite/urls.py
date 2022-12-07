from django.urls import path

from . import views

urlpatterns = [
    # User Id passed into API to grab relevant parties
    path('parties/invited/<int:pk>', views.PartiesInvitedList.as_view()),  # GET & POST 

    # These 2 are used for both Invited cards and Confirmed cards
    path('parties/host/<int:pk>/', views.HostView.as_view()),  # GET & POST
    path('parties/party/<int:pk>/', views.PartyView.as_view()),  # GET & POST

    # User Id passed into API to grab relevant parties
    path('parties/confirmed/<int:pk>', views.PartiesConfirmedList.as_view()),  # GET & POST

    path('createinvite/', views.CreateInvite.as_view()),
    # Endpoint accepts 2 fields in POST body: #1 Party Id #2 Guest Id

    # 1. Get the party 2. Get the invites 3. Get the guest profiles
    # Invites according to Party ID

    # #2 Guestlist Invites from Party_id
    path('guestlist/<int:pk>/', views.GuestlistInvites.as_view()),
    
    #  #3 User profile according to guest_id s
    path('guestlist/guest/<int:pk>/', views.GuestlistGuest.as_view()),
]
