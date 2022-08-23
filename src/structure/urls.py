
from django.urls import include, path
from structure.views import structure, delete_structure, search, create_structure,edit_structure



urlpatterns = [
    # STRUCTURE 
    path('create/', create_structure, name='create_structure'),
    path('<slug:structure_slug>/', structure, name='detail_structure'),
    # path('ajouter/structureperm/', add_StructurePerm, name='add_StructurePerm'),
    
    path('delete/<int:id>/', delete_structure, name='delete_structure' ),
    path('edit/<int:id>/', edit_structure, name='edit_structure' ),
    path('search/', search, name='search'),


]
