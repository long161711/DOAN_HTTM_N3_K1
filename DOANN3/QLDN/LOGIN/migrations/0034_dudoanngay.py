# Generated by Django 3.1.3 on 2020-12-25 16:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LOGIN', '0033_theongay'),
    ]

    operations = [
        migrations.CreateModel(
            name='dudoanngay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thoigian', models.DateField()),
                ('luongnuocdudoan', models.FloatField()),
            ],
        ),
    ]
