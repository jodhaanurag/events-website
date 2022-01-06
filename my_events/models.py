from django.db import models


class Event(models.Model):
    """
    Model for storing events.
    """
    event_name = models.CharField(max_length=100)
    data = models.CharField(max_length=1000)
    time = models.DateTimeField()
    location = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to="images/")
    is_liked = models.BooleanField(default=False)

