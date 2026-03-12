from django import forms
from shop.models import Order

class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['address', 'contact_no','quantity','payment_method']

    def clean_contact_no(self):
        contact_no = self.cleaned_data.get('contact_no')
        if len(contact_no) != 10:
            raise forms.ValidationError('Contact number must be 10 digits.')
        return contact_no