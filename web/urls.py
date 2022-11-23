from django.contrib import admin
from django.urls import path, include

from web.views import main_view, ItemDetailView, pay_view, success_view, cancel_view

urlpatterns = [
    path('', main_view, name='main'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item'),
    path('buy/<int:pk>/', pay_view),
    path('success', success_view),
    path('cancel', cancel_view),
]
