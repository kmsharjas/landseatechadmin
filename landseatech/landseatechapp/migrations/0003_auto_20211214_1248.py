# Generated by Django 3.2.5 on 2021-12-14 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landseatechapp', '0002_auto_20211214_0940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='big',
            field=models.FileField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='medium',
            field=models.FileField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='image',
            name='small',
            field=models.FileField(null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='title_img',
            field=models.FileField(null=True, upload_to='images/'),
        ),
    ]