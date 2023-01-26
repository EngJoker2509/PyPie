from django.urls import path
from . import views


app_name = 'FinalExamApp'

urlpatterns =[
    path('',views.dashboard,name='dashboard'),
    path('edit/<int:id>',views.edit_pypie,name='edit_pypie'),
    path('edit/edit/<int:id>/',views.edit,name='edit'),
    path('pies',views.add_pies,name='add_pies'),
    path('destroy',views.destroy,name='destroy'),
    path('show/<int:id>',views.show,name='show'),
    path('vote/<int:id>',views.vote,name='vote'),
    path('delete/<int:id>',views.delete,name='delete'),
]