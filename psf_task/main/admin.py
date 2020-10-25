from django.contrib import admin
from .models import Room, Booking, Restaurant

# admin.site.register(Post)
# admin.site.register(Applicant)
admin.site.register(Room)
admin.site.register(Booking)
admin.site.register(Restaurant)
admin.site.site_header = 'HMS ADMIN PORTAL'
admin.site.site_title = 'HMS ADMIN PORTAL'
admin.site.index_title = 'Welcome to the HMS Admin!'
