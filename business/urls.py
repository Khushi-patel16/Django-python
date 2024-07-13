from django.contrib import admin
from django.urls import include, path
from blog.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('inner-page/', innerpage, name='innerpage'),
    #path('portfolio_detail/', port_data, name='portfolio_detail'),
    path('portfolio_detail/<int:pk>/', port_data, name='portfolio_detail'),
    path('about/', about, name='about'),
    path('services/', services, name='services'),
    path('portfolio/', port, name='port'),
    path('contact/', contact, name='contact'),
    path('calculator/', calculator, name='calculator'),
    path('even/', even, name='even'),
    path('team/', team, name='team'),
    path('marksheet/', mark, name='mark'),
    path('subscribe/', subscribe, name='subscribe'),
    path('newsdetails/<slug>', news, name='news'),
    path('services/<slug>/', service_detail, name='service_detail'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
