# Generated by Django 4.1.2 on 2022-11-25 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('it', '0009_alter_impresoras_tipo_conexion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impresoras',
            name='tipo_conexion',
            field=models.CharField(choices=[('RED', 'Red'), ('USB', 'Usb'), ('COMPARTIDA', 'Compartida'), ('NO APLICA', 'No aplica')], max_length=45),
        ),
    ]