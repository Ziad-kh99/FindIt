from django.urls import path
from .views import MatchesListView


urlpatterns = [
    path('', MatchesListView.as_view()),
]

