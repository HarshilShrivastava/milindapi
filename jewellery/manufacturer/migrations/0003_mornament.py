# Generated by Django 3.0.4 on 2020-03-14 12:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('manufacturer', '0002_auto_20200312_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='MOrnament',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Type', models.CharField(max_length=50)),
                ('Manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='manufacturer.Manufacturer')),
            ],
        ),
    ]
