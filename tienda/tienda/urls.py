"""tienda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('contacto.urls')),
    # path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # path('index/', TemplateView.as_view(template_name='index.html'), name='index'),
    path('', TemplateView.as_view(template_name='index.html'), name='index'),
    # path('contactanos/', TemplateView.as_view(template_name='contacto/list_mensajes.html'), name='contactanos'),
    path('donde_encontrarnos/', TemplateView.as_view(template_name='paginas/dondeencontrarnos.html'), name='donde_encontrarnos'),
    path('nuestros_clientes', TemplateView.as_view(template_name='paginas/nuestrosclientes.html'), name='nuestros_clientes'),
    path('quienes_somos', TemplateView.as_view(template_name='paginas/quienessomos.html'), name='quienes_somos'),
]

