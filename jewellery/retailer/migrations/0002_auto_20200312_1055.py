# Generated by Django 3.0.4 on 2020-03-12 10:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
        ('retailer', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='retailer',
            name='User',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='User.user'),
        ),
    ]