from django.db import models
from django.utils.timezone import now


# Create your models here.
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30)
    speed = models.IntegerField()
    description = models.TextField()
    def __str__(self):
        return str(self.name)


class CarModel(models.Model):
    carMake = models.ForeignKey(CarMake, null=False, on_delete=models.CASCADE)
    name = models.CharField(null=False, max_length=30)
    dealerID = models.IntegerField()
    SEDAN = 'sedan'
    SUV = 'suv'
    WAGON = 'wagon'
    TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'SUV'),
        (WAGON, 'Wagon')
    ]
    carType = models.CharField(
        null=False,
        max_length=20,
        choices=TYPE_CHOICES,
        default=SEDAN
    )
    year = models.DateField(null=False)
    def __str__(self):
        return str(self.carMake)


# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
