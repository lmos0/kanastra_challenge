from django.db import models
from django.core.validators import EmailValidator

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=255)
    governmentId = models.CharField(max_length=20)
    email = models.EmailField(validators=[EmailValidator])
    debtAmount= models.DecimalField(max_digits=10, decimal_places=2)
    debtDueDate= models.DateField()

    class Meta:
        db_table = 'person'

