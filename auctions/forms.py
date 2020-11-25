from django import forms

from .models import Listing, Comment, Bid

class ListingForm(forms.ModelForm):

    class Meta:
        model = Listing
        exclude = ['creator','isActive','created_at']
        fields = ('title', 'description','image_link','category','startingBid','buyNowPrice')

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ['user', 'listing', 'timestamp']
        fields = ('text',)

class BidForm(forms.ModelForm):

    class Meta:
        model = Bid
        exclude = ['user', 'listing']
        fields = ('bidPrice',)
