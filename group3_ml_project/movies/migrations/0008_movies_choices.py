# Generated by Django 3.0.6 on 2020-05-06 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_auto_20200506_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='movies_choices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_1', models.CharField(max_length=528)),
                ('movie_2', models.CharField(max_length=528)),
                ('movie_3', models.CharField(max_length=528)),
            ],
        ),
    ]
