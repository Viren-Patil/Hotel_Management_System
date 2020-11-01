import datetime
from main.models import Room, Booking

def check_availability(room, check_in, check_out):
    avail_list = []
    booking_list = Booking.objects.filter(room=room)
    if len(booking_list) == 0:
        return True
    for booking in booking_list:
        if(check_out < booking.check_in or check_in > booking.check_out):
            avail_list.append(True)
        else:
            avail_list.append(False)

    return all(avail_list)