from django.contrib import admin
from .models import Room, Booking, Restaurant, Feedback

admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Restaurant)
admin.site.register(Feedback)
admin.site.site_header = 'HMS ADMIN PORTAL'
admin.site.site_title = 'HMS ADMIN PORTAL'
admin.site.index_title = 'Welcome to the HMS Admin!'
