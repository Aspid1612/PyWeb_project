# Generated by Django 4.1.5 on 2023-02-24 20:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cart_shop', '0002_wishlistuser'),
    ]

    operations = [
        migrations.DeleteModel(
            name='WishlistUser',
        ),
    ]
