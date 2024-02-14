# snacks/urls.py
from django.urls import path
from .views import HomeView, SnackListView, SnackDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('snacks/', SnackListView.as_view(), name='snack_list'),
    path('snacks/<int:pk>/', SnackDetailView.as_view(), name='snack_detail'),
]
