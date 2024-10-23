from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator 

class Country(models.Model):
    id = models.AutoField(primary_key=True)
    sortname = models.CharField(max_length=2, unique=True)
    name = models.TextField(max_length=50, unique=True)
    phonecode = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(999)]) 
    
    class Meta:
        db_table = 'countries'
        indexes = [models.Index(fields=['name'])]
        verbose_name_plural = 'Countries'
        
    
    def __str__(self):
        return self.name


class State(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='states')
    
    class Meta:
        db_table = 'states'
        indexes = [models.Index(fields=['name'])]
        verbose_name_plural = 'States'
        
    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=50)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='cities')
    
    class Meta:
        db_table = 'cities'
        indexes = [models.Index(fields=['name'])]
        verbose_name_plural = 'Cities'
        
    def __str__(self):
        return self.name
    

# Create your models here.
