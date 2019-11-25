from django.contrib import admin
from ckeditor.widgets import CKEditorWidget
from django import forms

from .models import TextSection
from tours.models import TourSection,Tour
# Register your models here.

class TextSectionAdminForm(forms.ModelForm):
    text = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = TourSection
        fields = '__all__'




