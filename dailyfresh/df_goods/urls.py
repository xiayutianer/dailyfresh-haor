from django.conf.urls import url
from . import views
from df_goods.views import *

urlpatterns=[
    url('^$',views.index),
    url('^list(\d+)_(\d+)_(\d+)/$', views.list),
    url('^(\d+)/$', views.detail),
    url(r'^search/', MySearchView()),

]
