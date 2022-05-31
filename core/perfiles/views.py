from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DetailView, CreateView,DeleteView
from core.main.forms import SkillsWorked, postRegistro
from core.main.models import Users
from .models import *
from .forms import *

from django.contrib import messages

# Create your views here.
def pefil(request, id):
    trabajador=Users.objects.get(pk=id)
    categorias=Skills.objects.all()
    habilidades=WorkedSkills.objects.filter(trabajador=id).select_related('trabajador').select_related('especialidad').all()
    evidencias=Evidencias.objects.filter(trabajador=id).all()
    form=ComentForm(request.POST, request.FILES)
    titulo=f"Perfil {trabajador.first_name}"
    return render(request, 'users/perfilWorked.html',{
        'title':titulo,
        'especialidades':categorias,
        'trabajador':trabajador,
        'habilidades':habilidades,
        'evidencias':evidencias,
        'comentForm':form
    })

class Pefillll(CreateView, DetailView):
    model_user=Users
    model_evidencias=Evidencias
    model_trabajador=Users
    model_habilidades=WorkedSkills
    model_categorias=Skills
    template_name='users/perfilWorked.html'
    form_coment=ComentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk=self.kwargs.get('pk',0)
        persona=self.model.objects.get(id=pk)

        if 'comentForm' not in context:
            context['form']=self.form_coment()
        if 'especialidades' not in context:
            context['especialidades']=Skills.objects.all()
        if 'evidencias' not in context:
            context['evidencias']=self.model_evidencias.objects.filter(trabajador=pk)
        context['title']='Galeria'
        context['id']=pk
        
        return context
    
    def post(self,request, *args, **kwargs):
        self.object=self.get_object
        id_persona=kwargs['pk']
        persona=self.model.objects.get(id=id_persona)
        if request.method=='POST':
            form=self.form_class(request.POST,request.FILES)
            if(form.is_valid()):
                data=form.cleaned_data
                descripcion=data['descripcion']
                evidenciaPhoto=data['evidenciaPhoto']
                evidence=Evidencias(
                    descripcion=descripcion,
                    evidenciaPhoto=evidenciaPhoto,
                    trabajador=persona
                )
                evidence.save() 
                
                messages.warning(request, 'Evidencia agregada correctamente')

                return redirect('galeriaPropia', pk=request.user.id)

        else:
            messages.warning(request, 'Hay algun error en el formulario')
            return redirect('galeriaPropia', pk=request.user.id)


def index(request):
    categorias=Skills.objects.all()
    return render(request, 'index/index.html',{
        'titulo':'Inicio',
        'especialidades':categorias
    })

class updateUser(CreateView, DetailView):
    model=Users
    model_skills=WorkedSkills
    template_name='users/perfilPropio.html'
    form_class=postRegistro
    form_esp=SkillsWorked

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk=self.kwargs.get('pk',0)
        persona=self.model.objects.get(id=pk)
        if 'form' not in context:
            context['form']=self.form_class(instance=persona)
        if 'form2' not in context:
            context['form2']=self.form_esp()
        if 'especialidad' not in context:
            context['especialidad']=self.model_skills.objects.filter(trabajador=pk)
        if 'especialidades' not in context:
            context['especialidades']=Skills.objects.all()
        context['title']='Perfil'
        context['id']=pk
        
        return context

    def post(self,request, *args, **kwargs):
        self.object=self.get_object
        id_persona=kwargs['pk']
        persona=self.model.objects.get(id=id_persona)
        if request.method=='POST':
            form=self.form_class(request.POST,request.FILES, instance=persona)
            form2=self.form_esp(request.POST)
            if(form.is_valid()):
                form.save() 
                messages.warning(request, 'datos actualizados')
                if form2.is_valid():
                    data=form2.cleaned_data
                    especiality=data['especialidad']

                for esp in especiality:
                    existe=WorkedSkills.objects.filter(trabajador=persona, especialidad=int(esp)).exists()
                    if not existe:
                        skill=WorkedSkills(
                            trabajador=persona,
                            especialidad=Skills.objects.get(id=int(esp))
                        )
                        skill.save()

                return redirect('perfilUpdate', pk=request.user.id)

        else:
            messages.warning(request, 'Hay algun error en el formulario')
            return redirect('perfilUpdate', pk=request.user.id)

class evidenciasTrabajadores(UpdateView, DetailView):
    model=Users
    model_evidencias=Evidencias
    template_name='users/evidencias.html'
    form_class=evidencias

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk=self.kwargs.get('pk',0)
        persona=self.model.objects.get(id=pk)
        if 'form' not in context:
            context['form']=self.form_class()
        if 'form2' not in context:
            context['form2']=self.form_class()
        if 'especialidades' not in context:
            context['especialidades']=Skills.objects.all()
        if 'evidencias' not in context:
            context['evidencias']=self.model_evidencias.objects.filter(trabajador=pk)
        context['title']='Galeria'
        context['id']=pk
        
        return context
    
    def post(self,request, *args, **kwargs):
        self.object=self.get_object
        id_persona=kwargs['pk']
        persona=self.model.objects.get(id=id_persona)
        if request.method=='POST':
            form=self.form_class(request.POST,request.FILES)
            if(form.is_valid()):
                data=form.cleaned_data
                descripcion=data['descripcion']
                evidenciaPhoto=data['evidenciaPhoto']
                evidence=Evidencias(
                    descripcion=descripcion,
                    evidenciaPhoto=evidenciaPhoto,
                    trabajador=persona
                )
                evidence.save() 
                
                messages.warning(request, 'Evidencia agregada correctamente')

                return redirect('galeriaPropia', pk=request.user.id)

        else:
            messages.warning(request, 'Hay algun error en el formulario')
            return redirect('galeriaPropia', pk=request.user.id)

def borrarEvidencia(request, id):
    try:
        evidencia=Evidencias.objects.get(pk=id)
        evidencia.delete()
        messages.warning(request, 'Evidencia eliminada con exito')
        return redirect('galeriaPropia', pk=request.user.id)
    except:
        return redirect('error')

def editarEvidencia(request, id):
    evidencia=Evidencias.objects.get(pk=id)
    formulario=evidencias(request.POST, request.FILES, instance=evidencia)
    if request.method=='POST':
        if formulario.is_valid():
            formulario.save()
    messages.warning(request, 'Evidencia actualizada con exito')
    return redirect('galeriaPropia', pk=request.user.id)

def error(request):
    return render(request,'index/error.html',{
        'title':'error',
    })

def categorias(request, id):
    categorias=Skills.objects.all()
    trabajadores=WorkedSkills.objects.filter(especialidad=id).select_related('trabajador__ciudad').all()
    titulo=categorias.get(pk=id)
    titulo=titulo.especialidad
    return render(request, 'users/categorias.html', {
        'titulo':titulo,
        'trabajadores':trabajadores,
        'especialidades':categorias

    })