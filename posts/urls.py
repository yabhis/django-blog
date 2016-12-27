from django.conf.urls import url

from .views import (
    posts_list,
    posts_update,
    posts_detail,
    posts_create,
    posts_delete
)

urlpatterns = [
    url(r'^$', posts_list),
    url(r'^create/$', posts_create),
    url(r'^detail/$', posts_detail),
    url(r'^update/$', posts_update),
    url(r'^delete/$', posts_delete)
]
