import json

from django.db import models
from django.contrib.auth import get_user_model

from django.utils import timezone

User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)
    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'
    def __str__(self):
        return self.name
    @property
    def products(self):
        return json.dumps(Product.objects.filter(category=self).values())



class Product(models.Model):
    category = models.ForeignKey(Category,
    related_name='products',
    on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
    def __str__(self):
        return self.name




class Customer(models.Model):

    user = models.OneToOneField(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, verbose_name='Номер телефона', null=True, blank=True)
    address = models.CharField(max_length=255, verbose_name='Адрес', null=True, blank=True)
    orders = models.ManyToManyField('orders.Order', verbose_name='Заказы покупателя', related_name='related_order', blank=True)

    def __str__(self):
        if not (self.user.first_name and self.user.last_name):
            return self.user.username
        return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)


