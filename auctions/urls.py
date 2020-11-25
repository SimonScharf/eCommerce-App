from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("listing<int:listing_id>", views.view_listing, name="view_listing"),
    path("watchlist", views.view_watchlist, name="view_watchlist"),
    path("add_comment<int:listing_id>", views.add_comment, name="add_comment")
]
