# Generated by Django 4.1.1 on 2022-09-10 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_item_gender_alter_item_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='sold',
            field=models.IntegerField(default=0),
        ),
    ]
