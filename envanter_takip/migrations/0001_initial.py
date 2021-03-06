# Generated by Django 3.0.3 on 2020-02-15 09:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_code', models.CharField(default='URN', max_length=7, verbose_name='Marka Kodu')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_code', models.CharField(default='URN', max_length=7, verbose_name='Kategori Kodu')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Debit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_date', models.DateTimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=16)),
                ('date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(default='URN', max_length=15, verbose_name='Ürün Kodu')),
                ('product_number', models.PositiveIntegerField(default='1', verbose_name='Ürün No')),
                ('feature', models.TextField()),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='envanter_takip.Brand')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='envanter_takip.Category')),
                ('debit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='envanter_takip.Debit')),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='envanter_takip.Invoice')),
            ],
        ),
    ]
