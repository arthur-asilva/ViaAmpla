from django.shortcuts import render
from apps.utils.views import CLIENT_RELATION

def ClientAddProposal(request):
    data = {
        'client_relation': CLIENT_RELATION
    }
    return render(request, 'client/add_ proposal.html', data)
