# Generated by Django 3.0.4 on 2020-03-12 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
        ('citizen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizen',
            name='User',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='User.user'),
        ),
    ]
