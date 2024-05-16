from django.shortcuts import render
from .models import Client
from apps.utils.views import DataModel
from apps.user.auth import LoginRequired


@LoginRequired
def ClientAddProposal(request):

    data = DataModel()

    if request.method == 'POST':
        Client.create(request)

    return render(request, 'client/add_proposal.html', data.data)



def ClientSelfAddProposal(request):

    data = DataModel()

    if request.method == 'POST':
        Client.create(request)

    return render(request, 'client/client_add_proposal.html', data.data)
