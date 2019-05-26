from django.db import models

# Create your models here.
class Users(models.Model):
    id = models.IntegerField(primary_key=True)
    company_id = models.OneToOneField(Companies, on_delete='CASCADE')
    created_at = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    name = models.CharField(max_length=1000)


class Companies(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(blank=True, default='')
