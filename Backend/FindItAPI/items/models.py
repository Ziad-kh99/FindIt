from django.db import models
from users.models import CustomUser

class Item(models.Model):
    ITEM_TYPE_CHOICES = [
        ('lost', 'Lost'),
        ('found', 'Found')
    ]

    ITEM_STATUS_CHOICES = [
        ('searching', 'Searching'),
        ('matching', 'Matching'),
        ('matched', 'Matched')
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    item_type = models.CharField(unique=True, max_length=100, choices=ITEM_TYPE_CHOICES)
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_time_reported = models.DateTimeField(auto_now_add=True)
    date_time = models.DateTimeField()
    location = models.CharField(max_length=255)
    image_path = models.CharField(max_length=255, null=True, blank=True)
    item_status = models.CharField(max_length=100, choices=ITEM_STATUS_CHOICES, default='searching')

    def __str__(self):
        return self.title 
    
class Tag(models.Model):
    name = models.CharField(unique=True, max_length=100)

    def __str__(self):
        return self.name
    
class ItemTag(models.Model):
    item = models.ManyToManyField(Item)
    tag = models.ManyToManyField(Tag)

    # class Meta:
    #     unique_together = ('item', 'tag')

    def __str__(self):
        return f'{self.item.title} - {self.tag.name}'
