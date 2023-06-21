# Generated by Django 4.1.4 on 2023-06-20 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('birth_date', models.DateField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('publication_date', models.DateField()),
                ('created_date', models.DateField(auto_now_add=True)),
                ('is_availble', models.BooleanField(default=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('description', models.TextField(max_length=200)),
                ('book_code', models.CharField(max_length=20)),
                ('rating', models.DecimalField(decimal_places=2, max_digits=5)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libraryapp.category')),
                ('genre', models.ManyToManyField(to='libraryapp.genre')),
            ],
        ),
    ]
