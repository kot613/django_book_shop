from django.conf import settings
from ebook.models import Book


class Basket(object):

    def __init__(self, request):
        # Ініціалізація кошика
        self.session = request.session
        basket = self.session.get(settings.CART_SESSION_ID)
        if not basket:
            basket = self.session[settings.CART_SESSION_ID] = {}
        self.basket = basket

    def __iter__(self):
        # Перебираємо товари в кошику та отримуємо товари з бази даних.
        product_ids = self.basket.keys()
        products = Book.objects.filter(id__in=product_ids)

        basket = self.basket.copy()
        for product in products:
            basket[str(product.id)]['product'] = product

        for item in basket.values():
            item['price'] = item['price']
            item['total_price'] = int(item['price']) * item['quantity']
            yield item

    def add(self, product, quantity=1):
        # Додаємо товар у кошик чи оновлюємо його кількість.
        product_id = str(product.id)
        if product_id not in self.basket:
            self.basket[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        self.basket[product_id]['quantity'] += quantity
        if not self.basket[product_id]['quantity']:
            del self.basket[product_id]
        self.save()

    def save(self):
        # зберігаємо товар
        self.session.modified = True

    def remove(self, product):
        # Видаляємо товар
        product_id = str(product.id)
        if product_id in self.basket:
            del self.basket[product_id]
            self.save()

    def get_total_price(self):
        # отримуємо загальну вартість
        return sum(int(item['price']) * item['quantity'] for item in self.basket.values())

    def get_total_quantity(self):
        # отримуємо загальну вартість
        return sum(int(item['quantity']) for item in self.basket.values())


