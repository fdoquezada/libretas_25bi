from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf.urls import handler404, handler500, handler403, handler400

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('libretas.urls')),  # URLs de libretas como página principal
    path('auth/', include('autentication.urls', namespace='auth')),  # URLs de autenticación con namespace
    path('contacto/', include('contacto.urls')),
    path('/.well-known/appspecific/com.chrome.devtools.json', TemplateView.as_view(template_name='empty.json')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Configuración de las vistas de error
handler404 = 'core.views.error_404'
handler500 = 'core.views.error_500'
handler403 = 'core.views.error_403'
handler400 = 'core.views.error_400' 