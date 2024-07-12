from django.dispatch import receiver
from django.db.models.signals import pre_save

from apps.users.models import Student


@receiver(pre_save, sender=Student)
def pre_save_student(instance, *args, **kwargs):
    old_student = Student.objects.filter(id=instance.id).first()
    if not old_student or old_student.contract <= instance.contract:
        return instance
    
    extra = old_student.contract - instance.contract
    
    sponsor_student = instance.sponsor_student.all().order_by('-created_at').first()
    sponsor = sponsor_student.sponsor
    
    sponsor_student.amount = sponsor_student.amount - extra
    sponsor.used_amount = sponsor.used_amount - extra
    instance.sponsored_amount = instance.sponsored_amount - extra

    sponsor_student.save()
    sponsor.save()

    return instance