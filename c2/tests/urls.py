from django.conf.urls import url

from .views import pickup, drop_off

urlpatterns = [
    url(r'^client/(?P<process_id>[\w-]+)/pickup', pickup),
    url(r'^task/(?P<task_id>[\w-]+)/drop-off', drop_off)
]
