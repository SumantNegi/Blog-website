from django.forms import ModelForm
from froala_editor.widgets import FroalaEditor
from .models import*

class blogform(ModelForm):
    class Meta:
        model = post
        fields=['detail','image']