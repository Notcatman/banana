from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'completed']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-input form-input--title',
                'placeholder': 'Enter title',
                'maxlength': '50',
                'minlength': '3'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-input form-input--desc',
                'rows': 3,
                'placeholder': 'Enter details',
                'maxlength': '300'
            }),
            'completed': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }
