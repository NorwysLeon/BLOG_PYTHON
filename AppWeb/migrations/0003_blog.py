# Generated by Django 4.1.4 on 2023-01-17 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppWeb', '0002_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=50)),
                ('subtitulo', models.CharField(max_length=50)),
                ('cuerpo', models.CharField(max_length=1000)),
                ('autor', models.CharField(max_length=50)),
                ('fecha', models.DateField()),
                ('imagen', models.ImageField(upload_to='blog')),
            ],
        ),
    ]