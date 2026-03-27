from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User


class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cliente')
    telefono = models.CharField(max_length=20, blank=True, null=True)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank=True, null=True)
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name() or self.user.username


class Cuenta(models.Model):
    TIPO_CUENTA_CHOICES = [
        ('ahorro', 'Cuenta de Ahorro'),
        ('corriente', 'Cuenta Corriente'),
        ('digital', 'Cuenta Digital'),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='cuentas')
    numero_cuenta = models.CharField(max_length=20, unique=True)
    tipo_cuenta = models.CharField(max_length=20, choices=TIPO_CUENTA_CHOICES)
    saldo = models.DecimalField(max_digits=12, decimal_places=2, default=0, validators=[MinValueValidator(0)])
    activa = models.BooleanField(default=True)
    creada_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.numero_cuenta} - {self.cliente}"


class Transaccion(models.Model):
    TIPO_TRANSACCION_CHOICES = [
        ('deposito', 'Depósito'),
        ('retiro', 'Retiro'),
        ('transferencia', 'Transferencia'),
    ]

    cuenta = models.ForeignKey(
        Cuenta,
        on_delete=models.CASCADE,
        related_name='transacciones',
        blank=True,
        null=True
    )
    cuenta_destino = models.ForeignKey(
        Cuenta,
        on_delete=models.CASCADE,
        related_name='transferencias_recibidas',
        blank=True,
        null=True
    )
    tipo = models.CharField(max_length=20, choices=TIPO_TRANSACCION_CHOICES)
    monto = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0.01)])
    descripcion = models.CharField(max_length=255, blank=True, null=True)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.tipo == 'transferencia' and self.cuenta_destino:
            return f"{self.tipo} - {self.monto} - {self.cuenta.numero_cuenta} a {self.cuenta_destino.numero_cuenta}"
        return f"{self.tipo} - {self.monto} - {self.cuenta.numero_cuenta if self.cuenta else 'Sin cuenta'}"