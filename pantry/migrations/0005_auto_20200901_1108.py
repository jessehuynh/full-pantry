# Generated by Django 3.0.1 on 2020-09-01 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pantry', '0004_auto_20200826_1315'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='purchase_date',
            field=models.DateField(),
        ),
    ]