from django.contrib import admin
from .models import LugarTurismo
from .models import TipoTransporte
from .models import EmpresaTransporte
#from .models import Pais

class LugarTurismoAdmin(admin.ModelAdmin):
    search_fields = ('fecha', 'lugar', 'descripcion')
    list_display = ("descripcion", "lugar", "fecha")
    list_filter = ("fecha",)

admin.site.register(LugarTurismo, LugarTurismoAdmin)


class TipoTransporteAdmin(admin.ModelAdmin):
    pass


admin.site.register(TipoTransporte, TipoTransporteAdmin)


class EmpresaAdmin(admin.ModelAdmin):
   pass


admin.site.register(EmpresaTransporte,EmpresaAdmin)

#class PaisAdmin(admin.ModelAdmin):
#    pass


#admin.site.register(Pais, PaisAdmin)