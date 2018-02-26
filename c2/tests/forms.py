from django.forms import ModelForm

from .models import TestRun, TestTask


class TestRunForm(ModelForm):
    class Meta:
        model = TestRun
        fields = ['target']


class TestTaskForm(ModelForm):
    class Meta:
        model = TestTask
        fields = ['result_ms', 'result_status_code']
