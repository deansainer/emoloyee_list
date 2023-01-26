from django.db import models


class Position(models.Model):
    position_name = models.CharField(max_length=55)

    def __str__(self):
        return self.position_name


class Location(models.Model):
    location_name = models.CharField(max_length=55)

    def __str__(self):
        return self.location_name


class Employee(models.Model):
    name = models.CharField(max_length=55)
    surname = models.CharField(max_length=85)
    position_name = models.ForeignKey(Position, on_delete=models.CASCADE)
    email = models.EmailField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    photo = models.ImageField(blank=True)
    birthday = models.DateField()
    phone = models.CharField(max_length=12)

    def __str__(self):
        return ''.join(f'{self.name} {self.surname}')
