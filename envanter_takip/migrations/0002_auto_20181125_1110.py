# Generated by Django 2.1.3 on 2018-11-25 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('envanter_takip', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urun',
            name='adet',
        ),
        migrations.AddField(
            model_name='urun',
            name='urun_kod',
            field=models.CharField(default='URN', max_length=5),
        ),
        migrations.AddField(
            model_name='urun',
            name='urun_no',
            field=models.PositiveIntegerField(default='1'),
        ),
    ]