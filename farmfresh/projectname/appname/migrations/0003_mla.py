# Generated by Django 4.1.6 on 2023-02-16 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appname', '0002_okk'),
    ]

    operations = [
        migrations.CreateModel(
            name='mla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='img')),
                ('name', models.CharField(max_length=150)),
                ('date', models.DateField()),
            ],
        ),
    ]
