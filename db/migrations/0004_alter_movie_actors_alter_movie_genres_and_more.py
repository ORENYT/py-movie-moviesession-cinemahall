# Generated by Django 4.0.2 on 2023-09-14 17:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_alter_movie_actors_alter_movie_genres'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='actors',
            field=models.ManyToManyField(related_name='movies', to='db.Actor'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='genres',
            field=models.ManyToManyField(related_name='movies', to='db.Genre'),
        ),
        migrations.AlterField(
            model_name='moviesession',
            name='cinema_hall',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movie_sessions', to='db.cinemahall'),
        ),
        migrations.AlterField(
            model_name='moviesession',
            name='movie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movie_sessions', to='db.movie'),
        ),
    ]
