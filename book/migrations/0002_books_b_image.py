# Generated by Django 3.0.2 on 2020-08-01 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='b_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
