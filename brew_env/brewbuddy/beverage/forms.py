from django import forms
from .models import HomebrewBatch, TastingNote

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'


class HomebrewBatchForm(forms.ModelForm):
    
    class Meta:
        model = HomebrewBatch
        fields = ['name', 'start_date','rack_date', 'bottle_date','original_gravity', 'final_gravity' ,'notes' ]
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'start_date' : forms.DateInput(attrs={'type': 'date', 'class': INPUT_CLASSES}),
            'rack_date' : forms.DateInput(attrs={'type': 'date', 'class': INPUT_CLASSES}),
            'bottle_date' : forms.DateInput(attrs={'type': 'date', 'class': INPUT_CLASSES}),
            'original_gravity': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'final_gravity': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'notes' : forms.Textarea(attrs={'class': INPUT_CLASSES})
        }

class EditHomebrewBatchForm(forms.ModelForm):
    class Meta:
        model = HomebrewBatch
        fields = ['name', 'start_date','rack_date', 'bottle_date','original_gravity', 'final_gravity', 'notes' ]
        widgets = {
            'name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'start_date' : forms.DateInput(attrs={'type': 'date', 'class': INPUT_CLASSES}),
            'rack_date' : forms.DateInput(attrs={'type': 'date', 'class': INPUT_CLASSES}),
            'bottle_date' : forms.DateInput(attrs={'type': 'date', 'class': INPUT_CLASSES}),
            'original_gravity': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'final_gravity': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'notes' : forms.Textarea(attrs={'class': INPUT_CLASSES})
        }


class TastingNoteForm(forms.ModelForm):
    class Meta:
        model = TastingNote
        fields =['batch', 'date', 'notes', 'rating']
        widgets = {
            'date' : forms.DateInput(attrs={'type': 'date','class': INPUT_CLASSES}),
            'notes' : forms.Textarea(attrs={'class': INPUT_CLASSES}),
            'rating' : forms.TextInput(attrs={'class': INPUT_CLASSES})
        }