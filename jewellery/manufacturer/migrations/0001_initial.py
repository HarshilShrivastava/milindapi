# Generated by Django 3.0.4 on 2020-03-12 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Manufacturer', to='User.user')),
            ],
        ),
    ]
