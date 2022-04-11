from django.urls import include, path
from HospítalGeneral import views
from django.template import loader


urlpatterns = [
    path("Index", views.index, name = "Index"),
    path("Paciente", views.paciente, name = "Paciente"),
    path("Doctor", views.doctor, name = "Doctor"),
    path("Padre", views.padre, name = "Padre"),
    #path('doctorFormulario', views.doctorFormulario, name="DoctorFormulario"),
    #path('pacienteFormulario', views.pacienteFormulario, name="PacienteFormulario")
]







