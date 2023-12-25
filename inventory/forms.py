from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field

from .models import Item


class AddItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('category', css_class='form-control border border-dark'),
            Field('name', css_class='form-control border border-dark'),
            Field('description', css_class='form-control border border-dark', rows=3),
            Field('price', css_class='form-control border border-dark'),
            Field('featured_image', css_class='form-control border border-dark', required=False)
        )

    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'featured_image')


class EditItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('category', css_class='form-control border border-dark'),
            Field('name', css_class='form-control border border-dark'),
            Field('description', css_class='form-control', rows=3),
            Field('original_price', css_class='form-control border border-dark'),
            Field('price', css_class='form-control border border-dark'),
            Field('featured_image', css_class='form-control border border-dark', required=False),
            Field('is_sold', css_class='form-control border border-dark'),
            Field('on_sale', css_class='form-control border border-dark'),
        )

    class Meta:
        model = Item
        fields = (
            'category',
            'name',
            'description',
            'original_price',
            'price',
            'featured_image',
            'is_sold',
            'on_sale',
            )
