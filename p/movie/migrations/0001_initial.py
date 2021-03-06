# Generated by Django 3.0.4 on 2020-05-16 11:23

import datetime
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='ismi')),
                ('age', models.PositiveSmallIntegerField(default=0, verbose_name='Yoshi')),
                ('description', models.TextField(verbose_name='opisaniyasi')),
                ('image', models.ImageField(upload_to='actors/')),
            ],
            options={
                'verbose_name': 'Akter va Rejisor',
                'verbose_name_plural': 'Akterlar va Rejisorlar',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Katigoriyasi')),
                ('description', models.TextField(verbose_name='opisaniyasi')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Katigoriya',
                'verbose_name_plural': 'Katigoriyalar',
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nomi')),
                ('description', models.TextField(verbose_name='opisaniyasi')),
                ('url', models.SlugField(max_length=160, unique=True)),
            ],
            options={
                'verbose_name': 'Janr',
                'verbose_name_plural': 'Janrlar',
            },
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Nomi')),
                ('tagline', models.CharField(default='', max_length=100, verbose_name='Slogan')),
                ('description', models.TextField(verbose_name='Opisaniyasi')),
                ('poster', models.ImageField(upload_to='movies/', verbose_name='Poster')),
                ('years', models.PositiveSmallIntegerField(default=2020, verbose_name='Chiqgan sanasi')),
                ('country', models.CharField(max_length=50, verbose_name='Mamlakat')),
                ('world_premiere', models.DateField(default=datetime.date.today, verbose_name='Dunyo premyerasi')),
                ('budget', models.PositiveIntegerField(default=0, help_text='narxini dollarda korsating', verbose_name='Byujet')),
                ('fees_in_usa', models.PositiveIntegerField(default=0, help_text='narxini dollarda korsating', verbose_name='AQSHda yigilgan puli')),
                ('fees_in_world', models.PositiveIntegerField(default=0, help_text='narxini dollarda korsating', verbose_name='Dunyoda yigilgan puli')),
                ('url', models.SlugField(max_length=130, unique=True)),
                ('draft', models.BooleanField(default=False, verbose_name='Chernovik')),
                ('actors', models.ManyToManyField(related_name='film_actor', to='movie.Actor', verbose_name='Akter')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.Category', verbose_name='Kategoriya')),
                ('directors', models.ManyToManyField(related_name='film_director', to='movie.Actor', verbose_name='rejisor')),
                ('genres', models.ManyToManyField(to='movie.Genre', verbose_name='janr')),
            ],
            options={
                'verbose_name': 'Film',
                'verbose_name_plural': 'Filmlar',
            },
        ),
        migrations.CreateModel(
            name='RatingStar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.SmallIntegerField(default=0, verbose_name='Manosi')),
            ],
            options={
                'verbose_name': 'Yulduz reytingi',
                'verbose_name_plural': 'Yulduzlar reytingi',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Emaili')),
                ('name', models.CharField(max_length=100, verbose_name='Nomi')),
                ('text', models.TextField(max_length=5000, verbose_name='Xabar')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movie', verbose_name='Film')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='movie.Reviews', verbose_name='Ota-ona')),
            ],
            options={
                'verbose_name': 'Sharh',
                'verbose_name_plural': 'Sharhlar',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=15, verbose_name='Ip adress')),
                ('movie', models.ForeignKey(on_delete=django.db.models.fields.CharField, to='movie.Movie', verbose_name='Film')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.RatingStar', verbose_name='yulduz')),
            ],
            options={
                'verbose_name': 'Reyting',
                'verbose_name_plural': 'Reytinglar',
            },
        ),
        migrations.CreateModel(
            name='MovieShots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Sarlavha')),
                ('description', models.TextField(verbose_name='Qisqacha malumot')),
                ('image', models.ImageField(upload_to='movie_shots/')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.Movie')),
            ],
            options={
                'verbose_name': 'Filmdan kadr',
                'verbose_name_plural': 'Filmdan kadrlar',
            },
        ),
    ]
