from django.db import models


class Acquirer(models.Model):
    name = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.name.upper()


class Connectivity(models.Model):
    type = models.CharField(max_length=31, unique=True)

    def __str__(self):
        return self.type.upper()


class Model(models.Model):
    name = models.CharField(max_length=63)
    connectivity = models.ForeignKey(
        Connectivity, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'{self.name.upper()} {self.connectivity.type.upper()}'


class Location(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name.upper()


class Status(models.Model):
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name.upper()


class Terminal(models.Model):
    serial_number = models.CharField(max_length=255, unique=True)
    part_number = models.CharField(max_length=255)
    acquirer = models.ForeignKey(
        Acquirer, on_delete=models.SET_NULL, null=True)
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey(
        Model, on_delete=models.SET_NULL, null=True)
    # default location id:pk:1 carrasco
    location = models.ForeignKey(
        Location, on_delete=models.PROTECT, default=1)
    notes = models.TextField(blank=True)

    def __str__(self):
        return f'{self.serial_number}, {self.model} de {self.acquirer}'
