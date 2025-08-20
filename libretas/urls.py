from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    
    # Supervisores
    path('supervisores/', views.SupervisorListView.as_view(), name='supervisor-list'),
    path('supervisores/nuevo/', views.SupervisorCreateView.as_view(), name='supervisor-create'),
    path('supervisores/<int:pk>/editar/', views.SupervisorUpdateView.as_view(), name='supervisor-update'),
    path('supervisores/<int:pk>/eliminar/', views.SupervisorDeleteView.as_view(), name='supervisor-delete'),
    
    # Conductores
    path('conductores/', views.ConductorListView.as_view(), name='conductor-list'),
    path('conductores/nuevo/', views.ConductorCreateView.as_view(), name='conductor-create'),
    path('conductores/<int:pk>/editar/', views.ConductorUpdateView.as_view(), name='conductor-update'),
    path('conductores/<int:pk>/eliminar/', views.ConductorDeleteView.as_view(), name='conductor-delete'),
    
    # Seguimiento de libretas
    path('seguimiento/', views.SeguimientoLibretasView.as_view(), name='seguimiento-libretas'),
    path('actualizar-estado/', views.ActualizarEstadoLibretaView.as_view(), name='actualizar-estado-libreta'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard-libretas'),
    path('seguimiento/export/csv/', views.ExportSeguimientoCSVView.as_view(), name='seguimiento-export-csv'),
    path('seguimiento/export/xlsx/', views.ExportSeguimientoExcelView.as_view(), name='seguimiento-export-xlsx'),
]