# Generated by Django 3.0.3 on 2020-03-13 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200313_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default='kertna', max_length=300),
        ),
    ]
