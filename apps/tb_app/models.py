# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if 'name' in postData:
            if len(postData['name']) < 3:
                errors["name"] = "name must be at least 3 characters"
        if len(postData['username']) < 3:
            errors["username"] = "username must be at least 3 characters"
        if len(postData['password']) < 8:
            errors["password"] = "password must be at least 8 characters"
            
        return errors

# class TripManager(models.Manager):
#     def basic_validator(self, postData):
#         errors = {}
#         if len(postData['destination']) < 1:
#                 errors["destination"] = "name must be at least 1 character"
#         if len(postData['description']) < 1:
#             errors["description"] = "description must be at least 1 character"
#         if len(postData['TravelDateFrom']) < 1:
#             errors["password"] = "TravelDateFrom must be at least 1 characters"
#         if len(postData['TravelDateTo']) < 1:
#             errors["TravelDateTo"] = "TravelDateTo must be at least 1 characters"
#         if postData['TravelDateFrom'] <= datetime.date.today():
#             errors["TravelDateFrom"] = "TravelDateFrom must be in the future"    
#         return errors
        
class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    def __str__(self):
         return self.name

class TripSchedule(models.Model):
    destination = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    TravelDateFrom = models.DateField()
    TravelDateTo = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, related_name = 'users') #added, a user can have many tripscheudles.
    # user_id = models.IntegerField()
    # objects = TripManager()


#carried over from old code.
# class Follow(models.Model): 
#     trip = models.ForeignKey(TripSchedule, related_name = 'users')
#     follower= models.ForeignKey(User, related_name = 'trips')

class Follow(models.Model): 
    trip = models.ForeignKey(TripSchedule, related_name = 'users')
    follower= models.ForeignKey(User, related_name = 'trips')


# Got rid of this code since the user id is now directly associated with the trip id.
# class Trip(models.Model): #addded
#     # admin = models.ForeignKey(TripSchedule, related_name = "trips")
#     # admin = models.OneToOneField(User, on_delete=models.CASCADE) 
#     admin = models.ForeignKey(User, related_name = 'adminrelated') 
#     trip = models.OneToOneField(TripSchedule, on_delete=models.CASCADE)
    

# class TripUser(models.Model):
#     user = models.ForeignKey(User, related_name = 'trips')
#     trip = models.ForeignKey(TripSchedule, related_name = 'users')
