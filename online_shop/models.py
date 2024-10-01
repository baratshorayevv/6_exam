from django.db import models

class Product(models.Model):
    class RatingChoices(models.IntegerChoices):
        zero = 0
        one = 1
        two = 2
        three = 3
        four = 4
        five = 5

    name = models.CharField(max_length=100, blank=True, default='')
    description = models.TextField(blank=True, default='')
    image = models.ImageField(upload_to='products', blank=True, null=True)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    new_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00, blank=True, null=True)
    rating = models.PositiveSmallIntegerField(choices=RatingChoices.choices, default=RatingChoices.zero.value, blank=True, null=True)
    discount = models.PositiveSmallIntegerField(default=0, blank=True, null=True)
    quantity = models.IntegerField(default=0)
    def __str__(self):
        return self.name
    

class Coments(models.Model):
    full_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='comments', null=True)

    def str(self):
        return f"{self.name} - {self.created_at}"