# Generated by Django 3.2.9 on 2021-11-18 15:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0001_initial'),
        ('mainapp', '0002_auto_20211118_1155'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartproduct',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartproduct',
            name='product',
        ),
        migrations.RemoveField(
            model_name='cartproduct',
            name='user',
        ),
        migrations.AlterField(
            model_name='order',
            name='cart',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cart.cart', verbose_name='Корзина'),
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartProduct',
        ),
    ]
