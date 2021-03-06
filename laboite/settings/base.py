import os


PACKAGE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
PROJECT_ROOT = os.path.abspath(os.path.join(PACKAGE_ROOT, os.pardir))
BASE_DIR = PACKAGE_ROOT

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "dev.db",
    }
}

ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = "Europe/Paris"

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = "fr-FR"

SITE_ID = int(os.environ.get("SITE_ID", 1))

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = os.path.join(PACKAGE_ROOT, "site_media", "media")

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = "/site_media/media/"

# Absolute path to the directory static files should be collected to.
# Don"t put anything in this directory yourself; store your static files
# in apps" "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(PACKAGE_ROOT, "site_media", "static")

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = "/site_media/static/"

# Additional locations of static files
STATICFILES_DIRS = [
    os.path.join(PROJECT_ROOT, "static", "dist"),
    os.path.join(PROJECT_ROOT, "laboite", "static"),
]

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

# Make this unique, and don't share it with anybody.
SECRET_KEY = "sxy3vh^sl1u+rsvj&=$kh(5=eal0cme7u1@i^5chr^j@jc-hfj"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(PACKAGE_ROOT, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "debug": DEBUG,
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.template.context_processors.request",
                "django.contrib.messages.context_processors.messages",
                "account.context_processors.account",
                "pinax_theme_bootstrap.context_processors.theme",
                "social.apps.django_app.context_processors.backends",
                "social.apps.django_app.context_processors.login_redirect",
            ],
        },
    },
]

MIDDLEWARE = [
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.auth.middleware.SessionAuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "laboite.urls"

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = "laboite.wsgi.application"

LABOITE_APPS = [
    "laboite.apps.airquality",
    "laboite.apps.bikes",
    "laboite.apps.bitmap",
    "laboite.apps.bus",
    "laboite.apps.calendar",
    "laboite.apps.coffees",
    "laboite.apps.cryptocurrency",
    "laboite.apps.data",
    "laboite.apps.energy",
    "laboite.apps.likes",
    "laboite.apps.luftdaten",
    "laboite.apps.messages",
    "laboite.apps.metro",
    "laboite.apps.parcel",
    "laboite.apps.parking",
    "laboite.apps.tasks",
    "laboite.apps.time",
    "laboite.apps.traffic",
    "laboite.apps.weather",
    "laboite.apps.wifi",
]

INSTALLED_APPS = [
    'dal',
    'dal_select2',
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "django.contrib.humanize",

    # theme
    "bootstrapform",
    "pinax_theme_bootstrap",

    # external
    "account",
    "pinax.eventlog",
    "pinax.webanalytics",
    "social.apps.django_app.default",
    "django_gravatar",

    # project
    "laboite",
    "boites"
] + LABOITE_APPS

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "filters": {
        "require_debug_false": {
            "()": "django.utils.log.RequireDebugFalse"
        }
    },
    "handlers": {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler'
        },
        "mail_admins": {
            "level": "ERROR",
            "filters": ["require_debug_false"],
            "class": "django.utils.log.AdminEmailHandler"
        }
    },
    "loggers": {
        'laboite.apps': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True
        },
        "django.request": {
            "handlers": ["mail_admins"],
            "level": "ERROR",
            "propagate": True,
        },
    }
}

FIXTURE_DIRS = [
    os.path.join(PROJECT_ROOT, "fixtures"),
]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

ACCOUNT_OPEN_SIGNUP = True
ACCOUNT_EMAIL_UNIQUE = True
ACCOUNT_EMAIL_CONFIRMATION_REQUIRED = False
ACCOUNT_LOGIN_REDIRECT_URL = LOGIN_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_REDIRECT_URL = "home"
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 2
ACCOUNT_USE_AUTH_AUTHENTICATE = True
LOGIN_URL = '/account/login/'

AUTHENTICATION_BACKENDS = [
    "social.backends.twitter.TwitterOAuth",
    "account.auth_backends.UsernameAuthenticationBackend",
]

SOCIAL_AUTH_TWITTER_KEY = ""
SOCIAL_AUTH_TWITTER_SECRET = ""

# Apps settings
# Bikes
STAR_API_BASE_URL = 'https://data.explore.star.fr/api/records/1.0/search'
STAR_API_KEY = ''
VELIB_API_BASE_URL = 'http://opendata.paris.fr/api/records/1.0/search'
VELIB_API_KEY = ''

# Likes
FACEBOOK_ACCESS_TOKEN = ''

# Traffic
GOOGLE_MAPS_API_KEY = ''
GOOGLE_MAPS_BASE_URL = 'https://maps.googleapis.com/maps/api/directions/json'

# Weather
OWM_APIKEY = ''

# Airquality
AIRBZH_URL = 'http://data.airbreizh.asso.fr/geoserver/airbreizh_ind_bretagne/ows?service=WFS&version=1.0.0&request=GetFeature&typeName=airbreizh_ind_bretagne:airbreizh_ind_prevision_bretagne&outputFormat=application%2Fjson'
LUFTDATEN_URL = 'https://data.sensor.community/airrohr/v1/sensor/'

# IFTT
IFTTT_API_BASE_URL = 'https://maker.ifttt.com/trigger/'

# Cryptocurrency
BLOCKCHAIN_BASE_URL = 'https://blockchain.info/ticker'
