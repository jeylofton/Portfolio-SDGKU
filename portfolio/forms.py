from crispy_bootstrap5.bootstrap5 import FloatingField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Field, Layout, Submit
from django import forms

from .models import Project


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'contact-form__input',
            'placeholder': 'Your name',
            'autocomplete': 'name',
        }),
    )
    email = forms.EmailField(
        max_length=254,
        widget=forms.EmailInput(attrs={
            'class': 'contact-form__input',
            'placeholder': 'you@example.com',
            'autocomplete': 'email',
        }),
    )
    subject = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'contact-form__input',
            'placeholder': 'Subject',
        }),
    )
    message = forms.CharField(
        max_length=5000,
        widget=forms.Textarea(attrs={
            'class': 'contact-form__input contact-form__textarea',
            'placeholder': 'Write your message...',
            'rows': 6,
        }),
    )
    # Honeypot: real users leave this blank; bots typically fill every field.
    website = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'tabindex': '-1',
            'autocomplete': 'off',
            'aria-hidden': 'true',
            'style': 'position:absolute;left:-10000px;top:auto;width:1px;height:1px;overflow:hidden;',
        }),
    )

    def clean_website(self):
        if self.cleaned_data.get('website'):
            raise forms.ValidationError('Spam detected.')
        return ''

    def _no_header_injection(self, value):
        if any(ch in value for ch in ('\r', '\n')):
            raise forms.ValidationError('Invalid characters detected.')
        return value

    def clean_name(self):
        return self._no_header_injection(self.cleaned_data['name'].strip())

    def clean_subject(self):
        return self._no_header_injection(self.cleaned_data['subject'].strip())


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'image', 'github_url', 'live_url', 'skills', 'featured']
        widgets = {
            'skills': forms.CheckboxSelectMultiple(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.attrs = {'enctype': 'multipart/form-data', 'novalidate': ''}
        self.helper.layout = Layout(
            FloatingField('title'),
            Field('description', rows=5),
            'image',
            FloatingField('github_url'),
            FloatingField('live_url'),
            'skills',
            'featured',
            Submit('submit', 'Save Project', css_class='btn btn-success'),
        )
