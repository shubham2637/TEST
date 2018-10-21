from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from .models import Collector, Doner
from . import forms


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
    if request.method == POST:
        form = forms.Collector_form(request.POST)
    context={
    "form" : form
    }

    return render(request, "Medical_Donation/collector_form.html", context)

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


def create_Collector(request):
    if request.POST:
            coll = Collector(name=request.POST['name'], address= (request.POST['address1']+ request.POST['address2'] + request.POST['address3']), pinCode=request.POST['pincode'], Phone_no=request.POST['phone_no'],BirthDate=request.POST['birth'], UID=request.POST['uid'], email=request.POST['email'],username=request.POST['username'], password=request.POST['password'], image=request.POST['image'] )
            coll.save()
    return HttpResponseRedirect(reverse("Add_Collector"))


def create_Doner(request):
    if request.POST:
            don = Doner(name=request.POST['name'], address= (request.POST['address1']+ request.POST['address2'] + request.POST['address3']), pinCode=request.POST['pincode'], Phone_no=request.POST['phone_no'],BirthDate=request.POST['birth'], UID=request.POST['uid'], email=request.POST['email'],username=request.POST['username'], password=request.POST['password'], image=request.POST['image'] )
            don.save()
    return HttpResponseRedirect(reverse("add_donor"))


def collector_form_view(request):
    if request.method == "POST":
        form = forms.Collector_form(request.POST)
        if form.is_valid():
                item = form.save(commit=False)
                item.save()
    else:
        form = forms.Collector_form()

    context={
    "form" : form
    }
    return render(request, "Medical_Donation/collector_form.html", context)
