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
    return render_to_response('tfg.html',{'formulario':formulario}, context_instance=RequestContext(request))
