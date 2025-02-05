# Generated by Django 4.2.16 on 2024-12-26 14:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wish', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wish',
            name='color',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='wish',
            name='is_sended',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='wish',
            name='other_option',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='wish',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sender', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='wish',
            name='size',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
