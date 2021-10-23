from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import RegisterUserForm
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Your account has been created successfully')
            return redirect('login')


    else:
        form = RegisterUserForm()
        
    context = {
        'form':form
    }
    return render(request,'users/register.html',context)

@login_required
def profile_view(request):
    profile=Profile.objects.get(user=request.user.id)
    return render(request,'users/profile.html')