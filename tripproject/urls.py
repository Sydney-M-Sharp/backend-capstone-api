from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from tripapi.views import *

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'trips', TripView, 'trip')
router.register(r'invites', InviteView, 'invite')
router.register(r'events', EventView, 'event')
router.register(r'likes', LikeView, 'like')

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),

]

