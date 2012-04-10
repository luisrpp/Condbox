# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from forms import CondoSearchForm
from models import Condominio


@login_required
def profile(request):
    context = RequestContext(request)
    return render_to_response('registration/profile.html', context)


@login_required
def search_condo(request):
    form = CondoSearchForm(auto_id=True)

    context = RequestContext(request)
    return render_to_response('core/search_condo.html',
                            {'form': form},
                             context)


@login_required
def ajax_condo_search(request):
    if request.is_ajax():
        query = (Q(nome__icontains=request.GET.get('condo')))
        query = query & (Q(cidade__uf__icontains=request.GET.get('uf')))
        query = query & (Q(cidade__nome__icontains=request.GET.get('cidade')))

        results = Condominio.objects.filter(query).distinct().order_by('nome')

        template = 'core/condo_results.html'
        data = {
            'results': results,
        }
        context = RequestContext(request)

        return render_to_response(template, data, context)


@login_required
def condo(request, slug):
    condominio = get_object_or_404(Condominio, slug=slug)

    template = 'core/condo.html'
    data = {
        'condominio': condominio,
    }
    context = RequestContext(request)

    return render_to_response(template, data, context)
