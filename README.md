# Sistema de Seguimiento de Libretas 25 Bits

Sistema web desarrollado en Django para el seguimiento y gestión de libretas de conductores, con funcionalidades de autenticación, gestión de supervisores y conductores, y seguimiento de entregas. **Organizado según las mejores prácticas de Django.**

## 🚀 Características

- **Autenticación de Usuarios**
  - Registro de usuarios
  - Inicio de sesión con namespace `auth/`
  - Protección de rutas
  - Gestión de sesiones

- **Gestión de Supervisores**
  - Listado de supervisores
  - Creación de nuevos supervisores
  - Edición de información
  - Eliminación de registros

- **Gestión de Conductores**
  - Listado de conductores
  - Registro de nuevos conductores
  - Actualización de datos
  - Eliminación de registros

- **Seguimiento de Libretas**
  - Control de entregas por semana
  - Estado de libretas (Entregado/Pendiente/No Entregado)
  - Dashboard con estadísticas
  - Filtros por supervisor, mes y año

## 🛠️ Tecnologías Utilizadas

- **Backend**
  - Python 3.13
  - Django 5.2
  - Django Authentication System
  - Python Decouple (para variables de entorno)

- **Frontend**
  - HTML5
  - CSS3
  - Bootstrap 5
  - Font Awesome
  - JavaScript (Vanilla)
  - Chart.js (para gráficos del dashboard)

## 📋 Requisitos Previos

- Python 3.13 o superior
- pip (gestor de paquetes de Python)
- Entorno virtual (recomendado)

## 🔧 Instalación

1. Clonar el repositorio:
```bash
git clone [URL_DEL_REPOSITORIO]
cd [NOMBRE_DEL_DIRECTORIO]
```

2. Crear y activar entorno virtual:
```bash
python -m venv entorno
# En Windows
entorno\Scripts\activate
# En Linux/Mac
source entorno/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Configurar variables de entorno:
   - Crear archivo `.env` en la raíz del proyecto
   - Agregar las siguientes variables:
```
SECRET_KEY=tu_clave_secreta
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

5. Realizar migraciones:
```bash
python manage.py makemigrations
python manage.py migrate
```

6. Crear superusuario:
```bash
python manage.py createsuperuser
```

7. Iniciar el servidor:
```bash
python manage.py runserver
```

## 📁 Estructura del Proyecto (Organizada según Django Best Practices)

```
📁 Sistema de Libretas 25 Bits/
├── 📁 cacciuttolo/                    # Proyecto principal Django
│   ├── settings.py                   # Configuración del proyecto
│   ├── urls.py                      # URLs principales (con namespaces)
│   ├── wsgi.py                      # Configuración WSGI
│   └── asgi.py                      # Configuración ASGI
│
├── 📁 libretas/                      # Aplicación principal
│   ├── 📁 templates/
│   │   └── 📁 libretas/             # Namespace de templates
│   │       ├── home.html            # Página principal
│   │       ├── dashboard.html       # Dashboard de libretas
│   │       ├── seguimiento_libretas.html # Seguimiento de entregas
│   │       ├── conductor_list.html  # Lista de conductores
│   │       ├── conductor_form.html  # Formulario de conductores
│   │       ├── conductor_confirm_delete.html
│   │       ├── supervisor_list.html # Lista de supervisores
│   │       ├── supervisor_form.html # Formulario de supervisores
│   │       └── supervisor_confirm_delete.html
│   ├── models.py                    # Modelos: Supervisor, Conductor, EntregaLibreta
│   ├── views.py                     # Vistas de la aplicación
│   ├── urls.py                      # URLs de libretas
│   ├── forms.py                     # Formularios
│   └── admin.py                     # Configuración del admin
│
├── 📁 autentication/                # Aplicación de autenticación
│   ├── 📁 templates/
│   │   └── 📁 autentication/        # Namespace de templates
│   │       ├── login.html           # Página de login
│   │       ├── register.html        # Página de registro
│   │       └── dashboard.html       # Dashboard de usuario
│   ├── views.py                     # Vistas de autenticación
│   ├── urls.py                      # URLs con namespace 'auth'
│   ├── forms.py                     # Formularios de autenticación
│   └── models.py                    # Modelos de usuario (si aplica)
│
├── 📁 contacto/                     # Aplicación de contacto
│   ├── views.py
│   └── urls.py
│
├── 📁 core/                         # Aplicación core
│   └── views.py                     # Vistas de error (404, 500, etc.)
│
├── 📁 templates/                    # Templates base compartidos
│   ├── base.html                   # Template base principal
│   ├── errors/                     # Templates de errores
│   │   ├── 400.html
│   │   ├── 403.html
│   │   ├── 404.html
│   │   └── 500.html
│   └── empty.json                  # Para Chrome DevTools
│
├── 📁 static/                      # Archivos estáticos
│   ├── css/
│   ├── js/
│   └── images/
│
├── 📁 staticfiles/                 # Archivos estáticos recolectados
├── 📁 logs/                        # Archivos de log
├── 📁 certificates/                # Certificados SSL (si aplica)
├── 📁 entorno/                     # Entorno virtual
├── manage.py                       # Script de gestión de Django
├── requirements.txt                # Dependencias del proyecto
├── .env                           # Variables de entorno (no versionado)
├── .gitignore                     # Archivos ignorados por Git
└── README.md                      # Este archivo
```

