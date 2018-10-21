from django.urls import path
from . import views
urlpatterns =[
path("", views.index, name="index"),
path("collector", views.collectors, name= "Collector_view"),
path("donor", views.donors, name= "Donor_view"),
path("add-collector", views.collector_add, name="Add_Collector"),
path("collector_form", views.collector_form_view, name="form_name"),
path("add-donor", views.donor_add, name="add_donor"),
path("create_Collector", views.create_Collector),
path("create_Doner", views.create_Doner)

]
