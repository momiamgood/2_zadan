from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *

urlpatterns = [
                  path('', IndexView.as_view(), name='index'),
                  path('about', AboutView.as_view(), name='about'),
                  path('contacts', ContactsView.as_view(), name='contacts'),
                  path('add_product', AddProductView.as_view(), name='add_product'),
                  path('products', ProductsView.as_view(), name='products'),
                  path('login', Login.as_view(), name='login'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
