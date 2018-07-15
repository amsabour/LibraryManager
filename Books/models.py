from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    image_url = models.CharField(max_length=500, default='')
    is_taken = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('Books:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title + ' - ' + self.author
