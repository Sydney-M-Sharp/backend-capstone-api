from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from tripapi.views import *

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'trips', TripView, 'trip')
router.register(r'invites', InviteView, 'invite')
router.register(r'events', EventView, 'event')
router.register(r'likes', LikeView, 'like')
router.register(r'users', UserView, 'user')


urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('register', register_user),
    path('login', login_user),
    path('api-token-auth', obtain_auth_token),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework')),
    

]

