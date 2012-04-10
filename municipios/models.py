# -*- coding: utf-8 -*-
from django.utils.translation import ugettext as _
from django.db import models

"""
Model classes do Django App Municipios.
"""


class Cidade(models.Model):
    """Classe que representa os municípios brasileiros."""
    nome = models.CharField(verbose_name=_(u'Cidade'), max_length=100)
    uf = models.CharField(verbose_name=_(u'UF'), max_length=2)
    is_capital = models.BooleanField(verbose_name=_(u'Capital'), default=False)

    class Meta:
        verbose_name = _(u'Cidade')
        verbose_name_plural = _(u'Cidades')

    def __unicode__(self):
        return self.nome
