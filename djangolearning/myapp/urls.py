from django.conf.urls import url,include
from django.contrib import admin
import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # url(r'^$', views.platform, name='platform'),
    url(r'^$', views.login, name='login'),
]