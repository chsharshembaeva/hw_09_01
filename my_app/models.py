from django.db import models


class Position(models.Model):
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    def __str__(self):
        return self.position


class Employee(models.Model):
    name = models.CharField(max_length=100)
    date_birth = models.DateTimeField()
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    salary = models.IntegerField()

    def __str__(self):
        return self.name


