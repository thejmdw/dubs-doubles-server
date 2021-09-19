"""dubs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from dubsapi.views import register_user, login_user, Customers, Orders, Products, Toppings, LineItemToppings
from dubsapi.views import ProductTypes, LineItems, Payments, Users, Cart, Profile, ToppingTypes, totalSales, productSales, dailySales
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'products', Products, 'product')
router.register(r'producttypes', ProductTypes, 'producttype')
router.register(r'lineitems', LineItems, 'orderproduct')
router.register(r'lineitemtoppings', LineItemToppings, 'toppings')
router.register(r'customers', Customers, 'customer')
router.register(r'users', Users, 'user')
router.register(r'orders', Orders, 'order')
router.register(r'cart', Cart, 'cart')
router.register(r'paymenttypes', Payments, 'payment')
router.register(r'profile', Profile, 'profile')
router.register(r'toppingtypes', ToppingTypes, 'toppingtype')
router.register(r'toppings', Toppings, 'topping')
# router.register(r'images', ImageView, 'image')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('charts/totalsales', totalSales),
    path('charts/productsales', productSales),
    path('charts/dailysales', dailySales),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

