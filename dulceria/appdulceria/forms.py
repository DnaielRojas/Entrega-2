from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from appdulceria.models import Usuario, SolicitudDulces

class CrearForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '12345678-9'}))
    password1 = forms.CharField(strip=False,widget=forms.PasswordInput(attrs={'placeholder': '********'}))
    password2 = forms.CharField(strip=False,widget=forms.PasswordInput(attrs={'placeholder': '********'}))
    def __init__(self, *args, **kwargs):
        super(CrearForm, self).__init__(*args, **kwargs)
        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

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
                'tipoUsuario']

class RutForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['rut']