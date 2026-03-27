from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Cuenta, Transaccion
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from decimal import Decimal
from django.contrib import messages


def inicio(request):
    return redirect('cuenta_list')

class InicioView(TemplateView):
    template_name = 'gestion/inicio.html'

class CuentaListView(LoginRequiredMixin, ListView):
    model = Cuenta
    template_name = 'gestion/cuenta_list.html'
    context_object_name = 'cuentas'


class CuentaDetailView(LoginRequiredMixin, DetailView):
    model = Cuenta
    template_name = 'gestion/cuenta_detail.html'
    context_object_name = 'cuenta'


class CuentaCreateView(LoginRequiredMixin, CreateView):
    model = Cuenta
    template_name = 'gestion/cuenta_form.html'
    fields = ['cliente', 'numero_cuenta', 'tipo_cuenta', 'saldo', 'activa']
    success_url = reverse_lazy('cuenta_list')


class CuentaUpdateView(LoginRequiredMixin, UpdateView):
    model = Cuenta
    template_name = 'gestion/cuenta_form.html'
    fields = ['cliente', 'numero_cuenta', 'tipo_cuenta', 'saldo', 'activa']
    success_url = reverse_lazy('cuenta_list')


class CuentaDeleteView(LoginRequiredMixin, DeleteView):
    model = Cuenta
    template_name = 'gestion/cuenta_confirm_delete.html'
    success_url = reverse_lazy('cuenta_list')


class TransaccionListView(LoginRequiredMixin, ListView):
    model = Transaccion
    template_name = 'gestion/transaccion_list.html'
    context_object_name = 'transacciones'



class TransaccionCreateView(LoginRequiredMixin, CreateView):
    model = Transaccion
    template_name = 'gestion/transaccion_form.html'
    fields = ['cuenta', 'cuenta_destino', 'tipo', 'monto', 'descripcion']
    success_url = reverse_lazy('transaccion_list')

    def form_valid(self, form):
        transaccion = form.save(commit=False)
        cuenta = transaccion.cuenta
        cuenta_destino = transaccion.cuenta_destino
        monto = transaccion.monto

        if transaccion.tipo in ['deposito', 'retiro']:
            transaccion.cuenta_destino = None
            cuenta_destino = None

        if transaccion.tipo == 'deposito':
            if not cuenta:
                form.add_error('cuenta', 'Debes seleccionar una cuenta para el depósito.')
                return self.form_invalid(form)
            cuenta.saldo += monto
            cuenta.save()

        elif transaccion.tipo == 'retiro':
            if not cuenta:
                form.add_error('cuenta', 'Debes seleccionar una cuenta para el retiro.')
                return self.form_invalid(form)
            if cuenta.saldo < monto:
                form.add_error('monto', 'Saldo insuficiente para realizar el retiro.')
                return self.form_invalid(form)
            cuenta.saldo -= monto
            cuenta.save()

        elif transaccion.tipo == 'transferencia':
            if not cuenta:
                form.add_error('cuenta', 'Debes seleccionar una cuenta de origen.')
                return self.form_invalid(form)

            if not cuenta_destino:
                form.add_error('cuenta_destino', 'Debes seleccionar una cuenta de destino.')
                return self.form_invalid(form)

            if cuenta == cuenta_destino:
                form.add_error('cuenta_destino', 'La cuenta de destino no puede ser la misma que la de origen.')
                return self.form_invalid(form)

            if cuenta.saldo < monto:
                form.add_error('monto', 'Saldo insuficiente para realizar la transferencia.')
                return self.form_invalid(form)

            cuenta.saldo -= monto
            cuenta_destino.saldo += monto
            cuenta.save()
            cuenta_destino.save()

        self.object = transaccion
        self.object.save()

        messages.success(self.request, 'Transacción registrada correctamente.')
        return redirect(self.success_url)