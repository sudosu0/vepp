# Generated by Django 2.0.4 on 2018-05-01 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crmapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partner',
            name='zipcode',
            field=models.PositiveIntegerField(default=0, verbose_name='поштовий індекс'),
        ),
    ]