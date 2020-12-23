from django.db import models
from django.contrib.auth.models import AbstractUser


class ticket(models.Model):
    objects = None
    title = models.CharField('Name', max_length=50)
    ticket = models.TextField('Description')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=50, blank=False)
    #age = models.PositiveIntegerField(null=True, blank=True)