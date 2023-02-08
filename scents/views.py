from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponse
from .models import Product, Category
# from .models import MenScent, WomenScent



# Create your views here.

def scents(request):
    pro = Product.objects.all()
    
    name = None
    if 'search_name' in request.GET:
        name = request.GET['search_name']
        
        if name:
            pro = pro.filter(name__icontains=name)
            
    context = {
        'products': pro,            
    }
    return render(request, 'scents/scents.html',context)

def scent(request, pro_id):
    
    context = {
        'pro':get_object_or_404(Product, pk=pro_id)
    }
    return render(request, 'scents/scent.html',context)

def ScentType(request, category_id):
    
    ScentType = Product.objects.all().filter(category = category_id)
    
    context = {
        'scenttype': ScentType,
        'products':Product.objects.all(),
        'category':get_object_or_404(Category, pk=category_id)
        
    }
    return render(request, 'scents/ScentType.html',context)




