# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import TestRun, TestTask

# Register your models here.
admin.site.register(TestRun)
admin.site.register(TestTask)
