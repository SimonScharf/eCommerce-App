from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Listing(models.Model):

    CATEGORY = (
        ("SPORTS", "Sports"),
        ("ELECTRONICS", "Electronics"),
        ("FASHION", "Fashion"),
        ("TOYS", "Toys"),
        ("HOME", "Home"),
        ("MISCELLANEOUS", "Miscellaneous")
    )

    creator =  models.ForeignKey(User, on_delete=models.CASCADE, related_name="listings", default=None)
    title = models.CharField(max_length=32,default='')
    description = models.TextField()
    image_link = models.CharField(max_length=256, default=None, blank=True, null=True)
    category = models.CharField(max_length=64, choices = CATEGORY, default="Category not specified.")
    isActive = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    startingBid = models.IntegerField(default=1)
    buyNowPrice = models.IntegerField(default=1)

    watchlistUsers = models.ManyToManyField(User, blank=True, related_name="watchlist", default=None)
    #users that have this listing on their watchlist
    def __str__(self):
        return f"Listing {self.id}: {self.title}"


class Bid(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bids", default=None)
    listing = models.OneToOneField(
        Listing,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name="currentBid",
        default=None
    )
    bidPrice = models.IntegerField(default=1)

    def __str__(self):
        return f"${self.bidPrice}.00"



class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments", default=None)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="comments", default=None)
    text = models.TextField(default='')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.listing} by {self.user}"
