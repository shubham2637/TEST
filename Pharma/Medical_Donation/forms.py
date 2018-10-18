from django import forms
from .models import *

class Collector_form(forms.ModelForm):
    class Meta:
        model = Collector
        fields = "__all__"


class Doner_form(forms.ModelForm):
    class Meta:
        model = Doner
        fields = "__all__"


class Acceptor_form(forms.ModelForm):
    class Meta:
        model = Acceptor
        fields = "__all__"

