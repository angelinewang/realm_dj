from django.urls import path

from django.views.decorators.csrf import csrf_exempt
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # USE WITH CAUTION To fully clean out 'user' table
    path('delete/all', views.DeleteAll.as_view()),
    path('delete/<int:pk>/', views.DeleteProfile.as_view()),  # POST only
    path('signup/', csrf_exempt(views.RegisterView.as_view())), # POST only
    path('login/', csrf_exempt(views.LoginView.as_view()),), # GET & POST 
    path('profile/<int:pk>/', views.ProfileDetail.as_view()), # GET & POST 
    # GETs the last party associated with user and sends ONLY the first entry as response 
    path('firstentry/<int:pk>/', views.FirstEntryView.as_view()),

    path('updatephoto/<int:pk>/', views.UpdatePhoto.as_view()),

    path('changerole/<int:pk>/', views.RoleChangeView.as_view()),
    
    path('guests/browse/<int:pk>/guestmode/', csrf_exempt(views.GuestsBrowseGuestMode.as_view())),  # GET only, when user state is guest
    # GET only, when user state is guest

    path('guests/browse/<int:party>/existinginvites/',
         views.ExistingInvitesView.as_view()),
    
    path('guests/browse/<int:pk>/hostmode/', views.GuestsBrowseHostMode.as_view()),
    # 00. Get the User Role 0. Get the party 1. Get the Existing Invites 2. Then gets the Users not part of the existing invites 

    # First param is the User ID, Second param is the Party ID
    # ON FRONT END: 1. Get User Role 2. Decide if user is host or guest 3. If Guest, pass User ID to guestmode URL : 3. If Host, Get User Party 4. Pass User ID and User Party ID to the hostmode URL 


    # User state is evaluated in the backend, if user is guest, get all users not himself, if user is host, get all users not himself and not already a guest_id tied to an invite tied to the host's most recent party entry 
#     # GET only, when user state is guest
#     path('guests/browse/<int:pk>/hostmode', views.GuestsBrowseHostMode.as_view()),
] 
# # ]

# if settings.DEBUG: 
#     urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)