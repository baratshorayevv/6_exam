from django.shortcuts import render, redirect
from online_shop.models import Product

from django.shortcuts import get_list_or_404
from online_shop.forms import CommentForm

from online_shop.models import Coments
from django.contrib.auth import login

from .forms import RegistrationForm  



# Home sahifasi uchun view
def home_page(request):
    filter_type = request.GET.get('filter', '')
    if filter_type == 'Popular items':
        products = Product.objects.all().order_by('-rating')[:4]
    elif filter_type == 'New Arrivals':
        products = Product.objects.all().order_by('-id')
    elif filter_type == 'Cheap':
        products = Product.objects.all().order_by('old_price')
    elif filter_type == 'Expensive':
        products = Product.objects.all().order_by('-old_price')
    elif filter_type == 'Likes':
        products = Product.objects.all().order_by('-rating')
    else:
        products = Product.objects.all()

    rating_range = list(range(1, 6))

    context = {
        'products': products,
        'rating_range': rating_range
    }

    return render(request, 'home.html', context)


def detail_page(request, _id):
    product = Product.objects.get(id=_id)
    comments = Coments.objects.all().order_by('-created_at')[:3]
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form
            comment.product = product
            comment.save()
            return redirect('detail', _id)

    context = {
        'comments': comments,
        'product': product,
        'form': form
    }
    return render(request, 'detail.html', context)


def all_products(request):
    return render(request, 'all_products.html')

def popular_items(request):
    return render(request, 'popular_items.html')

def new_arrivals(request):
    return render(request, 'new_arrivals.html')

def product_search(request):
    query = request.GET.get('q')  
    if query:
        products = Product.objects.filter(name__icontains=query)  
    else:
        products = Product.objects.all()  
    return render(request, 'search_results.html', {'products': products})





def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('home')  
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})



