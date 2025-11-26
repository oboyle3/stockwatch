from django.db import models

# Create your models here.
class Stock(models.Model):
    name  = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10,unique=True)

    def __str__(self):
        return f"{self.name} ({self.symbol})"
    
class MLB(models.Model):
    test = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.state})"
# class Stockprice(models.Model):
#     stock = models.ForeignKey(Stock, on_delete=models.CASCADE)
#     date = models.DateField()
#     price = models.FloatField()

#     class Meta:
#         unique_together = ('stock', 'data')

#     def __str__(self):
#         return f"{self.stock.symbol} - {self}"
class Member(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.firstname} ({self.lastname})"