# Generated by Django 3.2.4 on 2022-09-05 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_rename_ammountvalue_donatenow_amountvalue'),
    ]

    operations = [
        migrations.CreateModel(
            name='city',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ncity', models.CharField(max_length=30)),
                ('cdate', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='nlogin',
            name='Email',
            field=models.EmailField(max_length=30),
        ),
    ]
