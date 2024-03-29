# Generated by Django 3.1.7 on 2021-05-27 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_trek'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('user_image', models.ImageField(default='', upload_to='tnt/images')),
                ('review_description', models.TextField(blank=True)),
            ],
        ),
    ]
