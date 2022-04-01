from unittest.mock import create_autospec
from django.db import models

# Create your models here.

class Memo(models.Model):
    create_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    content = models.TextField(blank=True)
