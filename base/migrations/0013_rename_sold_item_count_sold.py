# Generated by Django 4.1.1 on 2022-09-11 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_item_sold'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='sold',
            new_name='count_sold',
        ),
    ]
