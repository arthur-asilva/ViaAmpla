from django.urls import path
from . import views

urlpatterns = [
    path('add_proposal', views.ClientAddProposal, name='add_proposal')
]