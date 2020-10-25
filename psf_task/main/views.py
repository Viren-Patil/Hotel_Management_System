from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.generic import ListView, FormView, DeleteView
from .models import Room, Booking, Restaurant
from django.utils.decorators import method_decorator
from .decorators import unauthenticated_user, allowed_users, student_only
from .forms import AvailabilityForm, TableBookingForm
from django.contrib import messages
from main.booking_functions.availability import check_availability

@method_decorator(login_required, name='dispatch')
@method_decorator(allowed_users(allowed_roles=['Customer']), name='dispatch')
class RoomList(ListView):
    model = Room
    template_name = 'main/home_customer.html'

    def get(self, request):
        booking_list = Booking.objects.filter(user=request.user)
        cat = ['YAC', 'NAC', 'DEL', 'KIN', 'QUE']
        roomlist = []
        for c in cat:
            roomlist.append(Room.objects.filter(category=c)[0])

        return render(request, self.template_name, {'title':'Home', 'room_list': roomlist, 'number_of_rooms': len(roomlist)})

@method_decorator(login_required, name='dispatch')
@method_decorator(allowed_users(allowed_roles=['Customer']), name='dispatch')
class BookingView(FormView):
    form_class = AvailabilityForm
    template_name = 'main/availability_form.html'

    def get_the_category(self, c):
        ROOM_CATEGORIES = (
            ('YAC', 'AC'),
            ('NAC', 'NON-AC'),
            ('DEL', 'DELUXE'),
            ('KIN', 'KING'),
            ('QUE', 'QUEEN'),
        )

        for i in ROOM_CATEGORIES:
            if i[0] == c:
                return i[1]

    def form_valid(self, form):
        data = form.cleaned_data
        room_list = Room.objects.filter(category=data['room_category'])
        available_rooms = []
        for room in room_list:
            if check_availability(room, data['check_in'], data['check_out']):
                available_rooms.append(room)
        
        if len(available_rooms) > 0:
            room = available_rooms[0]
            booking = Booking.objects.create(
                user = self.request.user,
                room = room,
                check_in = data['check_in'],
                check_out = data['check_out']
            )
            booking.save()
            messages.success(self.request, f'Your room has been booked!')
            return redirect('bookings')
        else:
            messages.error(
                self.request,
                f"Sorry! All the rooms of {self.get_the_category(data['room_category'])} category are occupied. Try other category!"
            )
            return redirect('booking_view')

@method_decorator(login_required, name='dispatch')
@method_decorator(allowed_users(allowed_roles=['Customer']), name='dispatch')
class RestaurantView(FormView):
    form_class = TableBookingForm
    template_name = 'main/restaurant_booking_form.html'
    
    def form_valid(self, form):
        data = form.cleaned_data
        room_booking_list = Booking.objects.filter(user=self.request.user)
        if len(room_booking_list) == 0:
            messages.error(self.request, f"You don't seem to have booked any room in our hotel! Go ahead and fill the form below to book a room!")
            return redirect('booking_view')
        rooms = []
        display_rooms = []
        for booking in room_booking_list:
            rooms.append((booking.room.number, booking))
            display_rooms.append(booking.room.number)
        flag = 0
        for r in rooms:
            if r[0] == data['room']:
                flag = 1
                bkng = r[1]

        if flag == 1:
            print(data['time'].date())
            if data['time'].date() < bkng.check_in or data['time'].date() > bkng.check_out:
                messages.error(self.request, f"You can book a table only between your check-in and check-out date of the room number that you enter in the form!")
                return redirect('table_booking')
            booking = Restaurant.objects.create(
                user = self.request.user,
                bkng = bkng,
                time = data['time']
            )
            booking.save()
            messages.success(self.request, f'Your table has been booked!')
            return redirect('bookings')

        elif flag == 0:
            messages.error(
                self.request, 
                f"Sorry you don't seem to have a booking with room number {data['room']} Your bookings: {display_rooms}"
            )
            return redirect('table_booking')

class CancelBookingView(DeleteView):
    model = Booking
    success_url = '/main/my-bookings/'

class CancelTableBookingView(DeleteView):
    model = Restaurant
    success_url = '/main/my-bookings/'

@login_required
@allowed_users(allowed_roles=['Customer'])
def payment(request):
    bookings = Booking.objects.filter(user=request.user)
    payment_list = []
    empty = False
    table_empty = False
    if len(bookings) == 0:
        empty = True
    else:
        for bk in bookings:
            table_bill = 0
            table = Restaurant.objects.filter(bkng=bk)
            if len(table) == 0:
                table_empty = True
            for t in table:
                if t.food_cost != None:
                    table_bill += t.food_cost
            room_cost = bk.get_cost()
            table_bill += room_cost
            payment_list.append([bk.room.number, bk.room.get_category(), bk.room.capacity, bk.room.beds, bk.check_in, bk.check_out, bk.room.price, table, table_empty, room_cost, table_bill])
        
    return render(request, 'main/payment.html', {'title': 'Payment', 'empty': empty, 'payment_list': payment_list})

@login_required
@allowed_users(allowed_roles=['Customer'])
def bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    table_booking_list = Restaurant.objects.filter(user=request.user)
    return render(request, 'main/bookings.html', {'title': 'My Bookings', 'bookings': bookings, 'table_booking_list': table_booking_list})

def about(request):
     return render(request, 'main/about.html', {'title': 'About'})


