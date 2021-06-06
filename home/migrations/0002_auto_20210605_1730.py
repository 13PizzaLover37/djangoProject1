# Generated by Django 3.2.4 on 2021-06-05 15:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='photos/', verbose_name='Photo'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gender',
            name='gender',
            field=models.CharField(max_length=20, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='languages',
            name='language',
            field=models.CharField(max_length=25, verbose_name='Language'),
        ),
    ]
