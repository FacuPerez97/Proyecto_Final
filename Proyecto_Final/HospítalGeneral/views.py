from django.http.request import QueryDict
from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from HospítalGeneral.templates.HospítalGeneral import *
from django.template import loader


def index(request):
    return render(request, "HospítalGeneral/inicio.html")

def doctor(request):
    return render(request, "HospítalGeneral/Doctor.html")

def paciente(request):
    return render(request, "HospítalGeneral/Paciente.html")

def padre(request):
    return render(request, "HospítalGeneral/padre.html")

