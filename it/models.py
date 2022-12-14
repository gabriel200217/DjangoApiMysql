from django.db import models

# Create your models here.

# class departamentos(models.Model):
#     nombre = models.CharField(max_length=45)

class empresas(models.Model):
    nombre = models.CharField(max_length=45)

class marcas(models.Model):
    nombre = models.CharField(max_length=45)

class departamentos(models.Model):
    # departamentosforeignkey = models.ForeignKey(departamentos, on_delete=models.CASCADE, related_name="departamentos_de", null="True")
    nombre = models.CharField(max_length=45)
    empresasforeignkey = models.ForeignKey(empresas, on_delete=models.CASCADE, related_name="empresas_de", null="True")

class ubicaciones(models.Model):
    nombre = models.CharField(max_length=45)
    empresasforeingkey = models.ForeignKey(empresas, on_delete=models.CASCADE, related_name="empresas_ub", null="True")

class usuarios(models.Model):
    nombre = models.CharField(max_length=45)
    cargo = models.CharField(max_length=45)
    departamentosforeignkey = models.ForeignKey(departamentos, on_delete=models.CASCADE, related_name="departamentos_empresas_us", null="True")
    
class informacion(models.Model):
    estatus = models.CharField(max_length=45)
    asignacion = models.CharField(max_length=45)
    observacion = models.TextField()
    ubicacionesforeignkey = models.ForeignKey(ubicaciones, on_delete=models.CASCADE, related_name="ubicaciones_user", null="True")
    # usuariosforeignkey = models.ForeignKey(usuarios, on_delete=models.CASCADE, related_name="informacion_us", null="True")

class modelos(models.Model):
    nombre = models.CharField(max_length=45)
    marcasforeignkey = models.ForeignKey(marcas, on_delete=models.CASCADE, related_name="marcas_m", null="True")

class equipos(models.Model):
    id = models.OneToOneField(informacion, primary_key=True, unique=True, on_delete=models.CASCADE, related_name="informacion_eq")
    tipo_equipo = models.CharField(max_length=45)
    modelosforeignkey = models.ForeignKey(modelos, on_delete=models.CASCADE, related_name="modelos_eq", null="True")
    serial = models.CharField(max_length=45)
    serial_unidad = models.CharField(max_length=45)
    serial_cargador = models.CharField(max_length=45)
    csb= models.CharField(max_length=45)
    dd = models.CharField(max_length=45)
    ram = models.CharField(max_length=45)
    tipo_ram = models.CharField(max_length=45)
    antivirus = models.CharField(max_length=45)
    so = models.CharField(max_length=45)
    usuario_so = models.CharField(max_length=45)
    usuariosforeignkey = models.ForeignKey(usuarios, on_delete=models.CASCADE, related_name="equipos_us", null="True")

class impresoras(models.Model):
    codigo_inventario = models.CharField(max_length=45)
    serial = models.CharField(max_length=45)
    csb = models.CharField(max_length=45)
    cbc = models.CharField(max_length=45)
    tipo_impresion = models.CharField(max_length=45)
    tipo_conexion = models.CharField(max_length=45)
    ip = models.CharField(max_length=45)
    propiedad = models.CharField(max_length=45)
    informacionforeignkey = models.ForeignKey(informacion, on_delete=models.CASCADE, related_name="informacion_im", null="True")
    modelosforeignkey = models.ForeignKey(modelos, on_delete=models.CASCADE, related_name="modelos_imp", null="True")

class dispositivos(models.Model):
    serial = models.CharField(max_length=45)
    modelosforeignkey = models.ForeignKey(modelos, on_delete=models.CASCADE, related_name="modelos_dis", null="True")
    informacionforeignkey = models.ForeignKey(informacion, on_delete=models.CASCADE, related_name="informacion_dis", null="True")
    usuariosforeignkey = models.ForeignKey(usuarios, on_delete=models.CASCADE, related_name="dispositivos_us", null="True")

# class capacidad_dispositivos(models.Model):
#     capacidad = models.IntegerField()
#     dispositivosforeignkey = models.ForeignKey(dispositivos, on_delete=models.CASCADE, related_name="dispositivos_cap", null="True")