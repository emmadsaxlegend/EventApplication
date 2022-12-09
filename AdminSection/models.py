from django.db import models
from django.urls import reverse


# Create your models here.


class Event(models.Model):
    event_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    paid = models.CharField(max_length=100, blank=True, null=True,)
    price = models.CharField(max_length=100, blank=True, null=True,)
    space_capacity = models.CharField(max_length=100, blank=True, null=True,)
    description = models.TextField(max_length=5000, blank=True, null=True,)
    event_date = models.DateTimeField(null=True, blank=True)
    event_end_date = models.DateTimeField(null=True, blank=True)
    header_image = models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return self.event_name + " event in " + str(self.location)
 
    def get_absolute_url(self):
        # ------------Return to Details View ---------------
        # return reverse("article-detail", kwargs={"pk": self.pk})
        #-----------Return to Home View-------------
        return reverse("dashboard")  