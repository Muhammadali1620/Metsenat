from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save

from apps.payments.models import SponsorStudent, Sponsor


@receiver(post_save, sender=SponsorStudent)
def post_save_sponsor_student(instance, created, *args, **kwargs):
    sponsor = instance.sponsor
    student = instance.student
    amount = instance.amount
    if not created:
        return instance

    student.sponsored_amount += amount
    student.save()
    
    sponsor.used_amount += amount
    sponsor.save()

    return instance


@receiver(pre_save, sender=Sponsor)
def pre_save_sponsor(instance, *args, **kwargs):
    old_sponsor = Sponsor.objects.filter(pk=instance.pk).first()
    if not old_sponsor or old_sponsor.status != Sponsor.Status.CONFIRMED:
        return instance
    instance.status = Sponsor.Status.CONFIRMED
    instance.amount = old_sponsor.amount
    return instance




@receiver(pre_save, sender=SponsorStudent)
def pre_save_sponsor_student(instance, *args, **kwargs):
    old_obj = SponsorStudent.objects.filter(pk=instance.pk).first()
    if not old_obj:
        return instance
    extra = old_obj.amount - instance.amount

    old_obj.student.sponsored_amount = old_obj.student.sponsored_amount - extra
    old_obj.student.save()

    old_obj.sponsor.used_amount = old_obj.sponsor.used_amount - extra
    old_obj.sponsor.save()
    return instance