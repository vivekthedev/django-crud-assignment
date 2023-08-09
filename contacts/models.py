from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    number = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)