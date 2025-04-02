from rest_framework import generics, permissions
from .models import Item, Tag, ItemTag
from .serializers import ItemSerializer, TagSerializer, ItemTagSerializer
from .permissions import IsOwner
from basic_matching.matching import BasicMatching
class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        item = serializer.save(user=self.request.user)
        BasicMatching.perform_matching(item)

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Item.objects.all()
        
        return Item.objects.filter(user=user)

class ItemRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    
