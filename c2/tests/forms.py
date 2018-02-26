from django.forms import ModelForm

from .models import TestRun


class TestRunForm(ModelForm):
    class Meta:
        model = TestRun
        fields = ['target']
