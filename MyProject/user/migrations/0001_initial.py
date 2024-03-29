# Generated by Django 3.2.4 on 2022-09-02 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=40)),
                ('Mobile', models.CharField(max_length=30)),
                ('Message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='igallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gname', models.CharField(max_length=400)),
                ('gpic', models.ImageField(default='', upload_to='static/gallery/')),
            ],
        ),
        migrations.CreateModel(
            name='slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shead', models.CharField(max_length=300)),
                ('ssubject', models.CharField(max_length=500)),
                ('sdes', models.TextField()),
                ('spic', models.ImageField(default='', upload_to='static/slider/')),
            ],
        ),
    ]
