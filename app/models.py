from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.
class BlogPost(models.Model):
    post_title = models.CharField(max_length=150)
    post_desc = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("app:detail", kwargs={'pk':self.pk})

    class Meta:
        ordering = ['-date_posted']

    def __str__(self):
        return self.post_title + '     '+ str(self.posted_by)
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pictures', blank=True, default='profile_piictures/default.jpg')

    def __str__(self):
        return self.user.username

