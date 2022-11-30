from django.shortcuts import render, redirect, get_object_or_404
from ebook.models import Book
from .basket import Basket
from .models import Order


def basket_add(request, product_id):
    # Додати книжку до кошика
    basket = Basket(request)
    product = get_object_or_404(Book, id=product_id)
    quantity = int(request.GET.get('quantity', 1))
    basket.add(product=product, quantity=quantity)
    return redirect('detail_basket')


def basket_remove(request, product_id):
    # Видалити книжку з кошика
    basket = Basket(request)
    product = get_object_or_404(Book, id=product_id)
    basket.remove(product)
    return redirect('detail_basket')


def basket_detail(request):
    return render(request, 'basket/detail.html', )


def checkout(request):
    return render(request, 'basket/checkout.html')


def done(request):
    # Додавання заказу до бд та знищення request.session['ID_SESSION']
    if request.method == 'POST':
        user_id = int(request.POST['user_id'])
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        phone = request.POST['phone']
        email = request.POST['email']
        city = request.POST['city']
        address = request.POST['address']
        order = request.POST['order']
        price = int(request.POST['price'])
        payment = True if request.POST['payment'] == 'on' else False

        add_order = Order(user_id=user_id,
                          last_name=last_name,
                          first_name=first_name,
                          phone=phone,
                          email=email,
                          city=city,
                          address=address,
                          order=order,
                          price=price,
                          payment=payment)
        add_order.save()
        number_order = add_order.id

    del request.session['ID_SESSION']
    return render(request, 'basket/done.html', {'number_order': number_order})
