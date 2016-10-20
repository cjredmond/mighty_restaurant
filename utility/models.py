from django.db import models

class Table(models.Model):
    server = models.ForeignKey('auth.User')

class Order(models.Model):
    paid = models.BooleanField(default=False)
    table = models.ForeignKey(Table)
    notes = models.CharField(max_length=255, null=True, blank=True)
    server = models.ForeignKey('auth.User')

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
