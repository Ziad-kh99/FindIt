# Generated by Django 5.1.7 on 2025-03-30 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0002_rename_user_id_item_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_type',
            field=models.CharField(choices=[('lost', 'Lost'), ('found', 'Found')], max_length=100),
        ),
    ]
