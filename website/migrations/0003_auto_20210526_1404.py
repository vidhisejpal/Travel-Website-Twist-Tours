# Generated by Django 3.1.7 on 2021-05-26 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_poupular_destination_destination_days'),
    ]

    operations = [
        migrations.CreateModel(
            name='Travel_Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trip_title', models.CharField(max_length=100)),
                ('trip_choice', models.CharField(choices=[('Choose', 'Choose'), ('Trending Trips', 'Trending Trips'), ('Popular Trips', 'Popular Trips')], default='Choose', max_length=50)),
                ('trip_days', models.IntegerField(default=0)),
                ('trip_description', models.TextField(blank=True)),
                ('trip_price', models.IntegerField(default=0)),
                ('trip_image', models.ImageField(default='', upload_to='tnt/images')),
            ],
        ),
        migrations.DeleteModel(
            name='Poupular_Destination',
        ),
    ]
