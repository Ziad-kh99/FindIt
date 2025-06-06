# Generated by Django 5.1.7 on 2025-03-30 14:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('items', '0002_rename_user_id_item_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('rejected', 'Rejected')], default='pending', max_length=100)),
                ('found_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='found_matches', to='items.item')),
                ('lost_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lost_matches', to='items.item')),
            ],
        ),
    ]
