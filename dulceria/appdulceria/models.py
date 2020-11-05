from django.db import models

class TipoUsuario(models.Model):
    id = models.IntegerField(primary_key=True)
    descripcion = models.CharField(max_length=50,null=False)
    class Meta:
        db_table = "tipo_usuario"
class Usuario(models.Model):
    rut = models.CharField(max_length=10,primary_key=True)
    nombre = models.CharField(max_length=100,null=False)
    apellido_paterno = models.CharField(max_length=100,null=False)
    apellido_materno = models.CharField(max_length=100,null=False)
    nick = models.CharField(max_length=15,null=False)
    correo = models.EmailField(null=False)
    fecha_nacimiento = models.DateField(null=False)
    contrasena = models.CharField(max_length=50,null=False)
    tipoUsuario = models.ForeignKey(TipoUsuario,on_delete=models.CASCADE,default=2)
    class Meta:
        db_table = "usuario"
class SolicitudDulces(models.Model):
    id_solicitud = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100,null=False)
    apellido_paterno = models.CharField(max_length=100,null=False)
    correo = models.EmailField(null=False)
    descripcion = models.CharField(max_length=500,null=False)
    dulce_dia = models.BooleanField()
    direccion = models.CharField(max_length=150, null=False)
    entrega_inmediata = models.BooleanField()
    factura = models.BooleanField()
    class Meta: 
        db_table = "solicitud_dulces"
class Producto(models.Model):
    id_producto = models.CharField(max_length=4,primary_key=True)
    nombre = models.CharField(max_length=100,null=False)
    valor = models.IntegerField(null=False)
    class Meta:
        db_table = "producto"
class ItemCarrito(models.Model):
    id_item = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    rut = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    cantidad = models.IntegerField(null=False)
    class Meta:
        db_table = "item_carrito"