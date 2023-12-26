# Generated by Django 4.2.8 on 2023-12-26 18:21

import app.product.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_remove_product_img_product_img1_product_img2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img1',
            field=models.ImageField(blank=True, null=True, upload_to=app.product.models.product_image_path, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img2',
            field=models.ImageField(blank=True, null=True, upload_to=app.product.models.product_image_path, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img3',
            field=models.ImageField(blank=True, null=True, upload_to=app.product.models.product_image_path, verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img4',
            field=models.ImageField(blank=True, null=True, upload_to=app.product.models.product_image_path, verbose_name='Изображение'),
        ),
    ]
