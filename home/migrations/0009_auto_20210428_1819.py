# Generated by Django 3.1.7 on 2021-04-28 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20210428_1818'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='gender',
            field=models.IntegerField(choices=[(1, 'Male'), (0, 'Female')], default=1),
        ),
    ]
