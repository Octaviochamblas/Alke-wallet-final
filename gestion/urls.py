from django.urls import path
from .views import (
    inicio,
    CuentaListView, CuentaDetailView, CuentaCreateView,
    CuentaUpdateView, CuentaDeleteView,
    TransaccionListView, TransaccionCreateView
)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('cuentas/', CuentaListView.as_view(), name='cuenta_list'),
    path('cuentas/nueva/', CuentaCreateView.as_view(), name='cuenta_create'),
    path('cuentas/<int:pk>/', CuentaDetailView.as_view(), name='cuenta_detail'),
    path('cuentas/<int:pk>/editar/', CuentaUpdateView.as_view(), name='cuenta_update'),
    path('cuentas/<int:pk>/eliminar/', CuentaDeleteView.as_view(), name='cuenta_delete'),

    path('transacciones/', TransaccionListView.as_view(), name='transaccion_list'),
    path('transacciones/nueva/', TransaccionCreateView.as_view(), name='transaccion_create'),
]