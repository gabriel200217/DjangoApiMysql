# Generated by Django 4.1.2 on 2022-11-25 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('it', '0005_remove_impresoras_informacion_alter_impresoras_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='impresoras',
            name='codigo_inventario',
        ),
        migrations.AddField(
            model_name='impresoras',
            name='tipo_impresion',
            field=models.CharField(choices=[('CINTA', 'Cinta'), ('TONER', 'Toner'), ('RIBON', 'Ribon'), ('TINTA', 'Tinta')], default=1, max_length=45),
            preserve_default=False,
        ),
    ]