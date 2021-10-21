# Generated by Django 3.1.7 on 2021-06-06 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0016_delete_travel_destination'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel_Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_title', models.CharField(max_length=100)),
                ('trip_choice', models.CharField(choices=[('Choose', 'Choose'), ('Trending Trips', 'Trending Trips'), ('Popular Trips', 'Popular Trips'), ('Treks', 'Treks')], default='Choose', max_length=50)),
                ('trip_drive_link', models.CharField(default='#', max_length=250)),
                ('trip_days', models.IntegerField(default=0)),
                ('trip_description', models.TextField(blank=True)),
                ('trip_price', models.IntegerField(default=0)),
                ('trip_location', models.CharField(max_length=100)),
                ('trip_image', models.ImageField(default='', upload_to='tnt/images')),
            ],
        ),
    ]