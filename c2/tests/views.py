# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from pops.models import POP

from .models import TestRun
from .forms import TestRunForm


def home(request):
    runs = TestRun.objects.all().order_by('-created')[:10]
    pops = POP.objects.all()

    if request.method == 'POST':
        form = TestRunForm(request.POST)
        if form.is_valid():
            test_run = form.save()
            test_run.schedule_tasks()
    else:
        form = TestRunForm()

    return render(request, 'home.html', context={
        'runs': runs,
        'pops': pops,
        'form': form,
    })
