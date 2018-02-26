# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import uuid

from django.db import models

from pops.models import Process, POP

class TestRun(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    target = models.URLField()
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return '{} - {}'.format(self.target, self.created)

    def schedule_tasks(self):
        for pop in POP.objects.all():
            TestTask.objects.create(
                test_run=self,
                POP=pop,
            )


class TestTask(models.Model):
    STATUS_CHOICES = (
        ('pending', 'pending'),
        ('running', 'running'),
        ('finished', 'finished'),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    test_run = models.ForeignKey(TestRun)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    POP = models.ForeignKey(POP)
    runner = models.ForeignKey(Process, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    run_start = models.DateTimeField(null=True)
    result_ms = models.IntegerField(null=True)
    result_status_code = models.IntegerField(null=True)

    def __str__(self):
        return '{} - {}'.format(self.test_run, self.POP)
