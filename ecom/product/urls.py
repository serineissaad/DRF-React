from django.urls import path
from django.views.generic import TemplateView
from .views import index


app_name = 'product'

urlpatterns = [
    path('', TemplateView.as_view(template_name="product/index.html")),
    #path('', index),
]