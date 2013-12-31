from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
#from django.contrib import admin
#admin.autodiscover()

urlpatterns = patterns('',
    url(r'^thermometers/?$', "django_thermometer.views.list_thermometers", name="list_thermometers"),
    url(r'^thermometer/(\w+)$', "django_thermometer.views.thermometer", name="thermometer"),
)
