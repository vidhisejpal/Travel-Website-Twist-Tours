# Generated by Django 3.1.7 on 2021-05-24 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poupular_Destination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination_title', models.CharField(max_length=100)),
                ('destination_description', models.TextField(blank=True)),
                ('destination_price', models.IntegerField(default=0)),
                ('destination_image', models.ImageField(default='', upload_to='tnt/images')),
            ],
        ),
    ]
