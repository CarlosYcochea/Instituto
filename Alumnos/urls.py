from django.urls import path
from .views import index , crud, alumnosAdd, alumnos_del, alumnos_finEdit, alumnosUpdate


urlpatterns = [
    path('index', index, name='index'),

    path('crud', crud, name='crud'),
    path('alumnosAdd', alumnosAdd, name='alumnosAdd'),
    path('alumnos_del/<str:pk>', alumnos_del, name='alumnos_del'),
    path('alumnos_finEdit/<str:pk>', alumnos_finEdit, name='alumnos_finEdit'),
    path('alumnosUpdate', alumnosUpdate, name='alumnosUpdate')
]