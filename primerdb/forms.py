from django import forms
from primerdb.models import Primer


class PrimerForm(forms.ModelForm):

    class Meta:
        model = Primer
        fields = '__all__'
