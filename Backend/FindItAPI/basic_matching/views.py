from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Match
from .serializers import MatchSerializer


class MatchesListView(generics.ListAPIView):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]     # AdminUser => user.is_staf = True


