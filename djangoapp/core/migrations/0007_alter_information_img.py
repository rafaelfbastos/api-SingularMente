# Generated by Django 4.2.7 on 2023-11-08 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_information_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='information',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='img/', verbose_name='imagem'),
        ),
    ]
