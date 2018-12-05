from django.contrib import admin
from django.urls import path,include
from django.conf.urls import include, url
from main  import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^upload/', include(('upload_form.urls','upload_form'),)),
]
