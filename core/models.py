from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


# TODO: django scheduler
# TODO: 

# Profile
# ----
# first
# last
# phone
# smsok
# carrier
# email
# Username
# auth_mode


# OrganizerProfile
# ----
# ???

# StudentProfile
# ----
# School (FK)


# Wait list
# ----
# Program (FK)
# Student (FK)
# position int, (auto inc)


# Watch List
# ----
# Student (FK)
# Program (FK)


# Program
# ----
# Contact (M2M)
# Category (FK)
# lat
# long
# name
# summary
# description
# status (approved, pending verfication,denied,)
# is_active
# start_date
# end_date
# start_time
# end_time
# frequecny
# logo image
# url
# phone
# fax
# ttd
# address 1
# address 2
# city
# state
# country (django-countries)
# zip
# type (FK? dropin signup)
# notes
# register instructions
# minage
# maxage
# rank
# capacity
# last mod date
# created date

# Frequency
# ----



# School
# ----
# name
# lat
# long
# address 1
# address 2
# city
# state
# country (django countries)
# zip
# level (choice list)
# district (standardized?)


# Cateogry
# ----
# name
# color

# Tag
# ----
# name
# color
# Category (FK)


# Generic Classes
class BusStop(models.Model):
    company = models.TextField()
    line = models.TextField()
    name = models.TextField()
    location = models.ForeignKey('Location')

class BartStop(models.Model):
    line = models.TextField()
    name = models.TextField()
    location = models.ForeignKey('Location')

class PhoneField(models.CharField): pass
class EventDate(models.Model):
    """
    Can this be replaced with a django scheduler?    
    """
    date = models.DateTimeField()


class School(models.Model):
    name = models.TextField()
    address = models.ForeignKey('Address')
    location = models.ForeignKey('Location')

class Profile(models.Model):
    user = models.ForeignKey(User, unique=True)
    school = models.ForeignKey(School, null=True)

    # it would be interesting to track favorite addresses
    # for students - esp those who are not in school - 
    # so we could better notify them of things nearby
     
class Contact(models.Model):
    """
    Contact info for projects and events
    """
    fullname = models.TextField(null=True)
    role = models.TextField(null=True)
    phone = PhoneField(null=True, max_length=20)
    smsok = models.BooleanField(default=False)
    tdd = PhoneField(null=True, max_length=20)
    fax = PhoneField(null=True, max_length=20)
    email = models.EmailField(null=True)
    web = models.URLField(null=True)

class Category(models.Model):
    """
    Moderated set of categories for events
    """
    name = models.TextField(unique=True)

class Tag(models.Model):
    """
    Moderated set of categories for events
    """
    name = models.TextField(unique=True)
    category = models.ForeignKey(Category)

class Location(models.Model):
    """
    GIS location data for events, schools,
    bus stops, and bart stops
    """
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)


class Address(models.Model):
    name = models.TextField()
    street = models.TextField()
    city = models.TextField(default='Oakland')
    state = models.CharField(max_length=2, default='CA')
    zipcode = models.PositiveIntegerField()
    district = models.PositiveIntegerField()

    # calculate on save
    bus = models.ManyToManyField(BusStop, null=True)
    bart = models.ManyToManyField(BartStop, null=True)

class Organization(models.Model):
    """
    An organization that offers Programs
    """
    name = models.TextField()
    about = models.TextField()
    headoffice = models.ForeignKey(Location, related_name='office')
    otherlocations = models.ManyToManyField(Location, related_name='locations')
    contacts = models.ManyToManyField(Contact)

    class Admin:
        pass


class Program(models.Model):
    """
    A single program for a single age group.
    """
    # lat
    # long
    # name
    # summary
    # description
    # status (approved, pending verfication,denied,)
    # is_active
    # start_date
    # end_date
    # start_time
    # end_time
    # frequecny
    # logo image
    # url
    # phone
    # fax
    # ttd
    # address 1
    # address 2
    # city
    # state
    # country (django-countries)
    # zip
    # type (FK? dropin signup)
    # notes
    # register instructions
    # minage
    # maxage
    # rank
    # capacity
    # last mod date
    # created date
    
    
    about = models.TextField()
    organization = models.ForeignKey(Organization)
    contacts = models.ManyToManyField(Contact, null=True)
    
    # how much does it cost, and whom is it for
    cost = models.FloatField(default=0.00)
    agemin = models.PositiveIntegerField(default=13)
    agemax = models.PositiveIntegerField(default=18)
    
    # who's going, how many total can attend
    attending = models.ForeignKey(User)
    totalseats = models.PositiveIntegerField()
    
    # the original datespec may be, e.g., 
    # "Every Tuesday and Thursday from 4-5
    # "for three weeks starting July 10"
    
    # We convert this to a list of dates
    datespec = models.TextField()
    dates = models.ManyToManyField(EventDate)
    dropin = models.BooleanField(default=False)
    
    # If it's by application, when the application is due
    byapplication = models.BooleanField(default=False)
    applicationdate = models.DateTimeField(null=True)
    tags = models.ManyToManyField(Tag)
    
    class Admin:
        pass

class Comment(models.Model):
    """
    A comment left by a user on an event
    """
    user = models.ForeignKey(User)
    program = models.ForeignKey(Program)
    flagged = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=140)

    class Meta:
        ordering = ["date"]

    class Admin:
        pass

    def __unicode__(self):
        return self.text

 
 
# -- Hoilding ---
