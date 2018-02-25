# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_http_methods

from .models import POP, Process


@require_http_methods('POST')
def register_process(request, zone):
    process_pop = get_object_or_404(POP, id=zone)
    process = Process.objects.create(POP=process_pop)

    return JsonResponse({'id': process.id})
