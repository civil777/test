# Generated by Django 3.1.3 on 2020-12-11 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.timestampedmodel')),
                ('file', models.ImageField(upload_to='product_photos')),
            ],
            bases=('core.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.timestampedmodel')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('address', models.CharField(max_length=140)),
                ('special_item', models.BooleanField(default=False)),
                ('time', models.TimeField()),
            ],
            bases=('core.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.timestampedmodel')),
                ('name', models.CharField(max_length=80)),
            ],
            options={
                'abstract': False,
            },
            bases=('core.timestampedmodel',),
        ),
    ]
