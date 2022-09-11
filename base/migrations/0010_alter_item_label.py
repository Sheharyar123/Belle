# Generated by Django 4.1.1 on 2022-09-10 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_item_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='label',
            field=models.CharField(choices=[('primary', 'new'), ('warning', 'hot'), ('danger', 'sale')], max_length=20),
        ),
    ]