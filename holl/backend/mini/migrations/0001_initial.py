# Generated by Django 4.0.5 on 2022-06-27 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mini',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('title', models.CharField(max_length=50)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
