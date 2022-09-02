from django.shortcuts import render, redirect, get_object_or_404
from ebook.models import Book
from .basket import Basket


def basket_add(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Book, id=product_id)
    quantity = int(request.GET.get('quantity', 1))
    basket.add(product=product, quantity=quantity)
    return redirect('detail_basket')


def basket_update(request, product_id, add=True):
    basket = Basket(request)
    product = get_object_or_404(Book, id=product_id)
    basket.add(product=product)
    return redirect('detail_basket')


def basket_remove(request, product_id):
    basket = Basket(request)
    product = get_object_or_404(Book, id=product_id)
    basket.remove(product)
    return redirect('detail_basket')


def basket_detail(request):
    basket = Basket(request)
    return render(request, 'basket/detail.html', {'basket': basket})