from django.shortcuts import render,redirect,get_object_or_404
from django.http  import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import *
from rest_framework import status
from .permissions import IsAdminOrReadOnly

# Create your views here.
def home(request):
    projects = Project.get_projects()
    reviews = Reviews.get_reviews()
    profile = Profile.get_profile()

    current_user = request.user
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            content = form.cleaned_data['content']
            review = form.save(commit=False)
            review.project = project
            review.juror = current_user
            review.design = design
            review.usability = usability
            review.content = content
            review.save()
        return redirect('home')

    else:
        form = ReviewForm()

    return render(request,"home.html",{"projects":projects, "reviews":reviews,"form": form,"profile":profile})

# login to update profile
@login_required(login_url='/accounts/login/')
def profile(request,profile_id):

    profile = Profile.objects.get(pk = profile_id)
    projects = Project.objects.filter(profile_id=profile).all()

    return render(request,"profile.html",{"profile":profile,"projects":projects})

# to add profile
@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('home')

    else:
        form = NewProfileForm()
    return render(request, 'new_profile.html', {"form": form})
