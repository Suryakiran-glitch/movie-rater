from django.urls import path , include
from rest_framework import routers
from .views import RatingViewSet,VideoViewSet

router = routers.DefaultRouter()
router.register('video' , VideoViewSet , 'video')
router.register('rating' , RatingViewSet , 'rating')

urlpatterns = [
    path('' , include(router.urls) )
]
