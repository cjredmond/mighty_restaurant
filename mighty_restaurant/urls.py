from django.conf.urls import url, include
from django.contrib import admin
from utility.views import UserCreateView, ProfileUpdateView, IndexView # FoodCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('django.contrib.auth.urls')),
    url(r'^create_user/$', UserCreateView.as_view(), name='user_create_view'),
    url(r'^accounts/profile/$', ProfileUpdateView.as_view(), name='profile_view'),
    url(r'^$', IndexView, name="index_view"),
    #url(r'^food/create/$', FoodCreateView.as_view(), name='food_create_view')
]
