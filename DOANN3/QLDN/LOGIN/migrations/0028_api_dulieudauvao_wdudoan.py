# Generated by Django 3.1.3 on 2020-12-19 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LOGIN', '0027_auto_20201219_1200'),
    ]

    operations = [
        migrations.CreateModel(
            name='API',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thoigian', models.DateTimeField()),
                ('nhietdo', models.FloatField()),
                ('doam', models.FloatField()),
                ('songuoi', models.IntegerField()),
                ('khoangtg', models.IntegerField()),
                ('luongnuocdudoan', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='dulieudauvao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thoigian', models.DateTimeField()),
                ('nhietdo', models.FloatField()),
                ('doam', models.FloatField()),
                ('songuoi', models.IntegerField()),
                ('khoangtg', models.IntegerField()),
                ('luongnuoc', models.FloatField()),
                ('luongnuocdudoan', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Wdudoan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('wnhietdo', models.FloatField()),
                ('wdoam', models.FloatField()),
                ('wsonguoi', models.FloatField()),
                ('wkhoangtg', models.IntegerField()),
            ],
        ),
    ]
