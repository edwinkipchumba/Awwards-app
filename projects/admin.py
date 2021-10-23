from django.contrib import admin
from .models import Projects,ProjectsApi,Review

# Register your models here.
admin.site.register(Projects)
admin.site.register(ProjectsApi)
admin.site.register(Review)