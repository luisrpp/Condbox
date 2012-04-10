# -*- coding: utf-8 -*-
from datetime import datetime

from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext as _
from django.contrib.auth.models import User

from municipios.models import Cidade

"""
Model classes do Django App Core.
"""


class Condominio(models.Model):
    """Classe que representa condomínio."""
    nome = models.CharField(max_length=200, verbose_name=_(u'Nome do condomínio'))
    endereco = models.CharField(max_length=200, verbose_name=_(u'Endereço'))
    numero = models.CharField(max_length=6, verbose_name=_(u'Número'))
    complemento = models.CharField(max_length=100, verbose_name=_(u'Complemento'), null=True, blank=True)
    bairro = models.CharField(max_length=100, verbose_name=_(u'Bairro'))
    cep = models.CharField(max_length=9, verbose_name=_(u'CEP'))
    cidade = models.ForeignKey(Cidade)
    data_criacao = models.DateTimeField(verbose_name=_(u'Data de criação'), default=datetime.now)
    slug = models.SlugField(max_length=100, blank=True, unique=True)

    class Meta:
        ordering = ['nome']
        verbose_name = _(u'Condomínio')
        verbose_name_plural = _(u'Condomínios')

    def __unicode__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('core:condo', kwargs={'slug': self.slug})


class Morador(models.Model):
    """Classe que representa um morador."""
    user = models.ForeignKey(User, verbose_name=_(u'Usuário'))
    condominio = models.ForeignKey(Condominio, verbose_name=_(u'Condomínio'))
    data_inicio = models.DateField(verbose_name=_(u'Data de entrada no condomínio'))
    data_fim = models.DateField(verbose_name=_(u'Data de saída do condomínio'), null=True, blank=True)

    class Meta:
        ordering = ['condominio', 'user']
        unique_together = ('user', 'condominio', 'data_inicio')
        verbose_name = _(u'Morador')
        verbose_name_plural = _(u'Moradores')

    def __unicode__(self):
        return self.user.username


# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify


def condominio_pre_save(signal, instance, sender, **kwargs):
    if not instance.slug:
        slug = slugify(instance.nome)
        new_slug = slug
        count = 0

        while Condominio.objects.filter(slug=new_slug).exclude(id=instance.id).count() > 0:
            count += 1
            new_slug = '%s-%d' % (slug, count)

        instance.slug = new_slug

signals.pre_save.connect(condominio_pre_save, sender=Condominio)
