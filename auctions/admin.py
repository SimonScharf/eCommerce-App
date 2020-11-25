from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Listing, Bid, Comment


class ListAdmin(admin.ModelAdmin):
    pass

class UserAdmin(admin.ModelAdmin):
    pass

class BidAdmin(admin.ModelAdmin):

    def form_valid(self, form):
        bid = form.save(commit=False)
        bid.user = self.request.user
        bid.save()


admin.site.register(User, UserAdmin)
admin.site.register(Listing, ListAdmin)
admin.site.register(Bid, BidAdmin)
admin.site.register(Comment)
# Register your models here.
