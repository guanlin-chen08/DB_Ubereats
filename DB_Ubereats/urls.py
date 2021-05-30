"""DB_Ubereats URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from uber_eat import views, store, product, order
from uber_store.models import Photo
from django.contrib.auth.models import User
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('insert/', views.insert, name='insert'),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('uber_eat/', include('uber_eat.urls')),
                  path('uber_store/', include('uber_store.urls')),
                  path('uber_deliver/', include('uber_deliver.urls')),
                  path('', views.home, name='home'),
                  path('userinfo/', views.userinfo),
                  path('test/', views.test),

                  # ------------------------------------------------------

                  # path('del_store/', store.del_store, name='del_store'),
                  # path('del_store_post/', store.del_store_post, name='del_store_post'),
                  # path('del_deliver/', deliver.del_deliver, name='del_deliver'),
                  # path('del_deliver_post/', deliver.del_deliver_post, name='del_deliver_post'),

                  path('add_order/', order.add_order, name='add_order'),
                  path('add_order_post/', order.add_order_post, name='add_order_post'),
                  path('mod_Ostatus_post/', order.mod_Ostatus_post, name='mod_Ostatus_post'),
                  path('mod_Odeliver_post/', order.mod_Odeliver_post, name='mod_Odeliver_post'),
                  path('user_show_order/', views.user_show_order, name='user_show_order'),
                  path('deliver_show_order/', order.deliver_show_order, name='deliver_show_order'),

              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
