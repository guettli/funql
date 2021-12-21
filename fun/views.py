from django.shortcuts import render

def accounts_profile(request):
    return render(request, 'fun/accounts_profile.html')

def start(request):
    return render(request, 'fun/start.html')
