from django.db import models
from items.models import Item


class Match(models.Model):
    MATCH_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('rejected', 'Rejected')
    ]
    
    lost_item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='lost_matches')
    found_item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='found_matches')
    match_status = models.CharField(max_length=100, choices=MATCH_STATUS_CHOICES, default='pending')

    def __str__(self):
        return f'Match: {self.lost_item.title} - {self.found_item.title}'


