from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from .models import Collector, Doner
from .forms import *


def index(request):
    context= {

    }
    return render(request,"Medical_Donation/index.html",context)

def collectors(request):
    context = {
    "collectors": Collector.objects.all()
    }

    return render(request, "Medical_Donation/collector.html",context)

def donors(request):
    context = {
    "donors": Doner.objects.all()
    }

    return render(request, "Medical_Donation/donor.html",context)


def form_Collector(request):
    form = forms.Collector_form()
    if request.method:
        form = forms.Collector_form(request.POST)
    context={
    "form" : form
    }

    return render(request, "Medical_Donation/collector_form.html")

def collector_add(request):
    context = {
    "collectors": Collector.objects.all()
    }

    return render(request, "Medical_Donation/add-collector.html",context)



def donor_add(request):
    context = {
    "donors": Doner.objects.all()
        }

    return render(request, "Medical_Donation/add-donor.html",context)


def create(request):
    if request.POST:
        if request.POST['pincode']:
            pin = request.POST['pincode']
        else:
            pin = False
        coll = Collector(name=request.POST['name'], address=(request.POST['address1']+ request.POST['address2'] + request.POST['address3']), pinCode=pin, Phone_no=request.POST['phone_no'],
                BirthDate=request.POST['birthdate'], UID=request.POST['uid'], email=request.POST['email'],username=request.POST['username'], password=request.POST['password'], image=request.POST['image'] )
        coll.save()
    return HttpResponseRedirect(reverse("Add_Collector"))
