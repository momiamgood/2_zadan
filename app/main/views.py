from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.views.generic import TemplateView, ListView, CreateView

from .forms import ProductAddForm
from .models import Products


# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'


class ContactsView(TemplateView):
    template_name = 'contacts.html'


class AboutView(TemplateView):
    template_name = 'about.html'


class Login(LoginView):
    template_name = 'login.html'
    model = User
    success_url = '/'


class ProductsView(ListView):
    model = Products
    template_name = 'products.html'
    context_object_name = 'products_list'


class AddProductView(CreateView, LoginRequiredMixin):
    template_name = 'add_product.html'
    model = Products
    login_url = '/login'
    success_url = '/products'
    form_class = ProductAddForm

