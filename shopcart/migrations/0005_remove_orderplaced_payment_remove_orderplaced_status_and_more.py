# Generated by Django 5.1.4 on 2025-01-18 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopcart', '0004_payment_orderplaced'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderplaced',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='orderplaced',
            name='status',
        ),
        migrations.AddField(
            model_name='orderplaced',
            name='orderId',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
    ]
