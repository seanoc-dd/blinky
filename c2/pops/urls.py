from django.conf.urls import url

from .views import register_process

urlpatterns = [
    url(r'^(?P<zone>[\w-]+)/register', register_process)
]
