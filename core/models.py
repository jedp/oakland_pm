from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic
from django_countries import CountryField
from django.contrib.localflavor.us.models import *
from django.contrib.localflavor.us.us_states import STATE_CHOICES
# https://docs.djangoproject.com/en/1.3/ref/contrib/localflavor/#united-states-of-america-us
 
# TODO: django scheduler
# TODO: confirm what's in User model
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
    watch_list = models.ForeignKey('WatchList', null=True, related_name="profile_watch_list")

    # class Meta:
    #      verbose_name_plural = 'Profiles'
    #      ordering = ('user',)
    # 
    #  def __unicode__(self):
    #      return self.user
    # 
    #  @models.permalink
    #  def get_absolute_url(self):
    #      return ('view_forum_category', (self.forum.slug, self.slug,))    
     
class School(models.Model):
    name = models.CharField(max_length=40, unique=True)
    address = models.ForeignKey('Address', null=True)    
    contact = models.ForeignKey('Contact', null=True)
    district = models.PositiveIntegerField(null=True)

    def __unicode__(self):
        return self.name
 
class Address(models.Model):
    street1 = models.TextField()
    street2 = models.TextField(null=True)
    city = models.TextField(default='Oakland')
    state = USStateField(choices=STATE_CHOICES, default='CA', null=True)
    country = CountryField(null=True, default='United States')
    zipcode = USPostalCodeField(null=True)

    # GIS is computed as a post-save process, so must
    # be able to be null on first save
    location = models.ForeignKey('GIS', null=True)

    def __unicode__(self):
        return self.street1

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
    duration_mins = models.PositiveIntegerField(default=60)

    def __unicode__(self):
        return self.date.isoformat()
      
class Contact(models.Model):
    """
    Contact info for projects and events
    """
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    role = models.TextField(null=True)
    phone = PhoneNumberField(null=True)
    smsok = models.BooleanField(default=False)
    tdd = PhoneNumberField(max_length=20, null=True)
    fax = PhoneNumberField(max_length=20, null=True)
    email = models.EmailField(null=True)
    web = models.URLField(null=True)

    def __unicode__(self):
        if self.email:
            return self.email
        if self.phone:
            return self.phone
        if self.web:
            return self.web
        return '<Contact at 0x%x>' % (id(self))

 
class Category(models.Model):
    """
    Moderated set of categories for events
    """
    name = models.TextField(unique=True)
    color = models.TextField(max_length=11, null=True)

    def __unicode__(self):
        return self.name
 
class SubCategory(models.Model):
    """
    Moderated set of subcats for events
    """
    name = models.TextField(unique=True)
    category = models.ForeignKey('Category')
    color = models.TextField(max_length=11, null=True)
 
    def __unicode__(self):
        return self.name
 
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

    def __unicode__(self):
        return self.name
 
class Program(models.Model):
    """
     Program info
    """
 
    # Core Details
    name = models.CharField(max_length=20, null=True)
    summaary = models.TextField(max_length=140, null=True)
    about = models.TextField()
    organization = models.ForeignKey('Organization', null=True)
    address = models.ForeignKey('Address')
     
    notes = models.TextField(null=True)
    primary_contact = models.ForeignKey('Contact')
 
    # Time
    dates = models.ManyToManyField('EventDate')
     
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
    program_type = models.ForeignKey('ProgramType') # eg drop-in, register
    rank = models.IntegerField(default=-1)
    capcity = models.PositiveIntegerField() # who's going, how many total can attend
    wait_list = models.ForeignKey('WaitList', null=True, related_name="program_wait_list")
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
 
class WatchList(models.Model):
    profile = models.ForeignKey('Profile', related_name="watchlist_profile")
    program = models.ForeignKey('Program', related_name="watchlist_program")
    date_added = models.DateTimeField(auto_now_add=True)
     
class WaitList(models.Model):
    profile = models.ForeignKey('Profile', related_name="waitlist_profile")
    program = models.ForeignKey('Program', related_name="waitlist_program")
    date_added = models.DateTimeField(auto_now_add=True)
    position = models.PositiveIntegerField(default=0)
     
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
