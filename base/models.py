from django.db import models
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.db.models import Avg
import numpy as np

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    profile_photo = models.ImageField(upload_to='profiles/',null=True)
    bio = models.CharField(max_length=240, null=True)
    phone = models.PositiveIntegerField(default=0)

    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

        post_save.connect(create_user_profile, sender=User)

    def save_profile(self):
        self.save()

    @classmethod
    def get_profile(cls):
        profile = Profile.objects.all()

        return 
    
    
class Project(models.Model):
    posted_by = models.ForeignKey(User, null=True)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True)
    title = models.CharField(max_length=100, null=True)
    project_image = models.ImageField(upload_to='projects/',null=True)
    description = models.TextField(null=True)
    project_link = models.TextField(null=True)

    @classmethod
    def get_projects(cls):
        projects = Project.objects.all()
        return projects

    @classmethod
    def find_project(cls,search_term):
        project = Project.objects.filter(title__icontains=search_term)
        return project

    def design_rating(self):
        all_designs =list( map(lambda x: x.design, self.reviews.all()))
        return np.mean(all_designs)

    def usability_rating(self):
        all_usability =list( map(lambda x: x.usability, self.reviews.all()))
        return np.mean(all_usability)

    def content_rating(self):
        all_content =list( map(lambda x: x.content, self.reviews.all()))
        return np.mean(all_content)
