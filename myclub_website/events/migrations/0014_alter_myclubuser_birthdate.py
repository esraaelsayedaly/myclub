# Generated by Django 4.1.7 on 2023-03-01 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_alter_myclubuser_birthdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myclubuser',
            name='birthdate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Birth date'),
        ),
    ]
