from django.db import models
from django.core.exceptions import ValidationError

from apps.users.validators import phone_validate


class University(models.Model):
    name = models.CharField(max_length=150)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Student(models.Model):
    class Level(models.IntegerChoices):
        BAKALAVR = 1, 'BAKALAVR'
        MAGISTER = 2, 'MAGISTER'

    full_name = models.CharField(max_length=150)
    university = models.ForeignKey(University, models.CASCADE, related_name='students')
    level = models.PositiveSmallIntegerField(choices=Level.choices)
    contract = models.DecimalField(max_digits=10, decimal_places=2, )
    sponsored_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    phone_number = models.CharField(max_length=13, validators=[phone_validate], unique=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        if self.sponsored_amount < 0 or self.contract <= 0:
            raise ValidationError('Sponsored or Contract amount cannot be negative')

    def __str__(self):
        return self.full_name