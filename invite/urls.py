from django.urls import path

from . import views

urlpatterns = [
    path('parties/', views.PartiesList.as_view()),  # GET & POST 
]
