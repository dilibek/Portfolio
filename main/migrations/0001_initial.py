# Generated by Django 4.0.2 on 2022-02-09 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fi', models.CharField(max_length=50)),
                ('staff', models.CharField(max_length=25)),
                ('photo', models.ImageField(upload_to='info')),
                ('gmail', models.CharField(max_length=25)),
                ('address', models.CharField(max_length=255)),
                ('birthday', models.DateField()),
                ('phone', models.CharField(max_length=13)),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tech', models.CharField(max_length=50)),
                ('percent', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='SMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('icon', models.CharField(max_length=25)),
                ('color', models.CharField(choices=[('fac', 'fac'), ('twi', 'twi'), ('dri', 'dri'), ('ins', 'ins')], max_length=3)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
    ]
