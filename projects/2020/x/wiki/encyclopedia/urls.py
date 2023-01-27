from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('wiki/<str:entry>', views.wiki, name='wiki'),
    path('search/', views.search, name='search'),
    path('new/', views.new, name='new'),
    path('edit/', views.edit, name='edit'),
    path('save/', views.save, name='save'),
    path('random/', views.random, name='random')
]
