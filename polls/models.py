import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
class Day(models.Model):
    date = models.DateField()

    def __str__(self):
        return f'{self.date}'

class Option(models.Model):
    name = models.CharField(max_length=200, unique=True)
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    LETTER_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
    ]
    letter = models.CharField(
        max_length=1,
        choices=LETTER_CHOICES,
        default='A',
    )

    def __str__(self):
        return f'{self.name} ({self.day})'

    def avg_ratings(self):
        return self.rating_set.aggregate(
            models.Avg('rating'),
        )

class Rating(models.Model):
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    RATING_CHOICES = [
        (1, '⭐️'),
        (2, '⭐️⭐️'),
        (3, '⭐️⭐️⭐️'),
        (4, '⭐️⭐️⭐️⭐️'),
        (5, '⭐️⭐️⭐️⭐️⭐️'),
    ]
    rating = models.PositiveSmallIntegerField(
        choices=RATING_CHOICES,
        default=3,
    )
    
    def __str__(self):
        return f'{self.option} ({self.timestamp})'

