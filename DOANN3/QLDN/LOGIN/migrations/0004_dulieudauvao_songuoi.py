# Generated by Django 3.1.3 on 2020-11-26 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LOGIN', '0003_dulieudauvao'),
    ]

    operations = [
        migrations.AddField(
            model_name='dulieudauvao',
            name='songuoi',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
