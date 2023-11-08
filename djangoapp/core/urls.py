from django.urls import path
from .views import *

urlpatterns = [
    path('pills/', PillsView, name='pills'),
    path('pills/<int:pk>', PillView),
    path('contacts/', ContactsView, name='contacts'),
    path('informations/', InformationsView, name='informations'),
]
