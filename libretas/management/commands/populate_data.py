from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from libretas.models import Supervisor, Conductor, EntregaLibreta
from django.utils import timezone
import random

class Command(BaseCommand):
    help = 'Pobla la base de datos con datos de prueba para el dashboard'

    def handle(self, *args, **options):
        self.stdout.write('Poblando base de datos con datos de prueba...')
        
        # Crear superusuario si no existe
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
            self.stdout.write('Superusuario creado: admin/admin123')
        
        # Crear supervisores de prueba
        supervisores_data = [
            {'nombre': 'Juan Pérez'},
            {'nombre': 'María García'},
            {'nombre': 'Carlos López'},
        ]
        
        supervisores = []
        for data in supervisores_data:
            supervisor, created = Supervisor.objects.get_or_create(
                nombre=data['nombre']
            )
            supervisores.append(supervisor)
            if created:
                self.stdout.write(f'Supervisor creado: {supervisor.nombre}')
        
        # Crear conductores de prueba
        conductores_data = [
            {'nombre': 'Pedro Rodríguez', 'supervisor': supervisores[0]},
            {'nombre': 'Ana Martínez', 'supervisor': supervisores[0]},
            {'nombre': 'Luis Fernández', 'supervisor': supervisores[1]},
            {'nombre': 'Carmen Ruiz', 'supervisor': supervisores[1]},
            {'nombre': 'Roberto Díaz', 'supervisor': supervisores[2]},
            {'nombre': 'Isabel Moreno', 'supervisor': supervisores[2]},
        ]
        
        conductores = []
        for data in conductores_data:
            conductor, created = Conductor.objects.get_or_create(
                nombre=data['nombre'],
                defaults={'supervisor': data['supervisor']}
            )
            conductores.append(conductor)
            if created:
                self.stdout.write(f'Conductor creado: {conductor.nombre}')
        
        # Crear datos de entrega de libretas para el mes actual
        hoy = timezone.now()
        mes_actual = hoy.month
        anio_actual = hoy.year
        
        # Estados posibles
        estados = ['ENTREGADO', 'PENDIENTE', 'NO_ENTREGADO']
        
        # Crear entregas de libretas para las 4 semanas del mes
        for semana in range(1, 5):
            for conductor in conductores:
                # Generar estado aleatorio con más probabilidad de entregado
                estado = random.choices(estados, weights=[60, 30, 10])[0]
                
                entrega, created = EntregaLibreta.objects.get_or_create(
                    conductor=conductor,
                    mes=mes_actual,
                    anio=anio_actual,
                    semana=semana,
                    defaults={'estado': estado}
                )
                
                if created:
                    self.stdout.write(f'Entrega creada: {conductor.nombre} - Semana {semana} - {estado}')
        
        self.stdout.write(
            self.style.SUCCESS('¡Datos de prueba creados exitosamente!')
        )
        self.stdout.write('Ahora puedes acceder al dashboard y ver los datos.')
        self.stdout.write('Credenciales de acceso: admin/admin123') 