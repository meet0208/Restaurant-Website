# Generated by Django 3.1.6 on 2021-04-17 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0007_reservation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish', models.CharField(max_length=50)),
                ('ingredients', models.TextField()),
                ('img5', models.ImageField(upload_to='menu')),
                ('price1', models.IntegerField()),
                ('Type', models.CharField(max_length=50)),
            ],
        ),
    ]
