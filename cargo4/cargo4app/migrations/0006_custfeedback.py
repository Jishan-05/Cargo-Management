# Generated by Django 5.0.7 on 2024-08-18 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargo4app', '0005_booking_inquiries'),
    ]

    operations = [
        migrations.CreateModel(
            name='Custfeedback',
            fields=[
                ('fb_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('custfeedback', models.TextField()),
            ],
            options={
                'db_table': 'custfeedback',
                'managed': False,
            },
        ),
    ]
