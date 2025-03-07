# Generated by Django 5.1.1 on 2024-09-25 16:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_shop', '0002_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('body', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='online_shop.product')),
            ],
        ),
    ]
