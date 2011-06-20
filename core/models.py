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
    school = models.ForeignKey('School', blank=True, null=True)
    watch_list = models.ForeignKey('WatchList', blank=True, null=True, related_name="profile_watch_list")

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
    name = models.CharField(max_length=200, unique=True)
    address = models.ForeignKey('Address', blank=True, null=True)    
    contact = models.ForeignKey('Contact', blank=True, null=True)
    district = models.PositiveIntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.name
 
class Address(models.Model):
    street1 = models.CharField(max_length=250)
    street2 = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=100, default='Oakland')
    state = USStateField(choices=STATE_CHOICES, default='CA', blank=True, null=True)
    country = CountryField(blank=True, null=True, default='US')
    zipcode = USPostalCodeField(blank=True, null=True)

    # GIS is computed as a post-save process, so must
    # be able to be null on first save
    location = models.ForeignKey('GIS', blank=True, null=True)

    def __unicode__(self):
        return self.street1

class GIS(models.Model):
    """
    GIS location data for events, schools,
    bus stops, and bart stops
    """
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
 
 
class EventDate(models.Model):
    """
    Can this be replaced with a django scheduler?    
    """
    date = models.DateTimeField()
    duration_mins = models.PositiveIntegerField(default=60)

    def __unicode__(self):
        return self.date.isoformat()

    class Meta:
        ordering = ['date']
      
class Contact(models.Model):
    """
    Contact info for projects and events
    """
    first_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=40, blank=True, null=True)
    role = models.CharField(max_length=200, blank=True, null=True)
    phone = PhoneNumberField(blank=True, null=True)
    smsok = models.BooleanField(default=False)
    tdd = PhoneNumberField(max_length=20, blank=True, null=True)
    fax = PhoneNumberField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    web = models.URLField(blank=True, null=True)

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
    name = models.CharField(max_length=60, unique=True)

    def __unicode__(self):
        return self.name
 
class Tag(models.Model):
    """
    Moderated set of subcats for events
    """
    name = models.CharField(max_length=60, unique=True)
 
    def __unicode__(self):
        return self.name
 
class Organization(models.Model):
    """
    An organization that offers Programs
    """
    name = models.CharField(max_length=250, unique=True)
    about = models.TextField(blank=True, null=True)
    headoffice = models.ForeignKey('Address', related_name='office')
    contact = models.ForeignKey('Contact')
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)    

    def __unicode__(self):
        return self.name
 
class Program(models.Model):
    """
     Program info
    """
 
    # Core Details
    name = models.CharField(max_length=200, blank=True, null=True)
    summary = models.TextField(blank=True, null=True)
    about = models.TextField()
    organization = models.ForeignKey('Organization', blank=True, null=True)
    address = models.ForeignKey('Address')
     
    notes = models.TextField(blank=True, null=True)
    primary_contact = models.ForeignKey('Contact', null=True)
 
    # Time
    events = models.ManyToManyField('EventDate')
     
    # Attendee Details
    cost = models.FloatField(default=0.00)
    agemin = models.PositiveIntegerField(default=13)
    agemax = models.PositiveIntegerField(default=18)
    registration_needed = models.BooleanField(blank=True, default=False)
    # validate required if reg_needed
    registration_due_by = models.DateTimeField(blank=True, null=True) 
    registration_instructions = models.TextField(blank=True, null=True)
         
    # Organization
    categories = models.ManyToManyField('Category')
    tags = models.ManyToManyField('Tag')
    # todo: make subcat intelligent based on cat selected
 
    # Meta
    is_active = models.BooleanField(default=False)

    program_status = models.ForeignKey('ProgramStatus', null=True) # eg pending approval, approved, denied, need verifications, etc.
    program_type = models.ForeignKey('ProgramType', null=True) # eg drop-in, register

    rank = models.IntegerField(default=-1)
    capcity = models.PositiveIntegerField(null=True) # who's going, how many total can attend
    wait_list = models.ForeignKey('WaitList', blank=True, null=True, related_name="program_wait_list")
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
         
    # holding
    # logo = models.ImageField()
    # attending = models.ForeignKey(User)

    def next_event(self):
        import datetime
        events = self.events.filter(date__gt=datetime.datetime.now()).order_by('date')
        if events: 
            return events[0].date
        return None

    def time_until(self):
        return "hi"

    def __unicode__(self):
        return self.name
 
 
class ProgramStatus(models.Model):
    program_status = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
 
class ProgramType(models.Model):
    program_type = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
 
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
     
    company = models.CharField(max_length=100)
    line = models.CharField(max_length=40)
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
