# Generated by Django 3.2.4 on 2022-09-05 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20220905_1240'),
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mstate', models.CharField(max_length=40)),
                ('mdate', models.DateField()),
            ],
        ),
    ]
