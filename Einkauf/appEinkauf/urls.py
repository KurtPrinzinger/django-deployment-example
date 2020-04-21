from django.conf.urls import url
from appEinkauf import views

# SET THE NAMESPACE!
app_name = 'appEinkauf'

urlpatterns=[
    url(r'^anzeigen/$',views.anzeigen,name='anzeigen'),
]
