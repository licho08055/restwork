from django.db import models
from datetime import timezone

class Mini(models.Model):
    name=models.CharField(max_length=40)
    title=models.CharField(max_length=50)
    date=models.DateField(auto_now=True)
