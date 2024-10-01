"""
Django settings for ecom_prj project.

Generated by 'django-admin startproject' using Django 4.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
from datetime import timedelta
from environs import Env
import os
from django.contrib import messages
import dj_database_url


env = Env()  
env.read_env()  

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&)0dbnucsu)$f4pgxd0ombb4)b+oj2ci9mi=yno-veu%^doqh!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#ALLOWED_HOSTS = ['.railway.app','*']
ALLOWED_HOSTS = ['*']
CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1', 'https://*.ngrok-free.app', 'https://fastcart.up.railway.app']
SECURE_CROSS_ORIGIN_OPENER_POLICY = 'same-origin-allow-popups'

# Application definition
INSTALLED_APPS = [
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.staticfiles',

    'userauths',
    'store',
    'vendor',
    'customer',
    'blog',

    'django_ckeditor_5',
    'anymail',
    'captcha',
    'django_extensions'

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecom_prj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'store.context.default',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ecom_prj.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }

   # 'default': dj_database_url.config(conn_max_age=600)
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/



STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles' #sunt comentate pentru railway le decomentez si comentez mai jos pentru local

#STATIC_URL = '/static/'
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
#si asta de jos trebuie comentata
#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

AUTH_USER_MODEL = 'userauths.User'


# Stripe API Keys 
#STRIPE_PUBLIC_KEY = env("STRIPE_PUBLIC_KEY")
#STRIPE_SECRET_KEY = env("STRIPE_SECRET_KEY")
STRIPE_SECRET_KEY = os.getenv('STRIPE_SECRET_KEY')
STRIPE_PUBLIC_KEY = os.getenv('STRIPE_PUBLIC_KEY')

# Paypal API Keys 
#PAYPAL_CLIENT_ID = env('PAYPAL_CLIENT_ID')
#PAYPAL_SECRET_ID = env('PAYPAL_SECRET_ID')

# Flutterwave Keys
#FLUTTERWAVE_PUBLIC_KEY=env("FLUTTERWAVE_PUBLIC_KEY")
#FLUTTERWAVE_PRIVATE_KEY=env("FLUTTERWAVE_PRIVATE_KEY")

# Paystack Keys
#PAYSTACK_PUBLIC_KEY=env("PAYSTACK_PUBLIC_KEY")
#PAYSTACK_PRIVATE_KEY=env("PAYSTACK_PRIVATE_KEY")

# Razorpay keys
#RAZORPAY_KEY_ID=env("RAZORPAY_KEY_ID")
#RAZORPAY_KEY_SECRET=env("RAZORPAY_KEY_SECRET")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

FROM_EMAIL=env("FROM_EMAIL")
EMAIL_BACKEND=env("EMAIL_BACKEND")
DEFAULT_FROM_EMAIL=env("DEFAULT_FROM_EMAIL")
SERVER_EMAIL=env("SERVER_EMAIL")

ANYMAIL = {
    "MAILGUN_API_KEY": os.environ.get("MAILGUN_API_KEY"),
    "MAILGUN_SENDER_DOMAIN": os.environ.get("MAILGUN_SENDER_DOMAIN"),
}

MESSAGE_TAGS = {
    messages.ERROR: 'danger',
}

GRAPH_MODELS ={
    'all_applications': True,
    'graph_models': True,
}

LOGIN_URL = "userauths:sign-in"
LOGIN_REDIRECT_URL = ""
LOGOUT_REDIRECT_URL = "userauths:sign-in"

RECAPTCHA_PUBLIC_KEY = env("DJANGO_RECAPTCHA_PUBLIC_KEY")
RECAPTCHA_PRIVATE_KEY = env("DJANGO_RECAPTCHA_PRIVATE_KEY")

# Custom Admin Settings
JAZZMIN_SETTINGS = {
    "site_title": "FastCart Ecommerce",
    "site_header": "FastCart Ecommerce",
    "site_brand": "FastCart Ecommerce ",
    # "site_icon": "images/favicon.ico",
    # "site_logo": "images/logos/logo.jpg",
    "welcome_sign": "Welcome To Desphixs",
    "copyright": "Desphixs",
    "user_avatar": "images/photos/logo.jpg",
    "show_sidebar": True,
    "navigation_expanded": True,
    "order_with_respect_to": [
        "store",
        "store.product",
        "store.cartorder",
        "store.cartorderitem",
        "store.cart",
        "store.category",
        "store.brand",
        "store.productfaq",
        "store.review",
        "vendor.Coupon",
        "vendor.DeliveryCouriers",
        "userauths",
        "userauths.user",
        "userauths.profile",
        "donations",
        "blog",
        'newsfeed',
        "contacts",
        "addon",
    ],
    "icons": {
        "admin.LogEntry": "fas fa-file",

        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",

        "userauths.User": "fas fa-user",
        "userauths.Profile":"fas fa-address-card",

        "donations.Donation": "fas fa-hand-holding-usd",
        "donations.Payment": "fas fa-credit-card",

        "newsfeed.Newsletter": "fas fa-envelope",
        "newsfeed.SubscribedUser": "fas fa-at",

        "newsfeed.SubscribedUser": "fas fa-at",

        "contacts.Inquiry": "fas fa-phone",
        "addon.BasicAddon": "fas fa-cog",

        "store.Product": "fas fa-th",
        "store.CartOrder":"fas fa-shopping-cart",
        "store.Cart":"fas fa-cart-plus",
        "store.CartOrderItem":"fas fa-shopping-basket",
        "store.Brand":"fas fa-check-circle",
        "store.productfaq":"fas fa-question",
        "store.Review":"fas fa-star fa-beat",
        "store.Category":"fas fa-tag",
        "store.Tag":"fas fa-tag",
        "store.Notification":"fas fa-bell",
        
        "customer.Address":"fas fa-location-arrow",
        "customer.Wishlist":"fas fa-heart",

        "vendor.DeliveryCouriers":"fas fa-truck",
        "vendor.Coupon":"fas fa-percentage",
        "vendor.Vendor":"fas fa-store",
        "vendor.Notification":"fas fa-bell",
        "vendor.PayoutTracker":"fas fa-wallet",
        "vendor.ChatMessage":"fas fa-envelope",

        "addons.BecomeAVendor":"fas fa-user-plus",
        "addons.AboutUS":"fas fa-users",
        "addons.Company":"fas fa-university",
        "addons.BasicAddon":"fas fa-cog",
    },
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-arrow-circle-right",
    "related_modal_active": False,
    
    "custom_js": None,
    "show_ui_builder": True,
    
    "changeform_format": "horizontal_tabs",
    "changeform_format_overrides": {
        "auth.user": "collapsible",
        "auth.group": "vertical_tabs",
    },
}


customColorPalette = [
    {"color": "hsl(4, 90%, 58%)", "label": "Red"},
    {"color": "hsl(340, 82%, 52%)", "label": "Pink"},
    {"color": "hsl(291, 64%, 42%)", "label": "Purple"},
    {"color": "hsl(262, 52%, 47%)", "label": "Deep Purple"},
    {"color": "hsl(231, 48%, 48%)", "label": "Indigo"},
    {"color": "hsl(207, 90%, 54%)", "label": "Blue"},
]

CKEDITOR_5_CONFIGS = {
    "default": {
        "toolbar": [
            "heading",
            "|",
            "bold",
            "italic",
            "link",
            "bulletedList",
            "numberedList",
            "blockQuote",
            "imageUpload"
        ],
    },
    "comment": {
        "language": {"ui": "en", "content": "en"},
        "toolbar": [
            "heading",
            "|",
            "bold",
            "italic",
            "link",
            "bulletedList",
            "numberedList",
            "blockQuote",
        ],
    },
    "extends": {
        "language": "en",
        "blockToolbar": [
            "paragraph",
            "heading1",
            "heading2",
            "heading3",
            "|",
            "bulletedList",
            "numberedList",
            "|",
            "blockQuote",
        ],
        "toolbar": [
            # "heading",
            # "codeBlock",
            # "|",
            # "outdent",
            # "indent",
            # "|",
            "bold",
            "italic",
            "underline",
            "|",
            "link",
            "strikethrough",
            "code",
            "subscript",
            "superscript",
            "highlight",
            "|",
            "bulletedList",
            "numberedList",
            "todoList",
            "|",
            "blockQuote",
            "insertImage",
            "|",
            "fontSize",
            "fontFamily",
            "fontColor",
            "fontBackgroundColor",
            "mediaEmbed",
            "removeFormat",
            "insertTable",
            "sourceEditing",
        ],
        "image": {
            "toolbar": [
                "imageTextAlternative",
                "|",
                "imageStyle:alignLeft",
                "imageStyle:alignRight",
                "imageStyle:alignCenter",
                "imageStyle:side",
                "|",
                "toggleImageCaption",
                "|"
            ],
            "styles": [
                "full",
                "side",
                "alignLeft",
                "alignRight",
                "alignCenter",
            ],
        },
        "table": {
            "contentToolbar": [
                "tableColumn",
                "tableRow",
                "mergeTableCells",
                "tableProperties",
                "tableCellProperties",
            ],
            "tableProperties": {
                "borderColors": customColorPalette,
                "backgroundColors": customColorPalette,
            },
            "tableCellProperties": {
                "borderColors": customColorPalette,
                "backgroundColors": customColorPalette,
            },
        },
        "heading": {
            "options": [
                {
                    "model": "paragraph",
                    "title": "Paragraph",
                    "class": "ck-heading_paragraph",
                },
                {
                    "model": "heading1",
                    "view": "h1",
                    "title": "Heading 1",
                    "class": "ck-heading_heading1",
                },
                {
                    "model": "heading2",
                    "view": "h2",
                    "title": "Heading 2",
                    "class": "ck-heading_heading2",
                },
                {
                    "model": "heading3",
                    "view": "h3",
                    "title": "Heading 3",
                    "class": "ck-heading_heading3",
                },
            ]
        },
        "list": {
            "properties": {
                "styles": True,
                "startIndex": True,
                "reversed": True,
            }
        },
        "htmlSupport": {
            "allow": [
                {"name": "/.*/", "attributes": True, "classes": True, "styles": True}
            ]
        },
    },
}