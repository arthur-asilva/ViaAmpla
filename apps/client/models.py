from django.db import models
from apps.utils.views import *
from django.utils import timezone

class Client(models.Model):
    client_name = models.CharField(max_length=254)
    client_email = models.EmailField(max_length=254)
    client_born_date = models.DateField()
    client_cpf = models.CharField(max_length=11)
    client_phone_number = models.CharField(max_length=30)
    client_has_license_plate = models.BooleanField()
    client_conductor_relation = models.IntegerField(choices=CLIENT_RELATION)

    conductor_name = models.CharField(max_length=254)
    conductor_cpf = models.CharField(max_length=11)
    conductor_gender = models.IntegerField(choices=GENDERS)
    conductor_born_date = models.DateField()
    conductor_marital_status = models.IntegerField(choices=MARITAL_STATUS)

    conductor_extended_coverage = models.IntegerField(choices=EXTENDED_COVERAGES)

    storage_cep = models.CharField(max_length=20)
    use_type = models.IntegerField(choices=USE_TYPES)

    is_rebranded_chassis = models.BooleanField()
    is_alienado = models.BooleanField()
    is_customized = models.BooleanField()
    is_armored = models.BooleanField()
    have_gas_kit = models.BooleanField()

    live_in = models.IntegerField(choices=LIVE_IN)
    storage_type = models.IntegerField(choices=STORAGE_IN)
    is_to_work = models.IntegerField(choices=IS_TO_WORK)
    is_to_college = models.IntegerField(choices=IS_TO_COLLEGE)

    trust_check = models.BooleanField(blank=True, null=True)
    created_at = models.DateTimeField(null=True, blank=True, default=timezone.now)

    seen = models.BooleanField(default=False, null=True)
    answered = models.BooleanField(default=False, null=True)

    def __str__(self):
        return self.client_name
    
    @classmethod
    def create(cls, request):
        data = request.POST.copy()
        cls.objects.create()




