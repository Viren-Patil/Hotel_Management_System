from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date

class Room(models.Model):
    ROOM_CATEGORIES = (
        ('YAC', 'AC'),
        ('NAC', 'NON-AC'),
        ('DEL', 'DELUXE'),
        ('KIN', 'KING'),
        ('QUE', 'QUEEN'),
    )
    number = models.IntegerField()
    category = models.CharField(max_length=3, choices=ROOM_CATEGORIES)
    beds = models.IntegerField()
    capacity = models.IntegerField()
    price = models.IntegerField(default=1000)

    def get_category(self):
        for i in self.ROOM_CATEGORIES:
            if i[0] == self.category:
                return i[1]

    def get_image(self):
        if self.category == 'YAC':
            return 'ac'
        elif self.category == 'NAC':
            return 'nonac'
        elif self.category == 'DEL':
            return 'deluxe'
        elif self.category == 'KIN':
            return 'king'
        elif self.category == 'QUE':
            return 'queen'

    def __str__(self):
        return f'{self.number}. {self.category} with {self.beds} beds for {self.capacity} people'

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateField()
    check_out = models.DateField()
    total_cost = models.IntegerField(blank=True, null=True)

    def get_cost(self):
        d0 = date(self.check_in.year, self.check_in.month, self.check_in.day)
        d1 = date(self.check_out.year, self.check_out.month, self.check_out.day)
        stay = d1 - d0
        price_per_night = self.room.price
        cost = price_per_night * stay.days
        return cost

    def __str__(self):
        return f'{self.user} has booked {self.room} from {self.check_in} to {self.check_out}'

class Restaurant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    bkng = models.ForeignKey(Booking, on_delete=models.CASCADE)
    time = models.DateTimeField()
    food_cost = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'{self.user} has booked a table for {self.bkng.room.capacity} at {self.time}'

class Feedback(models.Model):
    RATING_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.CharField(max_length=1, choices=RATING_CHOICES)
    suggestion = models.TextField()

    def __str__(self):
        return f'{self.user} feedback'