from django import forms
from .models import Girisler

class GirislerForm(forms.Form):

    tarih1 = forms.DateField(label="Başlangıç Tarihi:",required=False,
        widget=forms.DateTimeInput(attrs={'id': 'tarih1'
        })
    )

    tarih2 = forms.DateField(label="Bitiş Tarihi:",required=False,
        widget=forms.DateTimeInput(attrs={'id': 'tarih2'
        })
    )


