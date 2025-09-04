from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Supervisor(models.Model):
    nombre = models.CharField(max_length=100)
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='supervisor_profile')
    
    def __str__(self):
        return self.nombre
    
    class Meta:
        verbose_name_plural = "Supervisores"

class Conductor(models.Model):
    nombre = models.CharField(max_length=100)
    supervisor = models.ForeignKey(Supervisor, on_delete=models.CASCADE, related_name='conductores')
    
    def __str__(self):
        return self.nombre

class EntregaLibreta(models.Model):
    ESTADOS = [
        ('PENDIENTE', 'Pendiente'),
        ('ENTREGADO', 'Entregado'),
        ('NO_ENTREGADO', 'No Entregado'),
        ('DESVINCULADO', 'Desvinculado'),
        ('LICENCIA_MEDICA', 'Licencia Médica'),
    ]
    
    conductor = models.ForeignKey(Conductor, on_delete=models.CASCADE)
    fecha_entrega = models.DateField(default=timezone.now)
    mes = models.IntegerField()
    anio = models.IntegerField()
    semana = models.IntegerField()
    estado = models.CharField(max_length=20, choices=ESTADOS, default='PENDIENTE')
    
    class Meta:
        unique_together = ['conductor', 'mes', 'anio', 'semana']
        verbose_name = "Entrega de Libreta"
        verbose_name_plural = "Entregas de Libretas"
    
    def __str__(self):
        return f"{self.conductor} - {self.mes}/{self.anio} - Semana {self.semana}"
