from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^wall$', views.wall_index),
    url(r'^logout$', views.logout),
    url(r'^create_post$', views.create_post),
    url(r'^add_comment/(?P<post_id>\d+)$', views.add_comment),
    url(r'^delete_comment/(?P<comment_id>\d+)$', views.delete_comment),
    url(r'^delete_post$', views.delete_post),
]
