# Generated by Django 3.2.13 on 2022-08-29 20:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='driving',
        ),
        migrations.RemoveField(
            model_name='register',
            name='financial_help',
        ),
        migrations.RemoveField(
            model_name='register',
            name='know_job',
        ),
        migrations.RemoveField(
            model_name='register',
            name='medical',
        ),
        migrations.RemoveField(
            model_name='register',
            name='need_job',
        ),
        migrations.RemoveField(
            model_name='register',
            name='need_training',
        ),
        migrations.RemoveField(
            model_name='register',
            name='single',
        ),
        migrations.RemoveField(
            model_name='register',
            name='volunteer',
        ),
        migrations.AddField(
            model_name='register',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='register',
            name='address',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(max_length=60),
        ),
        migrations.AlterField(
            model_name='register',
            name='phone',
            field=models.CharField(max_length=30),
        ),
    ]
