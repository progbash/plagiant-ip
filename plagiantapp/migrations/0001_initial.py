# Generated by Django 2.2.10 on 2020-03-03 09:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=150)),
                ('logo', models.ImageField(upload_to='static/images/university_logo')),
                ('website', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Universities',
            },
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.TextField(max_length=30)),
                ('last_name', models.TextField(max_length=30)),
                ('email', models.EmailField(max_length=60)),
                ('username', models.TextField(max_length=30)),
                ('password', models.TextField(max_length=60)),
                ('confirm_password', models.TextField(max_length=60)),
                ('isPhysicalAccount', models.BooleanField(default=False)),
                ('university_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='plagiantapp.University')),
            ],
        ),
    ]
