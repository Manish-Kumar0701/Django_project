# Generated by Django 5.0.3 on 2024-03-07 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_name', models.CharField(max_length=100)),
                ('car_speed', models.IntegerField(default=50)),
            ],
        ),
        migrations.RenameField(
            model_name='recipe',
            old_name='recipe_discription',
            new_name='recipe_description',
        ),
    ]