from django.conf.urls import url, include
from django.contrib import admin
from main.views import IndexView, UserCreateView, ProfileDetailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name='index_view'),
    url(r'^new_user/$', UserCreateView.as_view(), name='user_create_view'),
    url(r'^accounts/profile/(?P<pk>\d+)/$', ProfileDetailView.as_view(), name='profile_detail_view'),

]
