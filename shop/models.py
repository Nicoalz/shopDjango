from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(
        max_length=2083, default='https://img.rawpixel.com/s3fs-private/rawpixel_images/website_content/rm436-033_2.jpg?w=800&dpr=1&fit=default&crop=default&q=65&vib=3&con=3&usm=15&bg=F4F4F3&ixlib=js-2.2.1&s=5932e6cd1597b7adcb7b249efb41215f')

    def __str__(self):
        return self.name
