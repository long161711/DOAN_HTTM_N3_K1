# Generated by Django 3.1.3 on 2020-12-11 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LOGIN', '0017_delete_api'),
    ]

    operations = [
        migrations.CreateModel(
            name='API',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thoigian', models.DateTimeField()),
                ('nhietdo', models.FloatField()),
                ('doam', models.FloatField()),
                ('luongnuocdudoan', models.FloatField()),
            ],
        ),
    ]
