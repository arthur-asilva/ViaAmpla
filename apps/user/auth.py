from django.conf import settings
from django.shortcuts import redirect

def LoginRequired(func):

    def wrapper(*args, **kwargs):
        user = args[0].session.get('app_auth', None)
        if user == None:
            return redirect(settings.HOST)
        
        return func(*args, **kwargs)
    
    return wrapper