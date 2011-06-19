from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django_countries import CountryField
from django.contrib.localflavor.us.models import *
from django.contrib.localflavor.us.us_states import STATE_CHOICES
# https://docs.djangoproject.com/en/1.3/ref/contrib/localflavor/#united-states-of-america-us

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


# User model?
# first name
# last name
# auth_mode (custom, facebook, tumblr?)


class Profile(models.Model):
    """
        Profile extends Django User Model
        todo: Selection should eventually be intelligent based on location
    """
    user = models.ForeignKey(User, unique=True, verbose_name='user')
    school = models.ForeignKey('School', null=True)
    watch_list = models.ForeignKey('WatchList', null=True)
    
class School(models.Model):
    name = models.CharField(max_length=40, unqique=True)
    address = models.ForeignKey('Address', null=True)    


class Address(models.Model):
    name = models.TextField(unique=True)
    street1 = models.TextField()
    street2 = models.TextField(null=True)
    city = models.TextField(default='Oakland')
    state = USStateField(choices=STATE_CHOICES)
    country = CountryField()
    zipcode = USPostalCodeField()
    district = models.PositiveIntegerField(null=True) # prepopulated?
    location = models.ForeginKey('Location')
class GIS(models.Model):
    """
    GIS location data for events, schools,
    bus stops, and bart stops
    """
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)



class EventDate(models.Model):
    """
    Can this be replaced with a django scheduler?    
    """
    date = models.DateTimeField()

     
class Contact(models.Model):
    """
    Contact info for projects and events
    """
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    role = models.TextField(null=True)
    phone = PhoneNumberField(null=True)
    smsok = models.BooleanField(default=False)
    tdd = PhoneNumberField(max_length=20)
    fax = PhoneNumberField(max_length=20)
    email = models.EmailField(null=True)
    web = models.URLField(null=True)

class Category(models.Model):
    """
    Moderated set of categories for events
    """
    name = models.TextField(unique=True)
    color = models.TextField(max_length=11, null=True)

class SubCategory(models.Model):
    """
    Moderated set of subcats for events
    """
    name = models.TextField(unique=True)
    category = models.ForeignKey('Category')
    color = models.TextField(max_length=11, null=True)


class Organization(models.Model):
    """
    An organization that offers Programs
    """
    name = models.TextField(unique=True)
    about = models.TextField(null=True)
    headoffice = models.ForeignKey('Address', related_name='office')
    otherlocations = models.ManyToManyField('Address', related_name='locations')
    contacts = models.ManyToManyField('Contact')
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)    

class Program(models.Model):
    """
     Program info
    """"

    # Core Details
    name = models.CharField(max_length=20, null=True)
    summaary = models.TextField(max_length=140, null=True)
    about = models.TextField()
    organization = models.ForeignKey('Organization', null=True)
    address = models.ForeignKey('Address')
    
    notes = models.DateTimeField(null=True)
    primary_contact = models.ForeignKey('Contact')

    # Time
    start_date = models.ManyToManyField('EventDate')
    end_date = models.ManyToManyField('EventDate')
    frequency = models.CharField(max_length=20, null=True) # todo: make this better, scheduling app?

    
    # Attendee Details
    cost = models.FloatField(default=0.00)
    agemin = models.PositiveIntegerField(default=13)
    agemax = models.PositiveIntegerField(default=18)
    registration_needed = models.BooleanField(default=False)
    registration_due_by = models.DateTimeField() # validate required if reg_needed
    registration_instructions = models.TextField(null=True)
        
    # Organization
    category = models.ForeignKey('Category')
    sub_category = models.ForeignKey('SubCategory')
    # todo: make subcat intelligent based on cat selected

    # Meta
    is_active = models.BooleanField(default=False)
    program_status = models.ForeignKey('ProgramStatus') # eg pending approval, approved, denied, need verifications, etc.
    program_type = models.ForeignKey('ProgramTypes') # eg drop-in, register
    rank = models.PositiveIntegerField(default=-1)
    capcity = models.PositiveIntegerField() # who's going, how many total can attend
    wait_list = models.ForeignKey('WaitList', null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
        
    # holding
    # logo = models.ImageField()
    # attending = models.ForeignKey(User)


class ProgramStatus(models.Model):
    program_status = models.TextField(max_length=20)
    description = models.TextField(null=True)

class ProgramType(models.Model):
    program_type = models.TextField(max_length=20)
    description = models.TextField(null=True)
   
    
# -- Hoilding ---
# class Comment(models.Model):
#     """
#     A comment left by a user on an event
#     """
#     user = models.ForeignKey(User)
#     program = models.ForeignKey(Program)
#     flagged = models.BooleanField(default=False)
#     date = models.DateTimeField(auto_now_add=True)
#     text = models.CharField(max_length=140)
# 
#     class Meta:
#         ordering = ["date"]
# 
#     class Admin:
#         pass
# 
#     def __unicode__(self):
#         return self.text



class WatchList(models.Model):
    profile = models.ForeignKey('Profile')
    program = models.ForeignKey('Program')
    date_added = models.DateTimeField(auto_now_add=True)
    
class WaitList(models.Model):
    profile = models.ForeignKey('Profile')
    program = models.ForeignKey('Program')
    date_added = models.DateTimeField(auto_now_add=True)
    position = models.PositiveIntegerField()
    
    def save(self):
        self.position += 1
        super(WaitList,self).save()
            
class PublicTransport(models.Model):
    ''' Pull data with APIs?'''
    
    TRANSPORT_CHOICES = (
        ('B', 'Bus'),
        ('T', 'Train'),
        ('LR', 'Light Rail'),
    )
    
    company = models.TextField()
    line = models.TextField(max_length=40)
    name = models.CharField(max_length=40)
    address = models.ForeignKey('Address')
    pt_type = models.CharField(max_length=10, choices=TRANSPORT_CHOICES)
