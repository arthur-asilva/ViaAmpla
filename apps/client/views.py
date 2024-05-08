from django.shortcuts import render
from apps.utils.views import CLIENT_RELATION, GENDERS, MARITAL_STATUS, EXTENDED_COVERAGES, USE_TYPES, STORAGE_IN, LIVE_IN, IS_TO_WORK, IS_TO_COLLEGE

def ClientAddProposal(request):
    data = {
        'client_relation': CLIENT_RELATION,
        'genders': GENDERS,
        'marital_status': MARITAL_STATUS,
        'extended_coverages': EXTENDED_COVERAGES,
        'use_types': USE_TYPES,
        'storage_in': STORAGE_IN,
        'live_in': LIVE_IN,
        'to_work_options': IS_TO_WORK,
        'to_college_options': IS_TO_COLLEGE,
    }
    return render(request, 'client/add_ proposal.html', data)
