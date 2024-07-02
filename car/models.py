from django.db import models

# Create your models here.
class Car(models.Model):
    car_id = models.CharField(primary_key=True, unique=True, null=False, max_length=10)
    class Category(models.TextChoices):
        mini = 'Mini'
        suv = 'SUV'
        luxe = 'Luxe'
    category = models.CharField(choices=Category.choices, default=Category.mini, max_length=5)
    model = models.CharField(max_length=20)
    number_plate = models.CharField(max_length=15, unique=True, null=False)
    current_city = models.CharField(max_length=20)
    rent_per_hr = models.IntegerField(default=100)
    user = models.ForeignKey('user.User', on_delete=models.CASCADE)
    is_available = models.BooleanField(default=True)
    
class History(models.Model):
    car_id = models.ForeignKey(Car, related_name='rent_history', on_delete=models.CASCADE)
    origin = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    amount = models.IntegerField()
    hours_requirement = models.IntegerField()
    
    
    
         
    