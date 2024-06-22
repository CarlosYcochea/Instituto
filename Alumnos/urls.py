from django.urls import path
from .views import index , crud, alumnosAdd, alumnos_del, alumnos_findEdit, alumnosUpdate, crud_generos, generosAdd


urlpatterns = [
    path('index', index, name='index'),

    path('crud', crud, name='crud'),
    path('alumnosAdd', alumnosAdd, name='alumnosAdd'),
    path('alumnos_del/<str:pk>', alumnos_del, name='alumnos_del'),
    path('alumnos_findEdit/<str:pk>', alumnos_findEdit, name='alumnos_findEdit'),
    path('alumnosUpdate', alumnosUpdate, name='alumnosUpdate')

    path('crud_generos', crud_generos, name='crud_generos')
    path('generosAdd', generosAdd, name='generosAdd')
    path('')
]