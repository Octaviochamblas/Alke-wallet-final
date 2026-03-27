from django.contrib import admin
from .models import Cliente, Cuenta, Transaccion


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'telefono', 'creado_en')
    search_fields = ('user__username', 'user__first_name', 'user__last_name', 'telefono')


@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
    list_display = ('id', 'numero_cuenta', 'cliente', 'tipo_cuenta', 'saldo', 'activa', 'creada_en')
    search_fields = ('numero_cuenta', 'cliente__user__username')
    list_filter = ('tipo_cuenta', 'activa')


@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('id', 'cuenta', 'cuenta_destino', 'tipo', 'monto', 'fecha')
    search_fields = ('cuenta__numero_cuenta', 'cuenta_destino__numero_cuenta', 'descripcion')
    list_filter = ('tipo', 'fecha')