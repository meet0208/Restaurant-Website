# Generated by Django 3.1.6 on 2021-04-08 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_party'),
    ]

    operations = [
        migrations.CreateModel(
            name='SpecialItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img4', models.ImageField(upload_to='specialitems')),
                ('dishname', models.CharField(max_length=50)),
                ('name2', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('num', models.IntegerField()),
            ],
        ),
    ]
