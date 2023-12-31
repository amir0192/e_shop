from django.db import models

# Create your models here.

# создаем категорию
class Category(models.Model):
    objects = models.Model
    name = models.CharField(max_length=60)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

# характеристика продукта
class Product(models.Model):
    objects = models.Model
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=150)
    product_amount = models.IntegerField()
    product_price = models.FloatField()
    reviews = models.FloatField()
    category_name = models.ForeignKey(Category, on_delete=models.CASCADE)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# создаем корзину для сайта
class UserCart(models.Model):
    objects = models.Model
    user_id = models.IntegerField()
    user_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user_product_quantity = models.IntegerField()
    added_date = models.DateTimeField(auto_now_add=True)






