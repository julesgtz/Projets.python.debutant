from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from . import models
from django import forms


class urlForms(ModelForm):
    class Meta:
        model = models.url
        fields = ('long_url',)
        labels = {
            'long_url': _('Votre URL'),
        }