from django.db import models
from django.core.exceptions import ValidationError

from apps.users.validators import phone_validate


class Sponsor(models.Model):
    class Status(models.IntegerChoices):
        NEW = 1, 'New'
        IN_MODERATION = 2, 'In moderation'
        CONFIRMED = 3, 'Confirmed'
        CANCELLED = 4, 'Cancelled'

    class Person(models.IntegerChoices):
        INDIVIDUAL = 1, 'Individual'
        COMPANY = 2, 'Company'

    class Currency(models.IntegerChoices):
        UzCard = 1, 'UzCard'
        HUMO = 2, 'HUMO'
        CLIC = 3, 'CLIC'

    full_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=13, validators=[phone_validate])
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    person = models.PositiveSmallIntegerField(choices=Person.choices)
    company_name = models.CharField(max_length=150, null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=Status.choices, default=Status.NEW)
    payment_type = models.PositiveSmallIntegerField(choices=Currency.choices)
    used_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        if self.amount <= 0:
            return ValidationError('Amount cannot be negative')

        if self.used_amount > self.amount:
            return ValidationError('Used amount cannot be greater than amount')

        if self.person == self.Person.COMPANY and not self.company_name:
            raise ValidationError('Company name is required for Legal Entities.')

        if self.person == self.Person.INDIVIDUAL and self.company_name:
            raise ValidationError('Company name should not be provided for Physical Persons.')


    def __str__(self):
        return self.full_name
    

class SponsorStudent(models.Model):
    sponsor = models.ForeignKey(Sponsor, on_delete=models.SET_NULL, limit_choices_to={'status': Sponsor.Status.CONFIRMED} , null=True, related_name='sponsor_student')
    student = models.ForeignKey('users.Student', on_delete=models.CASCADE, related_name='sponsor_student')
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        sponsor = self.sponsor
        student = self.student

        if sponsor.status != Sponsor.Status.CONFIRMED:
            raise ValidationError('Sponsor is not confirmed')
        
        sponsor_amount = sponsor.amount - sponsor.used_amount
        if sponsor_amount == 0:
            raise ValidationError('Sponsor amount is used up')
        
        student_contract = student.contract - student.sponsored_amount
        if student_contract == 0:
            raise ValidationError('Student contract is full')
        
        if self.amount <= 0:
            raise ValidationError('Amount cannot be negative')
        
        if self.amount > sponsor_amount:
            raise ValidationError('Amount cannot be greater than sponsor amount')

        if self.amount > student_contract:
            raise ValidationError('Amount cannot be greater than student contract')
        
    def __str__(self):
        return f"{self.sponsor}:{self.student}:{self.amount}"