"""slavanka URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from main.views import HomeView
from events.views import *
from tours.views import *
from tours.models import Tour, Article
from events.models import Event
from base.views import TestView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('events/<int:id>/', EventDetailsView.as_view(), name=Event.url_name),
    path('tours/<int:id>/', ToursDetailsView.as_view(), name=Tour.url_name),
    path('articles/<int:id>/', ArticleDetailsView.as_view(), name=Article.url_name),
    path('events/', EventListView.as_view(), name='event_list'),
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('tours/', ToursListView.as_view(), name='tour_list'),
    path('admin/', admin.site.urls),
    path('test/<int:id>/', TestView.as_view(), name='test')
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
