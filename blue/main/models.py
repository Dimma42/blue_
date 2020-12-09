from django.db import models


class ticket(models.Model):
    title = models.CharField('Name', max_length=50)
    ticket = models.TextField('Description')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'task'
        verbose_name_plural = 'tasks'