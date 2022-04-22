# plates/forms.py

from django import forms#, ModelForm

from .models import NewPlate, PlateContent


class PostForm(forms.ModelForm):
    class Meta:
        model = NewPlate
        fields = ('title', 'world', 'genre', 'character', 'setting')
        labels = {'character': 'State Your Character'}
            #labels = {'character': _('State Your Character')}
            #help_texts = {'due_back': _('Enter a date between now and 4 weeks (default 3).')}



class PostForm2(forms.ModelForm):
    class Meta:
        model = PlateContent
        fields = ('storytext',)
        labels = {'storytext': ''}
        widgets = {'storytext': forms.Textarea(attrs={'cols': 80})}