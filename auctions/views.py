from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import User, Listing, Bid, Comment
from .forms import ListingForm, CommentForm


def index(request):
    listings = Listing.objects.filter(isActive = True).order_by('-created_at')
    return render(request, "auctions/index.html", {'listings': listings})


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

@login_required
def post_new(request):
    if request.method == "POST":
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.creator = request.user
            listing.save()
            return redirect('view_listing', pk=listing.pk)
    else:
        form = ListingForm()
    return render(request, 'auctions/createListing.html', {'form': form})


def add_comment(request, listing_id):

    if request.method == "POST":
        form = CommentForm(request.POST)
        message = None
        if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user
                listing = Listing.objects.get(id=listing_id)
                comment.listing = listing
                comment.save()
                return redirect('view_listing', listing_id)
        else:
            message = "User must be logged in to post comment."
        try:
            listing = Listing.objects.get(id=listing_id)
        except:
            return redirect('index')
        try:
            comments = Comment.objects.filter(listing=listing).order_by('-timestamp')
        except:
            comments = None
        return render(request, "auctions/listing.html", {
            "listing": listing,
            "comments": comments,
            "comment_form": comment_form,
            "message": message
        })
    else:
        return redirect('index')


def view_listing(request, listing_id):

        comment_form = CommentForm()
        # bid_form = BidForm()
        message = None
        try:
            listing = Listing.objects.get(id=listing_id)
        except:
            return redirect('index')
        try:
            comments = Comment.objects.filter(listing=listing).order_by('-timestamp')
        except:
            comments = None
        return render(request, "auctions/listing.html", {
            "listing": listing,
            "comments": comments,
            "comment_form": comment_form,
            "message": message
        })

@login_required
def view_watchlist(request):
    watchlist = request.user.watchlist.all()
    # Listing.objects.filter(isActive = True).order_by('-created_at')
    return render(request, "auctions/watchlist.html", {'listings': watchlist})
