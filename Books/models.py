from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    image_url = models.CharField(max_length=500, default='')
    is_taken = models.BooleanField(default=False)

    def __str__(self):
        return self.title + ' - ' + self.author
