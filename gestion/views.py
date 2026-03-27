from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Cuenta, Transaccion
from django.shortcuts import redirect

def inicio(request):
    return redirect('cuenta_list')

class CuentaListView(ListView):
    model = Cuenta
    template_name = 'gestion/cuenta_list.html'
    context_object_name = 'cuentas'


class CuentaDetailView(DetailView):
    model = Cuenta
    template_name = 'gestion/cuenta_detail.html'
    context_object_name = 'cuenta'


class CuentaCreateView(CreateView):
    model = Cuenta
    template_name = 'gestion/cuenta_form.html'
    fields = ['cliente', 'numero_cuenta', 'tipo_cuenta', 'saldo', 'activa']
    success_url = reverse_lazy('cuenta_list')


class CuentaUpdateView(UpdateView):
    model = Cuenta
    template_name = 'gestion/cuenta_form.html'
    fields = ['cliente', 'numero_cuenta', 'tipo_cuenta', 'saldo', 'activa']
    success_url = reverse_lazy('cuenta_list')


class CuentaDeleteView(DeleteView):
    model = Cuenta
    template_name = 'gestion/cuenta_confirm_delete.html'
    success_url = reverse_lazy('cuenta_list')


class TransaccionListView(ListView):
    model = Transaccion
    template_name = 'gestion/transaccion_list.html'
    context_object_name = 'transacciones'


class TransaccionCreateView(CreateView):
    model = Transaccion
    template_name = 'gestion/transaccion_form.html'
    fields = ['cuenta', 'tipo', 'monto', 'descripcion']
    success_url = reverse_lazy('transaccion_list')