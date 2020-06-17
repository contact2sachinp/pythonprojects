from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from base import views
from base.views import HomeView, TitanicView

app_name ='base'

urlpatterns=[
    url(r'^Register/$', views.register, name='register'),
    url(r'^user_login/$', views.user_login, name='user_login'),
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^titanic/$', TitanicView.as_view(), name='titanic'),
    ]