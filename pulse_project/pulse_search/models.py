from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Search(models.Model):
    term = models.CharField(max_length = 100)
    date_searched = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.term