## 🔗 Configuración de URLs (Namespaces)

### URLs Principales (`cacciuttolo/urls.py`)
```python
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('libretas.urls')),                    # Página principal
    path('auth/', include('autentication.urls', namespace='auth')), # Autenticación
    path('contacto/', include('contacto.urls')),
]
```

### URLs de Autenticación (`autentication/urls.py`)
```python
app_name = 'auth'  # Namespace configurado

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
```

### URLs de Libretas (`libretas/urls.py`)
```python
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('supervisores/', views.SupervisorListView.as_view(), name='supervisor-list'),
    path('conductores/', views.ConductorListView.as_view(), name='conductor-list'),
    path('seguimiento/', views.SeguimientoLibretasView.as_view(), name='seguimiento-libretas'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard-libretas'),
    # ... más URLs
]
```

## 🎯 Referencias de URLs en Templates

### URLs de Autenticación (con namespace)
- `{% url 'auth:login' %}` - Iniciar sesión
- `{% url 'auth:logout' %}` - Cerrar sesión
- `{% url 'auth:register' %}` - Registro
- `{% url 'auth:dashboard' %}` - Dashboard de usuario

### URLs de Libretas
- `{% url 'home' %}` - Página principal
- `{% url 'supervisor-list' %}` - Lista de supervisores
- `{% url 'conductor-list' %}` - Lista de conductores
- `{% url 'seguimiento-libretas' %}` - Seguimiento de libretas
- `{% url 'dashboard-libretas' %}` - Dashboard de libretas

## 🔐 Variables de Entorno

El proyecto utiliza las siguientes variables de entorno:

- `SECRET_KEY`: Clave secreta para Django
- `DEBUG`: Modo de depuración (True/False)
- `ALLOWED_HOSTS`: Hosts permitidos
- `DATABASE_URL`: URL de la base de datos (opcional)

## 👥 Roles de Usuario

- **Superusuario**: Acceso total al sistema y admin de Django
- **Usuario Autenticado**: Acceso a todas las funcionalidades del sistema
- **Visitante**: Acceso solo a la página de inicio y autenticación

## 🚀 Uso

1. **Acceder al sistema:**
   - URL: `http://localhost:8000`
   - Iniciar sesión: `http://localhost:8000/auth/login/`
   - Registro: `http://localhost:8000/auth/register/`

2. **Navegación principal:**
   - **Inicio**: Vista general del sistema
   - **Supervisores**: Gestión completa de supervisores
   - **Conductores**: Gestión completa de conductores
   - **Seguimiento**: Control de libretas por semana
   - **Dashboard**: Estadísticas y gráficos

3. **Funcionalidades del Seguimiento:**
   - Filtros por supervisor, mes y año
   - Cambio de estado de libretas (Entregado/Pendiente/No Entregado)
   - Vista de tabla con estados por semana
   - Actualización en tiempo real

## ✅ Mejoras Implementadas (Buenas Prácticas)

### 🏗️ Organización de Templates
- ✅ **Templates organizados por app**: Cada app tiene su propia carpeta `templates/nombre_app/`
- ✅ **Template base compartido**: Solo `templates/base.html` en carpeta general
- ✅ **Namespaces de templates**: Evita conflictos de nombres entre apps
- ✅ **Estructura modular**: Fácil mantenimiento y escalabilidad

### 🔗 Configuración de URLs
- ✅ **Namespaces configurados**: `auth:` para autenticación
- ✅ **URLs organizadas**: Cada app maneja sus propias URLs
- ✅ **Referencias corregidas**: Todas las URLs funcionan correctamente
- ✅ **Estructura escalable**: Fácil agregar nuevas apps

### 🎨 Mejoras de UI/UX
- ✅ **Bootstrap 5**: Diseño moderno y responsive
- ✅ **Font Awesome**: Iconos consistentes
- ✅ **Chart.js**: Gráficos interactivos en dashboard
- ✅ **JavaScript**: Funcionalidades dinámicas

## 🤝 Contribución

1. Fork el proyecto
2. Crear una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir un Pull Request

## 📝 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo `LICENSE` para más detalles.

## ✨ Características Futuras

- [ ] Implementación de notificaciones por email
- [ ] Reportes PDF y Excel
- [ ] API REST para integración externa
- [ ] Panel de administración personalizado
- [ ] Sistema de auditoría de cambios
- [ ] Exportación de datos
- [ ] Dashboard con más métricas

## 🐛 Solución de Problemas

### Error: NoReverseMatch
Si encuentras errores de URLs, verifica:
1. Que los namespaces estén configurados correctamente
2. Que las referencias en templates usen el formato correcto: `{% url 'namespace:name' %}`
3. Que las URLs estén incluidas en el archivo principal

### Error: Template not found
Verifica que los templates estén en la ubicación correcta:
- Templates de app: `app/templates/app/`
- Templates base: `templates/`

## 📞 Soporte

Para soporte, por favor contactar a [fdoquezadapuno@gmail.com] o crear un issue en el repositorio.

---

**Desarrollado con ❤️ por [Fernando Quezada Puño]**

*Última actualización: Junio 2025 - Reorganización según Django Best Practices*
