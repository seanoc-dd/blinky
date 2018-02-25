# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import datetime
import uuid

from django.db import models


class POP(models.Model):
    id = models.CharField(primary_key=True, max_length=255)
    created = created = models.DateTimeField(auto_now_add=True, editable=False)
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.id


class Process(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    POP = models.ForeignKey(POP, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_seen = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return str(self.id)
