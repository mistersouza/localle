from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

from .models import Item

class AddItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('category', css_class='form-control'),
            Field('name', css_class='form-control'),
            Field('description', css_class='form-control', rows=4),
            Field('price', css_class='form-control'),
            Field('featured_image', css_class='form-control', required=False)
        )

    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'featured_image')


class EditItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('category', css_class='form-control'),
            Field('name', css_class='form-control'),
            Field('description', css_class='form-control', rows=4),
            Field('original_price', css_class='form-control'),
            Field('price', css_class='form-control'),
            Field('featured_image', css_class='form-control', required=False),
            Field('is_sold', css_class='form-control'),
            Field('on_sale', css_class='form-control'),
        )

    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'original_price', 'price', 'featured_image', 'is_sold', 'on_sale',)
