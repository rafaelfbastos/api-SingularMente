# Generated by Django 4.2.5 on 2023-09-29 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Texto')),
                ('background', models.IntegerField(default=1)),
                ('isLottie', models.BooleanField(verbose_name='Lottie?')),
                ('createDate', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Pílula',
                'verbose_name_plural': 'Pílulas',
            },
        ),
    ]
