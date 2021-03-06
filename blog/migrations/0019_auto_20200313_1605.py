# Generated by Django 3.0.3 on 2020-03-13 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_remove_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300, unique=True)),
                ('minprice', models.FloatField()),
                ('image', models.ImageField(blank='True', default='default.jpeg', upload_to='media/items')),
                ('category', models.CharField(max_length=300)),
                ('description', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
