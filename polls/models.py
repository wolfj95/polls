import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Option(models.Model):
    name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class Day(models.Model):
    date = models.DateField()
    options = models.ManyToManyField(Option, through='Serving')

    def __str__(self):
        return f'{self.date}'

class Serving(models.Model):
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE)
    LETTER_CHOICES = [
        ("A", 'Option A'),
        ("B", 'Option B'),
        ("C", 'Option C'),
    ]
    letter = models.CharField(
        max_length=1,
        choices=LETTER_CHOICES,
        default='A',
    )

    def avg_ratings(self):
        return self.rating_set.aggregate(
            models.Avg('rating'),
        )

    def __str__(self):
        return f'{self.option} on {self.day}'

class Rating(models.Model):
    serving = models.ForeignKey(Serving, on_delete=models.CASCADE)
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
        return f'{self.serving}'
