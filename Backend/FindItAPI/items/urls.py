from django.urls import path
from .views import (
    ItemListCreateView,
    ItemRetrieveUpdateView,
)

urlpatterns = [
    path('', ItemListCreateView.as_view()),
    path('<int:pk>/', ItemRetrieveUpdateView.as_view()),
]
