from django.db import models

# Create your models here.
class Employee(models.Model):
    Employee_id=models.IntegerField()
    Name=models.CharField(max_length=100)
    Department=models.CharField(max_length=100)
    Salary=models.FloatField()
    Phone=models.CharField(max_length=20)
    Email=models.EmailField()
    Address=models.CharField(max_length=100)
    Joining_date=models.DateField()
    role_choices=(
        ('ACTIVE','active'),
        ('INACTIVE','inactive')
    )
    Status=models.CharField(max_length=10,choices=role_choices,default='ACTIVE')
