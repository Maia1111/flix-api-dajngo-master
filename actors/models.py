from django.db import models

class Actor(models.Model):
    NATIONALITY_CHOICES = (
        ('USA', 'Estados Unidos'),
        ('BR', 'Brasil'),
    )
    name = models.CharField(max_length=200)
    birthday = models.DateField(null=True, blank=True)
    nationality = models.CharField(
        max_length=100,
        choices=NATIONALITY_CHOICES,
        blank=True,
        null=True
    )
    
    def __str__(self):
        return self.name
