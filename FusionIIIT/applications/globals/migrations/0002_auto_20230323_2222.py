# Generated by Django 3.1.5 on 2023-03-23 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='user_status',
            field=models.CharField(choices=[('PRESENT', 'PRESENT'), ('NEW', 'NEW')], default='PRESENT', max_length=50),
        ),
    ]
