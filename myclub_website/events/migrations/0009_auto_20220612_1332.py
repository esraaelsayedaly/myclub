# Generated by Django 3.1.5 on 2022-06-12 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_myclubuser_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='myclubuser',
            name='driving',
            field=models.BooleanField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10, verbose_name='You Have Driving Licence'),
        ),
        migrations.AlterField(
            model_name='myclubuser',
            name='financial_help',
            field=models.BooleanField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10, verbose_name='You Need Financial Help'),
        ),
        migrations.AlterField(
            model_name='myclubuser',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='myclubuser',
            name='know_job',
            field=models.BooleanField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10, verbose_name='You Know a Job Vacancy'),
        ),
        migrations.AlterField(
            model_name='myclubuser',
            name='medical',
            field=models.BooleanField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10, verbose_name='You Need Medical Insurance'),
        ),
        migrations.AlterField(
            model_name='myclubuser',
            name='need_job',
            field=models.BooleanField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10, verbose_name='You Need Job'),
        ),
        migrations.AlterField(
            model_name='myclubuser',
            name='need_training',
            field=models.BooleanField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10, verbose_name='You Need Training'),
        ),
        migrations.AlterField(
            model_name='myclubuser',
            name='single',
            field=models.BooleanField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10, verbose_name='You are Single'),
        ),
        migrations.AlterField(
            model_name='myclubuser',
            name='volunteer',
            field=models.BooleanField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=10, verbose_name='You Can be Volunteer'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
