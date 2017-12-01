from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, get_list_or_404
from django.template import RequestContext

from principal.forms import *
from principal.models import *


def inicio(request):
    autenticado = False
    user = request.user
    if request.user.is_authenticated():
        autenticado = True
    return render_to_response("inicio.html", {'auth':autenticado, 'usuario':user})

def real_login(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/')
    if request.method=='POST':
        formulario = LogInForm(request.POST)
        if formulario.is_valid():
            user = authenticate(username=formulario.cleaned_data['user'], password=formulario.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect('/')
            else:
                error = 'Usuario o Password incorrectos'
                return render_to_response('login.html',{'formulario':formulario, 'error':error}, context_instance=RequestContext(request)) 
    else:
        formulario = LogInForm()
    
    return render_to_response('login.html',{'formulario':formulario}, context_instance=RequestContext(request))

def real_logout(request):
    logout(request)
#     autenticado = 0
    return render_to_response("inicio.html", {'auth':False})

def real_signin(request):
    if not request.user.is_anonymous():
        return HttpResponseRedirect('/')
    if request.method=='POST':
        formulario = UsuarioForm(request.POST, request.FILES)
        if formulario.is_valid():
            if formulario.cleaned_data['password']==formulario.cleaned_data['password2']:
                usuario = User.objects.create_user(formulario.cleaned_data['user'], formulario.cleaned_data['email'], formulario.cleaned_data['password'])
                Usuario.objects.create(usuario=usuario, nombre=formulario.cleaned_data['nombre'], apellidos=formulario.cleaned_data['apellidos'])
                return HttpResponseRedirect('/login')
            else:
                error = "Las password no coinciden"
                return render_to_response('signin.html',{'formulario':formulario, 'error':error}, context_instance=RequestContext(request))
    else:
        formulario = UsuarioForm()
    return render_to_response('signin.html',{'formulario':formulario}, context_instance=RequestContext(request))

def create_sucursal(request):
    if request.method=='POST':
        formulario = SucursalesForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = SucursalesForm()
    return render_to_response('sucursal.html',{'formulario':formulario}, context_instance=RequestContext(request))

def create_cuenta(request):
    if request.method=='POST':
        formulario = CuentaForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = CuentaForm()
    return render_to_response('cuenta.html',{'formulario':formulario}, context_instance=RequestContext(request))

def create_banco(request):
    if request.method=='POST':
        formulario = BancoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = BancoForm()
    return render_to_response('nuevoBanco.html',{'formulario':formulario}, context_instance=RequestContext(request))

def create_movimiento(request):
    if request.method=='POST':
        formulario = MovimientoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = MovimientoForm()
    return render_to_response('movimiento.html',{'formulario':formulario}, context_instance=RequestContext(request))

def create_tipo_de_movimiento(request):
    if request.method=='POST':
        formulario = TipoMovimientoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return HttpResponseRedirect('/')
    else:
        formulario = TipoMovimientoForm()
    return render_to_response('tipoDeMovimiento.html',{'formulario':formulario}, context_instance=RequestContext(request))

@login_required(login_url='/login')
def list_movimientos(request):
    usuario = Usuario.objects.get(usuario_id=request.user.id)
    cuentas = Cuenta.objects.all()
    movimientos = Movimiento.objects.all()
    return render_to_response("lista_movimientos.html", {'cuentas':cuentas, 'movimientos':movimientos, 'usuario':usuario})

def list_sucursales(request):
    bancos = Banco.objects.all()
    sucursales = Sucursales.objects.all()
    return render_to_response("lista_sucursales.html", {'bancos':bancos, 'sucursales':sucursales})