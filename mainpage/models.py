from django.db import models

class Apply(models.Model):
    name = models.TextField()
    phonenumber = models.TextField()
    koreandance = models.TextField(null=True)
    PIagree= models.TextField(null=True)
    # select = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

