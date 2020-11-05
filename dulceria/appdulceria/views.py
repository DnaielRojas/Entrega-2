from django.shortcuts import render, redirect
from appdulceria.forms import UsuarioForm, EditarForm, ContrasenaForm, SolicitudForm, EditarSolicitudForm
from appdulceria.models import Usuario, SolicitudDulces
from appdulceria.filters import UsuarioFiltro, SolicitudFiltro

def usuario(request):
    if request.method == "POST":
        usuario_f = Usuario(rut = request.POST['rut'],
                            nombre = request.POST['nombre'],
                            apellido_paterno = request.POST['apellidoP'],
                            apellido_materno = request.POST['apellidoM'],
                            nick = request.POST['nick'],
                            correo = request.POST['correo'],
                            fecha_nacimiento = request.POST['fecha'],
                            contrasena = request.POST['contrasena']
                            )
        usuario_f.save()
        return redirect('/login')
    return render(request,'registro.html')

def solicitud_r(request):
    if request.method == "POST":
        solicitud_f = SolicitudDulces(
                            nombre = request.POST['nombre'],
                            apellido_paterno = request.POST['apellidoP'],
                            rut = request.POST['rut'],
                            correo = request.POST['correo'],
                            descripcion = request.POST['desc'],
                            dulce_dia = request.POST.get('dulce', False),
                            direccion = request.POST['direccion'],
                            entrega_inmediata = request.POST.get('entrega', False),
                            factura = request.POST.get('factura', False)
                            )

        if solicitud_f.dulce_dia == 'on':
            solicitud_f.dulce_dia = True
        else:
            solicitud_f.dulce_dia = False
        
        if solicitud_f.entrega_inmediata == 'on':
            solicitud_f.entrega_inmediata = True
        else:
            solicitud_f.entrega_inmediata = False
        
        if solicitud_f.factura == 'on':
            solicitud_f.factura = True
        else:
            solicitud_f.factura = False
        solicitud_f.save()
        return redirect('/')
    return render(request,'solicitud.html')

def editar_solicitud(request,id_solicitud):
    sol = SolicitudDulces.objects.get(id_solicitud=id_solicitud)
    form = SolicitudForm(instance=sol)
    return render(request,'modificar_solicitud.html',{'form':form,'id_solicitud':sol.id_solicitud})

def editar(request,rut):
    cli = Usuario.objects.get(rut=rut)
    form = UsuarioForm(instance=cli)
    return render(request,'modificar_usuario.html',{'form':form,'rut':cli.rut})

def modificar(request,rut):
    cli = Usuario.objects.get(rut=rut)
    if request.method == "POST":
        form = EditarForm(request.POST, instance=cli)
        if form.is_valid():
            try:
                form.save()
                redirect('/clientes')
            except:
                pass
    l_clientes = Usuario.objects.all()
    form = UsuarioForm()
    cli_filtro = UsuarioFiltro(request.GET, queryset=l_clientes)
    l_clientes = cli_filtro.qs
    return render(request,'gestion_usuarios.html',{'form':form, 'clientes':l_clientes,'cli_filtro':cli_filtro})

def modificar_solicitud(request,id_solicitud):
    sol = SolicitudDulces.objects.get(id_solicitud=id_solicitud)
    if request.method == "POST":
        form = EditarSolicitudForm(request.POST, instance=sol)
        if form.is_valid():
            try:
                form.save()
                redirect('/lista_solicitudes')
            except:
                pass
    l_solicitudes = SolicitudDulces.objects.all()
    form = SolicitudForm()
    sol_filtro = SolicitudFiltro(request.GET, queryset=l_solicitudes)
    l_solicitudes = sol_filtro.qs
    return render(request,'gestion_dulces.html',{'form':form, 'solicitudes':l_solicitudes,'sol_filtro':sol_filtro})

def eliminar(request, rut):
    cli = Usuario.objects.get(rut=rut)
    cli.delete()
    l_clientes = Usuario.objects.all()
    form = UsuarioForm()
    cli_filtro = UsuarioFiltro(request.GET, queryset=l_clientes)
    l_clientes = cli_filtro.qs
    return render(request,'gestion_usuarios.html',{'form':form,'clientes':l_clientes,'cli_filtro':cli_filtro})

def eliminar_solcitud(request, id_solicitud):
    sol = SolicitudDulces.objects.get(id_solicitud=id_solicitud)
    sol.delete()
    l_solicitudes = SolicitudDulces.objects.all()
    form = SolicitudForm()
    sol_filtro = SolicitudFiltro(request.GET, queryset=l_solicitudes)
    l_solicitudes = sol_filtro.qs
    return render(request,'gestion_dulces.html',{'form':form,'solicitudes':l_solicitudes,'sol_filtro':sol_filtro})

def editar_pass(request):
    cli_pass = Usuario(rut = request.POST['rut'])
    cli = Usuario.objects.get(rut=cli_pass.rut)
    form = ContrasenaForm(instance=cli)
    return render(request,'cambiar_pass.html',{'form':form,'cli':cli})

def modificar_pass(request,rut):
    cli = Usuario.objects.get(rut=rut)
    if request.method == "POST":
        form = ContrasenaForm(request.POST, instance=cli)
        if form.is_valid():
            try:
                form.save()
                redirect('/login')
            except:
                pass
    return render(request,'login.html')

def clientes(request):
    form = UsuarioForm()
    l_clientes = Usuario.objects.all()

    cli_filtro = UsuarioFiltro(request.GET, queryset=l_clientes)
    l_clientes = cli_filtro.qs
    return render(request,'gestion_usuarios.html',{'form':form,'clientes':l_clientes,'cli_filtro':cli_filtro})

def lista_solicitudes(request):
    form = SolicitudForm()
    l_solicitudes = SolicitudDulces.objects.all()

    sol_filtro = SolicitudFiltro(request.GET, queryset=l_solicitudes)
    l_solicitudes = sol_filtro.qs
    return render(request,'gestion_dulces.html',{'form':form,'solicitudes':l_solicitudes,'sol_filtro':sol_filtro})