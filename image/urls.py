from django.conf.urls import url
from . import views

urlpatterns=[
    
    url(r'^$',views.image_day,name='imageOfToday'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$',views.past_days_image,name = 'pastImage')
]