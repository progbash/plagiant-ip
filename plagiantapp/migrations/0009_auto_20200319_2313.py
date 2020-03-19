# Generated by Django 2.2.10 on 2020-03-19 23:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('plagiantapp', '0008_originaldocument_checked_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='originaldocument',
            name='checked_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]