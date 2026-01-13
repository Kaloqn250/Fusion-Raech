from django import forms

from companies.models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder':  'Company name',
            }),
            'logo': forms.FileInput(attrs={
                'placeholder': "Company's logo",
            }),
            'type': forms.TextInput(attrs={
                'placeholder': "Company's type",
            }),
            'about_company': forms.TextInput(attrs={
                'placeholder': 'Write description for the company'
            }),
            'work_space': forms.TextInput(attrs={
                'placeholder': 'Write your work space advantages',
            }),
            'website': forms.TextInput(attrs={
                'placeholder': 'If the company has a website, you can place the url here',
            }),
        }
