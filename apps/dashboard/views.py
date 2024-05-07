from django.shortcuts import render

def Dashboard(request):
    return render(request, 'dashboard/dashboard.html', {'data': range(0, 20)})