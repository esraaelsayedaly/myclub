# Generated by Django 3.2.13 on 2022-06-03 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_event_manager'),
    ]

    operations = [
        migrations.AddField(
            model_name='myclubuser',
            name='phone',
            field=models.CharField(default='SOME STRING', max_length=100, verbose_name='Your phone'),
        ),
        migrations.AlterField(
            model_name='myclubuser',
            name='email',
            field=models.EmailField(max_length=100, verbose_name='User Email'),
        ),
    ]
