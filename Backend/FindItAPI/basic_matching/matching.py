from django.db.models import Q
from .models import Match
from items.models import Item

class BasicMatching:
    @classmethod
    def perform_matching(cls, item):
        if item.item_type == 'lost':
            matching_items = Item.objects.filter(
                Q(item_type = 'found'),
                Q(location = item.location),
                Q(item_status = 'searching')
            )
        elif item.item_type == 'found':
            matching_items = Item.objects.filter(
                Q(item_type = 'lost'),
                Q(location = item.location),
                Q(item_status = 'searching')
            )
        else:
            matching_items = Item.objects.none()

        if matching_items.exists():
            for matching_item in matching_items:
                Match.objects.create(lost_item = item if item.item_type == 'lost' else matching_item, 
                                     found_item = item if item.item_type == 'found' else matching_item)

                item.item_status = 'matching'
                matching_item.item_status = 'matching'
                item.save()
                matching_item.save()

        else:
            item.save()



