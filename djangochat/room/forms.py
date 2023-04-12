from django.forms import ModelForm
from django import forms
from .models import Room
from django.utils.translation import gettext_lazy as _

class RoomCreateForm(ModelForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       self.fields["name"].widget.attrs.update({"class": "w-full mt-2 px-4 py-2 rounded-xl", "placeholder": "new room"})
    class Meta:
        model = Room
        fields = ['name',]
        labels = {
            "name": _(""),
        }