# Generated by Django 3.1.3 on 2020-12-11 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LOGIN', '0015_wdudoan'),
    ]

    operations = [
        migrations.CreateModel(
            name='API',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thoigian', models.DateTimeField()),
                ('nhietdo', models.FloatField()),
                ('doam', models.FloatField()),
            ],
        ),
    ]
