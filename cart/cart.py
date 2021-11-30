# from decimal import Decimal
# from django.conf import settings
#
# from mainapp.models import Product
#
# class Cart(object):
#     def __init__(self, request):
#         """Инициализация объекта корзины."""
#         self.session = request.session
#         cart = self.session.get(settings.CART_SESSION_ID)
#         if not cart:
#             # Сохраняем в сессии пустую корзину.
#             cart = self.session[settings.CART_SESSION_ID] = {}
#             self.cart = cart
#
#     def add(self, product, quantity=1, update_quantity=False):
#         """Добавление товара в корзину или обновление его количества."""
#         product_id = str(product.id)
#         if product_id not in self.cart:
#             self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
#         if update_quantity:
#             self.cart[product_id]['quantity'] = quantity
#         else:
#             self.cart[product_id]['quantity'] += quantity
#         self.save()
#
#
#     def save(self):
#         # Помечаем сессию как измененную
#         self.session.modified = True
#
#
#     def remove(self, product):
#         """Удаление товара из корзины."""
#         product_id = str(product.id)
#         if product_id in self.cart:
#             del self.cart[product_id]
#             self.save()