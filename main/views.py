from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from accounts.models import CustomProfile
# Create your views here.
from django.contrib.auth.models import User, auth
from .forms import ProfileCreationForm
from django.contrib.auth import get_user_model
User = get_user_model()


@login_required
def home(request):
    context={}
    accounts=User.objects.get(email=request.user.email)
    context['accounts']=accounts
    try:
      Data = CustomProfile.objects.get(user=request.user)
      context['profile']=Data
      return render(request,'home.html',context)
    except CustomProfile.DoesNotExist:
      form=ProfileCreationForm()
      if request.method == 'POST' :
        print(request.POST)
        
        form=ProfileCreationForm(request.POST, request.FILES)
        if form.is_valid():
            proc= form.save(commit=False)
            proc.user=request.user
            proc.save()
            return redirect('home')

      context={'form':form}
      return render(request,'home.html',context)
    

    

