from django.urls import path
from . import views
from .views import RoomList, BookingView, CancelBookingView, RestaurantView, CancelTableBookingView

urlpatterns = [
    path('home-customer/', RoomList.as_view(), name='main-home'),
    path('booking/', BookingView.as_view(), name='booking_view'),
    path('my-bookings/', views.bookings, name='bookings'),
    path('table-booking/', RestaurantView.as_view(), name='table_booking'),
    path('booking/cancel/<pk>', CancelBookingView.as_view(), name='cancel_booking_view'),
    path('table-booking/cancel/<pk>', CancelTableBookingView.as_view(), name='cancel_table_booking_view'),
    path('payment/', views.payment, name='payment'),
    path('about/', views.about, name='about'),
]