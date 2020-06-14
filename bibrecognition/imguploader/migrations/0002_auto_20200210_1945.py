# Generated by Django 3.0.3 on 2020-02-10 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imguploader', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='image',
            field=models.ImageField(default='placeholder.jpg', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='photo',
            name='name',
            field=models.CharField(default='Zdjecie', max_length=100),
        ),
    ]
