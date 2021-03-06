# Generated by Django 3.0.4 on 2020-04-06 09:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('retailer', '0004_rbucket'),
        ('wholeseller', '0004_wbucket_wri'),
    ]

    operations = [
        migrations.CreateModel(
            name='WRIC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Wholeseller1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Wholeseller1C', to='wholeseller.Wholeseller')),
                ('retailer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='retailerC', to='retailer.retailer')),
            ],
        ),
    ]
