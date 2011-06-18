# settings_auth.py
#
# this is imported by settings.py only if social_auth can be 
# imported, which means openid, oauth2, etc. all work.  You
# Probably don't want to bother with this in dev, since you 
# can't easily use facebook etc. auth from a localhost addr.

AUTHENTICATION_BACKENDS = (
    #'social_auth.backends.twitter.TwitterBackend',
    'social_auth.backends.facebook.FacebookBackend',
    #'social_auth.backends.google.GoogleOAuthBackend',
    #'social_auth.backends.google.GoogleOAuth2Backend',
    #'social_auth.backends.google.GoogleBackend',
    #'social_auth.backends.yahoo.YahooBackend',
    #'social_auth.backends.contrib.linkedin.LinkedinBackend',
    #'social_auth.backends.contrib.LiveJournalBackend',
    #'social_auth.backends.contrib.orkut.OrkutBackend',
    #'social_auth.backends.contrib.orkut.FoursquareBackend',
    #'social_auth.backends.OpenIDBackend',
    #'django.contrib.auth.backends.ModelBackend',
)
        
# ----------------------------------------------------------------------
# Social auth

SOCIAL_AUTH_IMPORT_BACKENDS = (
)

LOGIN_URL = '/login-form/'
LOGIN_REDIRECT_URL = '/logged-in/'
LOGIN_ERROR_URL = '/login-error/'

SOCIAL_AUTH_ERROR_KEY = 'social_errors'

SOCIAL_AUTH_COMPLETE_URL_NAME = 'complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'associate_complete'
SOCIAL_AUTH_DEFAULT_USERNAME = 'new_social_auth_user'

# Final user name will have a random UUID-generated suffix in case it's already
# taken.  The UUID token max length can be changed with the setting:
SOCIAL_AUTH_UUID_LENGTH = 16

# Backends will store extra values from response by default.  Set this to False
# to avoid such behavior:
SOACIAL_AUTH_EXTRA_DATA = False

# Session expiration time is a special value.  It is recommended to define:
SOCIAL_AUTH_EXPIRATION = 'expires'

# and use such setting name where times are returned.  The view that completes
# the login process will set session expiration time using this name if it is
# present, or 'expires' by default.  Expiration configuration can be disabled
# with setting:
# SOCIAL_AUTH_SESSION_EXPIRATION = False

# It's possible to disable user creationg by django-social-auth with:
# SOCIAL_AUTH_CREATE_USERS = False

# It is possible to associate multiple user accounts with a single email
# address as long as the rest of the user data is unique.  Set value as True to
# enable, otherwise set False to disable.  This behavior is disabled by default
# (False) unless specifically set:
# SOCIAL_AUTH_ASSOCIATE_BY_EMAIL: True

# ----------------------------------------------------------------------
# Facebook

FACEBOOK_APP_ID = '180519672002663'
FACEBOOK_API_SECRET = None  # configure in settings_local


