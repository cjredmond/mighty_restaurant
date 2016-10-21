from django.conf.urls import url, include
from django.contrib import admin
from utility.views import UserCreateView, ProfileUpdateView, IndexView, FoodCreateView, \
                          FoodListView, ServerView, OrderUpdateView, CookView, OrderCreateView, \
                          ServerView, TableDetailView, OrderDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^create_user/$', UserCreateView.as_view(), name='user_create_view'),
    url(r'^accounts/profile/$', ProfileUpdateView.as_view(), name='profile_view'),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^food/create/$', FoodCreateView.as_view(), name='food_create_view'),
    url(r'^food/list/$', FoodListView.as_view(), name='food_list_view'),
    url(r'^server/$', ServerView.as_view(), name='server_view'),
    url(r'^order/(?P<pk>\d+)/update$', OrderUpdateView.as_view(), name='order_update_view'),
    url(r'^cook/$', CookView.as_view(), name='cook_view'),
    url(r'^table/(?P<pk>\d+)/$', TableDetailView.as_view(), name='table_detail_view'),
    url(r'^order/(?P<pk>\d+)/create/$', OrderCreateView.as_view(), name='order_create_view'),
    url(r'^order/(?P<pk>\d+)/$', OrderDetailView.as_view(), name='order_detail_view'),
]
