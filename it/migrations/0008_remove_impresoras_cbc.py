# Generated by Django 4.1.2 on 2022-11-25 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('it', '0007_alter_impresoras_tipo_impresion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='impresoras',
            name='cbc',
        ),
    ]
