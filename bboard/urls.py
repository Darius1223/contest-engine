from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('all/', BbListView.as_view(), name='bbs_list')
]
