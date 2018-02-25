# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import POP, Process


admin.site.register(POP)
admin.site.register(Process)
