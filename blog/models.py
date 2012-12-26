from django.db import models
from taggit.managers import TaggableManager
from django.contrib.localflavor.us.models import USStateField

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    create_at = models.DateField(auto_now_add=True)
    tags = TaggableManager()
#    state = USStateField()

    def __unicode__(self):
        return self.title
