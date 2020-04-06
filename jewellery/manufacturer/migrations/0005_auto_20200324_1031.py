# Generated by Django 3.0.4 on 2020-03-24 10:31

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wholeseller', '0004_wbucket_wri'),
        ('manufacturer', '0004_mbucket_mwi'),
    ]

    operations = [
        migrations.CreateModel(
            name='MWIC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('Manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ManufacturerC', to='manufacturer.Manufacturer')),
                ('Wholeseller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='WholesellerC', to='wholeseller.Wholeseller')),
            ],
        ),
        migrations.CreateModel(
            name='MWIR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(blank=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('rejected', models.DateTimeField(blank=True, null=True)),
                ('viewed', models.DateTimeField(blank=True, null=True)),
                ('Manufacturer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ManufacturerR', to='manufacturer.Manufacturer')),
                ('Wholeseller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='WholesellerR', to='wholeseller.Wholeseller')),
            ],
        ),
        migrations.DeleteModel(
            name='MWI',
        ),
    ]