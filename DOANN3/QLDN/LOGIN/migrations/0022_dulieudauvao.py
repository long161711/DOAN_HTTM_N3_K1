# Generated by Django 3.1.3 on 2020-12-19 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LOGIN', '0021_delete_dulieudauvao'),
    ]

    operations = [
        migrations.CreateModel(
            name='dulieudauvao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thoigian', models.DateTimeField()),
                ('nhietdo', models.FloatField()),
                ('doam', models.FloatField()),
                ('songuoi', models.IntegerField()),
                ('luongnuoc', models.FloatField()),
                ('luongnuocdudoan', models.FloatField()),
            ],
        ),
    ]
