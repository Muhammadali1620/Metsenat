import django_filters
from .models import Sponsor, SponsorStudent


class SponsorFilter(django_filters.FilterSet):
    class Meta:
        model = Sponsor
        fields = ['person', 'status', 'payment_type']
