from django import forms
from .models import Room, User, Restaurant, Booking
from django.utils import timezone
import datetime

check = []

def present_or_future_checkin_date(value):
    if value < datetime.date.today():
        raise forms.ValidationError("The date cannot be in the past!")
    else:
        check.append(value)
        print(check)
    return value

def present_or_future_checkout_date(value):
    if value < datetime.date.today():
        raise forms.ValidationError("The date cannot be in the past!")
    else:
        check.append(value)
        print(check)
        if (check[1] <= check[0]):
            while (len(check) != 0):
                check.pop()
            print(check)
            raise forms.ValidationError("The checkout date cannot be before checkin date!")
        else:
            while (len(check) != 0):
                check.pop()
    return value

def present_or_future_datetime(value):
    if value < timezone.now():
        raise forms.ValidationError("The date and time cannot be in the past!")
    return value

class AvailabilityForm(forms.Form):
    ROOM_CATEGORIES = (
        ('YAC', 'AC'),
        ('NAC', 'NON-AC'),
        ('DEL', 'DELUXE'),
        ('KIN', 'KING'),
        ('QUE', 'QUEEN'),
    )
    room_category = forms.ChoiceField(choices=ROOM_CATEGORIES, required=True)
    check_in = forms.DateField(
        widget=forms.DateInput(     
            attrs={'type': 'date'} 
        )
    )
    check_out = forms.DateField(
        widget=forms.DateInput(     
            attrs={'type': 'date'} 
        )
    )

class TableBookingForm(forms.Form):
    room = forms.IntegerField()
    check_in = forms.DateField(
        widget=forms.DateInput(     
            attrs={'type': 'date'} 
        )
    )
    check_out = forms.DateField(
        widget=forms.DateInput(     
            attrs={'type': 'date'} 
        )
    )
    time = forms.DateTimeField(
        widget=forms.DateTimeInput(     
            attrs={'type': 'datetime-local'} 
        ),
        validators=[present_or_future_datetime]
    )

class FeedbackForm(forms.Form):
    RATING_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    room = room = forms.IntegerField()
    rating = forms.ChoiceField(choices=RATING_CHOICES, required=True)
    suggestions_or_complaints = forms.CharField(widget=forms.Textarea)
