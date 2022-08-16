
from django.urls import include, path
from structure.views import structure, delete_structure, update_permission, search, create_structure



urlpatterns = [
    # STRUCTURE 
    path('<slug:structure_slug>/', structure, name='detail_structure'),
    path('create/', create_structure, name='create_structure'),
    # path('ajouter/structureperm/', add_StructurePerm, name='add_StructurePerm'),
    path('update/<int:id>', update_permission, name='update_permission' ),
    path('delete/<int:id>', delete_structure, name='delete_structure' ),
    path('search/', search, name='search'),


]
