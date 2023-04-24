# Generated by Django 4.2 on 2023-04-24 05:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomebrewBatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='brew_images')),
                ('start_date', models.DateField()),
                ('rack_date', models.DateField()),
                ('bottle_date', models.DateField()),
                ('original_gravity', models.FloatField()),
                ('final_gravity', models.FloatField()),
                ('abv', models.FloatField()),
                ('notes', models.TextField()),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TastingNote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('notes', models.TextField()),
                ('rating', models.FloatField()),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beverage.homebrewbatch')),
            ],
        ),
        migrations.AddField(
            model_name='homebrewbatch',
            name='ingredients',
            field=models.ManyToManyField(to='beverage.ingredient'),
        ),
    ]
