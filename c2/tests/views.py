# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.views.decorators.http import require_POST

from pops.models import POP, Process

from .models import TestRun, TestTask
from .forms import TestRunForm, TestTaskForm


def home(request):
    runs = TestRun.objects.all().order_by('-created')
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


@require_POST
def pickup(request, process_id):
    process = get_object_or_404(Process, id=process_id)
    process.touch()

    task = TestTask.objects.filter(
        status='pending', POP=process.POP,
    ).order_by('created').first()

    if task is None:
        return HttpResponse(status=204)

    task.runner = process
    task.run_start = datetime.datetime.now()
    task.status = 'running'
    task.save()

    return JsonResponse({
        'task_id': task.id,
        'target': task.test_run.target,
    })


@require_POST
def drop_off(request, task_id):
    task = get_object_or_404(TestTask, id=task_id)
    task.runner.touch()

    form = TestTaskForm(request.POST, instance=task)
    if not form.is_valid():
        return JsonResponse({'errors': form.errors}, status=400)

    task = form.save(commit=False)
    task.status = 'finished'
    task.save()

    return HttpResponse(status=200)
