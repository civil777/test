# Generated by Django 3.1.2 on 2020-12-08 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Index',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(default='')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.timestampedmodel')),
                ('이름', models.CharField(blank=True, default='', max_length=10)),
                ('전화번호', models.CharField(blank=True, default='', max_length=13)),
                ('이메일', models.CharField(blank=True, default='', max_length=50)),
                ('주소', models.CharField(blank=True, default='', max_length=50)),
                ('문의사항', models.TextField(blank=True, default='')),
            ],
            bases=('core.timestampedmodel',),
        ),
    ]
