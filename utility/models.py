from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Table(models.Model):
    server = models.ForeignKey('auth.User')

class Order(models.Model):
    paid = models.BooleanField(default=False)
    table = models.ForeignKey(Table)
    notes = models.CharField(max_length=255, null=True, blank=True)
    server = models.ForeignKey('auth.User')

    @property
    def contents(self):
        return [food_obj.food for food_obj in self.food_set.all()]
    

class Food(models.Model):
    food = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.FloatField()
    owner = models.ForeignKey('auth.User')
    order = models.ForeignKey(Order)


STATUS = [
    ('o', 'Owner'),
    ('c', 'Cook'),
    ('s', 'Server')
]

class Profile(models.Model):
    user = models.OneToOneField('auth.User')
    status = models.CharField(max_length=1, choices=STATUS)

@receiver(post_save, sender=User)
def create(**kwargs):
    created = kwargs['created']
    instance = kwargs['instance']
    if created:
        Profile.objects.create(user=instance)
