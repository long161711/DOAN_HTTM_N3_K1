# Generated by Django 3.1.3 on 2020-12-09 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LOGIN', '0014_delete_wdudoan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Wdudoan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('wnhietdo', models.FloatField()),
                ('wdoam', models.FloatField()),
                ('wsonguoi', models.FloatField()),
            ],
        ),
    ]
