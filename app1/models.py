from django.db import models

# Create your models here.
class employee(models.Model):
    employeeId         = models.IntegerField()
    employeeName       = models.CharField(max_length=50)
    employeeSalary     = models.FloatField()


    def __str__(self):
        return f"{self.employeeId}--{self.employeeName}"
