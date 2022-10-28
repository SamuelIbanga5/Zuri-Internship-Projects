from django.db import models

class Data(models.Model):
    slackUsername = models.CharField(max_length=255)
    backend = models.BooleanField(default=False)
    age = models.PositiveSmallIntegerField()
    bio = models.TextField(max_length=500)
    
    def __str__(self):
        return self.slackUsername
