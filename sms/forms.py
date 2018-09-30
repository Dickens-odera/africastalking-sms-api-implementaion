from django import forms
from sms.models import Recipients

class RecipientsForm(forms.ModelForm):
    class Meta:
        model = Recipients
        fields = '__all__'