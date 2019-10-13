from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    
    url(r'^$',views.image_display,name='images'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^image/(\d+)',views.image,name ='image')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)