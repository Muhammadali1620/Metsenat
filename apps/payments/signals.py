from django.dispatch import receiver
from django.db.models.signals import post_save

from apps.payments.models import SponsorStudent


@receiver(post_save, sender=SponsorStudent)
def post_save_sponsor_student(instance, created, *args, **kwargs):
    if not created:
        return instance
    sponsor = instance.sponsor
    student = instance.student
    amount = instance.amount

    student.sponsored_amount += amount
    student.save()
    
    sponsor.used_amount += amount
    sponsor.save()

    return instance