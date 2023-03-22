from django.db import models


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Review(models.Model):
    CHOICES = ((i, '* ' * i) for i in range(1, 6))
    movie = models.ForeignKey(Product, on_delete=models.CASCADE,
                              related_name='reviews')
    stars = models.IntegerField(choices=CHOICES)
    text = models.TextField()

    def __str__(self):
        return self.text
