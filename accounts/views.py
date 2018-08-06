# accounts/view.py
from django.shortcuts import render
from .forms import SignupForm 
from django.conf import settings
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,JsonResponse
#from .models import Profile

def signup(request):
    if request.method =='POST':
         form = SignupForm(request.POST)
         if form.is_valid():
             user = form.save()
             return redirect(settings.LOGIN_URL)
    else:
            form = SignupForm()
    return render(request, "accounts/signup_form.html", {
          'form' : form,
      })

@login_required #로그인시만
def profile(request):
    return render(request, 'accounts/profile.html')
'''
def index_save(request):
    if request.method =='POST':
        pointer = request.POST['pointer']
        profile = Profile(index=pointer)
        profile.save()
   
    return HttpResponse()
    ## views.py 에서는 같은 앱에 있는 모델 밖에 불러오지 못한다.
'''