import json
from django.shortcuts import render, redirect
from .auth import LoginRequired
from apps.utils.views import DataModel
from .models import User
from django.conf import settings



def UserLogin(request):
    data = DataModel(message_text='Usuário não encontrado', message_title='Verifique seus dados e tente novamente')

    if request.session.get('app_auth', None) != None:
        return redirect(f"{settings.HOST}/dashboard")

    if request.method == 'POST':
        user = User.objects.filter(email=request.POST['email'], password=request.POST['password'])
        data.SetItem('has_message', True)

        if user.exists():
            data.SetItem('has_message', False)
            request.session['app_auth'] = json.dumps({'id': user.first().id, 'name': user.first().name, 'email': user.first().email})
            return redirect(f"{settings.HOST}/dashboard")

    return render(request, 'user/login.html', data.GetData())



@LoginRequired
def UserLogout(request):
    session = request.session.get('app_auth', None)
    
    if session != None:
        del request.session['app_auth']

    return redirect(f"{settings.HOST}")
