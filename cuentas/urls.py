from django.urls import path
from .views import iniciar_sesion, registrarse, perfil, editar_perfil
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('iniciar-sesion/', iniciar_sesion, name='iniciar_sesion'),
    path('registrarse/', registrarse, name='registrarse'),
    path('cerrar-sesion/', LogoutView.as_view(template_name='cuentas/cerrar_sesion.html'), name='cerrar_sesion'),
    path('perfil/', perfil, name='perfil'),
    path('editar-perfil/', editar_perfil, name='editar_perfil')
]
