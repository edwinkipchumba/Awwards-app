from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from cloudinary.models import CloudinaryField
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating
from django.dispatch import receiver

# Create your models here.

class Rating(models.Model):
    source = models.CharField(max_length=50)
    rating = models.CharField(max_length=10)

    def __str__(self):
        return self.source


class Projects(models.Model):
    image = CloudinaryField('image')
    title = models.CharField(max_length=120)
    description = models.TextField() 
    link = models.CharField(max_length=500)
    ratings = GenericRelation(Rating, related_query_name='projects')
    date_posted = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.title
    
    # delete project option
    # def delete(self):
    #     self.delete()

    class Meta:
        ordering = ['-date_posted']




class ProjectsApi(models.Model):
    title = models.CharField(max_length=40)
    description = models.TextField()


RATE_CHOICES = [
	(1, '1 - Trash'),
	(2, '2 - Horrible'),
	(3, '3 - Terrible'),
	(4, '4 - Bad'),
	(5, '5 - OK'),
	(6, '6 - Nice'),
	(7, '7 - Good'),
	(8, '8 - Very Good'),
	(9, '9 - Perfect'),
	(10,'10 - Excellent'), 
]

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete = models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)