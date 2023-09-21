from django import forms
from catalog.models import Product, Version

BANNED_PRODUCTS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'

    def clean_name(self):
        cleaned_data = self.cleaned_data['name'].lower()
        for word in cleaned_data.split():
            if word in BANNED_PRODUCTS:
                raise forms.ValidationError('Запрещенный товар, нельзя добавить')
        return cleaned_data

    def clean_description(self):
        cleaned_data = self.cleaned_data['description'].lower()
        for word in cleaned_data.split():
            if word in BANNED_PRODUCTS:
                raise forms.ValidationError('Запрещенный товар, нельзя добавить')
        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
