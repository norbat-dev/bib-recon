# Generated by Django 3.0.2 on 2020-02-02 02:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Competitions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comp_slug', models.CharField(max_length=100)),
                ('comp_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=50)),
                ('comp_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imguploader.Competitions')),
            ],
        ),
        migrations.CreateModel(
            name='PhotoMeta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_key', models.CharField(max_length=50)),
                ('meta_value', models.CharField(max_length=50)),
                ('photo_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='imguploader.Photo')),
            ],
        ),
    ]
