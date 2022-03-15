from django.db import models

# Create your models here.
class LugarTurismo(models.Model):
    descripcion=models.CharField('Descripcion', max_length=20)
    lugar=models.CharField('Lugar', max_length=20)
    fecha=models.DateField('Fecha',)
   
    class Meta: 
        verbose_name="Turismo"
        verbose_name_plural="Lugares Turisticos"


class TipoTransporte(models.Model):
    tipo=models.CharField('Tipo', max_length=20)

    def __str__(self):
        return f'{self.tipo}'

    class Meta: 
        verbose_name="Tipo Transporte"
        verbose_name_plural="Tipos Transportes"


class EmpresaTransporte(models.Model):
    cod_Empresa=models.CharField('Cod_Empresa', max_length=20)
    nombre=models.CharField('Nombre', max_length=20)
    direccion=models.CharField('Direccion', max_length=20)
    Fecha_insc=models.DateField('Fecha')
    tipo_empresa=models.ForeignKey(TipoTransporte, related_name="+", on_delete=models.PROTECT)
    #pais=models.ForeignKey(Pais, related_name="+", on_delete=models.PROTECT, null = True, blank = True)

    class Meta: 
        verbose_name="Empresa"
        verbose_name_plural="Empresas Registradas"
