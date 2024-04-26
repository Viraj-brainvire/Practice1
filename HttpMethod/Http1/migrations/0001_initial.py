# Generated by Django 4.2.11 on 2024-04-25 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('personid', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=3)),
                ('firstname', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=255)),
            ],
        ),
    ]
