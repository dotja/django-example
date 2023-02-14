# Django examples

A Django project with example apps.

This repo will be updated when new apps are added to it.

The current list of apps include:

1. app_users
An app to demonstrate using a custom user model in Django.

2. user_payment
An app to receive user payments through Stripe.

3. edit_photo
An app that converts JPEG images into sketch using Celery.


## Running this project

* start by installing the requirements:

```
pip install --upgrade pip
pip install -r requirements.txt
```

* the following environment variables need to be exported prior to use:

```
export SECRET_KEY='your django secret key'
export STRIPE_PUBLIC_KEY_TEST='pk_test_12345...'
export STRIPE_SECRET_KEY_TEST='sk_test_12345...'
export STRIPE_WEBHOOK_SECRET_TEST='whsec_12345..'
export PRODUCT_PRICE='price_12345...'
```

* to run the photo editing app you need to have rabbitmq and a Celery worker running as follows:

```
## run the rabbitmq docker container
docker run -d -p 5672:5672 rabbitmq

## start the Celery worker
cd django-example
celery -A django_examples worker --loglevel=INFO
```

* after that you can run the following:

```
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```