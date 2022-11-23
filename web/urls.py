from django.contrib import admin
from django.urls import path, include

from web.views import main_view, ItemDetailView

urlpatterns = [
    path('', main_view, name='main'),
    path("item/<int:pk>/", ItemDetailView.as_view(), name="site"),
]
