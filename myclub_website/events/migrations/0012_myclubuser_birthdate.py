# Generated by Django 4.1.7 on 2023-03-01 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0011_myclubuser_gender_alter_myclubuser_driving_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='myclubuser',
            name='birthdate',
            field=models.DateField(default='', verbose_name='Birthdate'),
        ),
    ]