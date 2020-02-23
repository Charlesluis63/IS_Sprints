from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from .models import Juridica
from .models import Ciudad
from .models import Sector
from .models import TipoEmpresa
from ..personas_naturales.models import Persona_Natural
from . import forms
from dal import autocomplete

from django.core.paginator import Paginator


class EmpresaAutocomplete(autocomplete.Select2QuerySetView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def get_queryset(self):
        qs = Juridica.objects.all().order_by("nombre")
        if self.q:
            qs = qs.filter(Q(nombre__icontains=self.q) | Q(ruc__istartswith=self.q))
            #qs = qs.filter(nombre__istartswith=self.q)
        return qs

    def has_add_permission(self, request):
        return True

class TipoAutocomplete(autocomplete.Select2QuerySetView):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	def get_queryset(self):
		qs = TipoEmpresa.objects.all().order_by("nombre")

		if self.q:
			qs = qs.filter(nombre__istartswith=self.q)
		return qs

		
	def has_add_permission(self, request):
		return True
class SectorAutocomplete(autocomplete.Select2QuerySetView):
	def get_queryset(self):
		qs = Sector.objects.all().order_by("nombre")

		if self.q:
			qs = qs.filter(nombre__istartswith=self.q)

		return qs
	def has_add_permission(self, request):
		return True
# Create your views here.
def index_juridicas(request):
	
	juridicas_list = Juridica.objects.all().order_by("pk")

	filter = forms.JuridicaFilter(request.GET, queryset=juridicas_list )
	paginator = Paginator(filter.qs, 30) 

	page = request.GET.get('page')
	juridicas = paginator.get_page(page)
	return render(request, 'personas_juridicas/index.html', {'juridicas': juridicas, "filter":filter})

	
def load_ciudades(request):
	provincia_id = request.GET.get("provincia")
	ciudades = Ciudad.objects.filter(provincia_id=provincia_id).order_by('nombre')
	
	return render(request,"personas_juridicas/dropdown_ciudades.html",{"ciudades":ciudades})

def juridicas_view(request):
	# def post(self, request, *args, **kwargs):
    #     self.object =self.get_object
    #     form=self.form_class(request.POST)
    #     if form.is_valid():
    #         try:
    #             pre = str(int(self.model.objects.latest('pk').pk+1))
    #             sec = '0'*(4-len(pre))+pre
    #         except self.model.DoesNotExist:
    #             sec = '0001'
    #         form.instance.cod_reporte = 'RC-CEC-'+sec+'-'+str(date.today().year)
    #         reporte=form.save()
    #         return HttpResponseRedirect(self.get_success_url()+'/'+str(reporte.pk))
    #     else:
    #         return self.render_to_response(self.get_context_data(form=form))

	#href="{% url 'editar_juridica' pk=j.pk %}"
			
	if(request.method == "POST"):
		form = forms.JuridicaForm(request.POST)
		if(form.is_valid()):
			form.save()
			#return HttpResponseRedirect(get_success_url()+'/'+str(reporte.pk))
			ruc = form.cleaned_data["ruc"]
			print(form.is_valid())
			print(ruc)
			return redirect("editar_juridica",pk = ruc)
		else:
			print(form.errors)
			print("No entre a validar")
	else:	

		form = forms.JuridicaForm()
		print("Soy genial")
	
	return render(request,"personas_juridicas/forma.html", {"form":form})


def juridicas_editar(request,pk):
	n = Persona_Natural.objects.all()
	if(request.method == "POST"):
		p = get_object_or_404(Juridica, pk=pk)
		form = forms.JuridicaForm(request.POST,instance=p)
		if(form.is_valid()):
			form.save()
			return redirect("index_juridicas")
	else:

		p = get_object_or_404(Juridica, pk=pk)
		form = forms.JuridicaForm(instance=p)
		#form.fields["fecha"].value=None
	print(n)
	return render(request, 'personas_juridicas/editar_forma.html', {'form': form,'naturales':n})


def juridicas_eliminar(request,pk=None):
	if(request.method == "POST"):
		p = get_object_or_404(Juridica,pk=pk)
		p.delete()
		return redirect("index_juridicas")
	else:
		pk= request.GET.get('pk')
		if len(pk)<13:
			pk="0"+str(pk)
		p = get_object_or_404(Juridica,pk=pk)
		return render(request, 'personas_juridicas/eliminar.html', {'object': p})