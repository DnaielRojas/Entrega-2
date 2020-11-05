from django import forms
from django.contrib.auth.forms import AuthenticationForm
from appdulceria.models import Usuario, SolicitudDulces

'''class FormularioLogin(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(FormularioLogin, self).__init__(*args,**kwargs)
        self.fields['rut'].widget.attrs['class'] = 'form-control'
        self.fields['rut'].widget.attrs['placeholder'] = 'Rut'
        self.fields['contrasena'].widget.attrs['class'] = 'form-control'
        self.fields['contrasena'].widget.attrs['placeholder'] = 'Contraseña'
        '''

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"

class SolicitudForm(forms.ModelForm):
    class Meta:
        model = SolicitudDulces
        fields = "__all__"
        
class EditarSolicitudForm(forms.ModelForm):
    
    class Meta:
        model = SolicitudDulces
        fields = '__all__'
        exclude = ['id_solicitud']
        
                

class EditarForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre',
                'apellido_paterno',
                'apellido_materno',
                'nick',
                'correo',
                'fecha_nacimiento',
                'contrasena',
                'tipoUsuario']

class ContrasenaForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['contrasena']

class RutForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['rut']