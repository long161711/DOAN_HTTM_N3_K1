# Generated by Django 3.1.3 on 2020-11-26 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LOGIN', '0004_dulieudauvao_songuoi'),
    ]

    operations = [
        migrations.CreateModel(
            name='dulieuhocmay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('luongnuoc', models.FloatField()),
            ],
        ),
    ]
