from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

class School(models.Model):
    name = models.TextField()
    address = models.ForeignKey('Address')
    location = models.ForeignKey('Location')

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique=True)
    school = models.ForeignKey(School, null=True)

    # it would be interesting to track favorite addresses
    # for students - esp those who are not in school - 
    # so we could better notify them of things nearby
    

class Contact(models.Model):
    """
    Contact info for projects and events
    """
    fullname = models.StringField(null=True)
    role = models.StringField(null=True)
    phone = models.PhoneField(null=True)
    smsok = models.BooleanField(default=False)
    tdd = models.PhoneField(null=True)
    fax = models.PhoneField(null=True)
    email = models.EmailField(null=True)
    web = models.URLField(null=True)

class Category(models.Model):
    """
    Moderated set of categories for events
    """
    name = models.StringField(unique=True)

class Location(models.Model):
    """
    GIS location data for events, schools,
    bus stops, and bart stops
    """
    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)

class BusStop(models.Model):
    company = models.StringField()
    line = models.StringField()
    name = models.StringField()
    location = models.ForeignKey(Location)

class BartStop(models.Model):
    line = models.StringField()
    name = models.StringField()
    location = models.ForeignKey(Location)

class Address(models.Model):
    name = models.StringField()
    street = models.StringField()
    city = models.StringField(default='Oakland')
    state = models.CharField(max_length=2, default='CA')
    zipcode = models.PositiveIntegerField()
    district = models.PositiveIntegerField()

    # calculate on save
    bus = models.ManyToManyField(BusLine, null=True)
    bart = models.ManyToManyField(BartStop, null=True)

class Organization(models.Model):
    """
    An organization that offers Programs
    """
    name = models.StringField()
    about = models.TextField()
    headoffice = models.ForeignKey(Location)
    otherlocations = models.ManyToManyField(Location)
    contacts = models.ManyToManyField(Contact)

    class Admin:
        pass

class EventDate(models.Model):
    date = models.DateTimeField()

class Program(models.Model):
    """
    A single program for a single age group.
    """
    about = models.TextField()
    program = models.ForeignKey(Program)
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
    datespec = models.StringField()
    dates = models.ManyToManyField(EventDate)

    dropin = models.BooleanField(default=False)

    # If it's by application, when the application is due
    byapplication = models.BooleanField(default=False)
    applicationdate = models.DateTimeField(null=True)

    categories = models.ManyToManyField(Category)

    class Admin:
        pass

class Comment(models.Model):
    """
    A comment left by a user on an event
    """
    user = models.ForeignKey(User)
    event = models.ForeignKey(Event)
    flagged = models.BooleanField(default=False)
    date = models.DateTimeField(auto_add_now=True)
    text = models.CharField(max_length=140)

    class Meta:
        ordering = ["event"]

    class Admin:
        pass

    def __unicode__(self):
        return self.text

