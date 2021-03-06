# Generated by Django 3.2.8 on 2021-10-31 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('confirmed', 'confirmed'), ('canceled', 'canceled')], default='pending', max_length=12)),
                ('check_in', models.DateField()),
                ('check_out', models.DateField()),
                ('place', models.CharField(choices=[('guesthouse', 'guest house'), ('hairsalon', 'hairsalon'), ('facility', 'facility')], default='null', max_length=12)),
                ('time_in', models.TimeField(blank=True, null=True)),
                ('time_out', models.TimeField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
