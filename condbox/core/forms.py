# -*- coding: utf-8 -*-
from django import forms
from django.utils.translation import ugettext as _
from django.contrib.localflavor.br.br_states import STATE_CHOICES


class CondoSearchForm(forms.Form):
    """ Form para busca de condomínios. """
    condo = forms.CharField(label=_(u"Condomínio"),
                            widget=forms.TextInput(attrs={'class': 'span2'}))
    uf = forms.ChoiceField(label=_(u"Estado"), choices=STATE_CHOICES)
    cidade = forms.CharField(label=_(u"Cidade"),
                            widget=forms.TextInput(attrs={'class': 'span2'}))
