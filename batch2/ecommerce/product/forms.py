from django import forms
from product.models import Product
"""
Two type of forms are there in django:
1. Form => we must define every custom field
2. ModelForm => django automatically define the forms on the basis of model
"""

"""Form"""
"""
There are two type of validation.
1. Field level validation => individual field laii valid garne e.g: email validation, password validation
2. Object level validation => two or more field ko bich maa validation lagaue e.g:
3. using Validators
"""
class LoginForm(forms.Form):
    email = forms.EmailField(label='User-Email', required=True)
    password = forms.CharField(max_length=30,widget=forms.PasswordInput(), label='User-Password')
    is_admin = forms.BooleanField()

    def clean_password(self):
        password = self.cleaned_data['password']
        if len(password) < 8:
            raise forms.ValidationError("Password must be greater than 8 characters.")
        return password

class ProductForm(forms.ModelForm):
    """Product Form for creating the product."""
    # total_price = forms.CharField(max_length=10)
    class Meta:
        model = Product
        # fields = ['product_name','product_price','product_description','product_image','in_stock','category']
        fields = "__all__"
        # exclude = ['category']

    def clean_product_name(self): # clean_<field_name>
        product_name = self.cleaned_data['product_name']
        if len(product_name)< 3:
            raise forms.ValidationError("Product name must be greater than 3 characters.")
        # productname = "laptop"
        if Product.objects.filter(product_name=product_name).exists():
            raise forms.ValidationError("Product with this name already exists.")
        return product_name


    def clean(self):
        product_name = self.cleaned_data.get('product_name')
        product_description = self.cleaned_data.get('product_description')
        if product_name == product_description:
            raise forms.ValidationError("Product name and description cannot be same.")
        return  super().clean()


class EditProductForm(forms.ModelForm):
    """Form to update the product."""
    class Meta:
        model = Product
        exclude = ['category']