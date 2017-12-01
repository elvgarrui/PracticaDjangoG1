from principal.models import *
from django.shortcuts import render_to_response, get_list_or_404
from django.contrib.auth import authenticate
from principal.forms import *
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext

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
