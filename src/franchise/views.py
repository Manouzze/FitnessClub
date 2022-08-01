from django.shortcuts import render
from franchise.models import Franchise

# Create your views here.
def list_franchise(request):
    clients = Franchise.objects.filter(is_active=True)
    return render(request, 'list_franchise.html', context={'clients': clients,})