from django.shortcuts import render, HttpResponse
from structure.models import Structure
from franchise.models import Franchise
from account.models import User
from django.contrib import auth, messages
from django.db.models import Q # permet de faire une recherche sur plusieurs champs
from django.http import JsonResponse

# Create your views here.

def dashboard(request):
    search_structure = Structure.objects.all()
    
    structures = Structure.objects.count()
    franchises = Franchise.objects.count()
    user = User.objects.filter(is_staff=False, is_admin=False)
    users = user.count()
    return render(request, 'dashboard.html', context={'search_structure':search_structure, 'structures':structures, 'franchises':franchises, 'users':users,})



# --------------* SEARCH BAR *--------------#
def search(request):
    search = request.GET.get('search')
    results_structure = Structure.objects.filter(Q(name__icontains=search) |
                                        Q(address__icontains=search))
    results_franchise = Franchise.objects.filter(name__icontains=search)
    return render(request, 'search.html', context={'results_structure': results_structure, 'results_franchise':results_franchise})




# # --------------* SEARCH BAR *--------------#
# def search_results(request):
#     is_ajax = request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'
#     if request.is_ajax:
#         structure = request.POST.get('structure')
#         print(structure)
#         qs = Structure.objects.filter(name__icontains=structure)
#         if len(qs) > 0 and len(structure) > 0:
#             data = []
#             for pos in qs:
#                 item = {
#                     'pk':pos.pk,
#                     'name':pos.name
#                 }
#                 data.append(item)
#             res = data
#         else:
#             res= 'No structure found ..'
#         return JsonResponse({'data': res})
#     return JsonResponse({})


