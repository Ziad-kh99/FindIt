from rest_framework import generics, permissions
from .models import Item, Tag, ItemTag
from .serializers import ItemSerializer, TagSerializer, ItemTagSerializer
from .permissions import IsOwner

class ItemListCreateView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Item.objects.all()
        
        return Item.objects.filter(user=user)

class ItemRetrieveUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    
