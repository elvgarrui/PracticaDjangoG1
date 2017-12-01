from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'principal.views.inicio', name='Inicio'),
    url(r'^login/', 'principal.views.real_login'),
    url(r'^signin/', 'principal.views.real_signin'),
    url(r'^logout/', 'principal.views.real_logout'),
    url(r'^listBancos/', 'principal.views.real_logout'),
    url(r'^listMovimientos/', 'principal.views.real_logout'),
    url(r'^logout/', 'principal.views.real_logout'),
    url(r'^creaSucursal/', 'principal.views.create_sucursal'),
    url(r'^creaCuenta/', 'principal.views.create_cuenta'),
    url(r'^creaTipoMovimiento/', 'principal.views.create_tipo_de_movimiento'),
    url(r'^creaMovimiento/', 'principal.views.create_movimiento'),
    url(r'^creaBanco/', 'principal.views.create_banco'),


    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)
