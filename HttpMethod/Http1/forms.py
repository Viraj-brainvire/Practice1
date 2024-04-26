from django import forms
from .models import data

class DataForm(forms.ModelForm):
    class Meta:
        model = data
        fields = ('personid','lastname','firstname','address','city')
        labels = {
            
        }

    def __init__(self,*callback_args,** callback_kwargs):
        super(DataForm,self).__init__(*callback_args,** callback_kwargs)
        # self.fields['Position'].empty_label = 'Select'
        self.fields['personid'].empty_label = False
        self.fields['address'].empty_label = False