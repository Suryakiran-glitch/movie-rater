from django.urls import path , include
from rest_framework import routers
from .views import RatingViewset,VideoViewset

router = routers.DefaultRouter()
router.register('video' , VideoViewset , 'video')
router.register('rating' , RatingViewset , 'rating')

urlpatterns = [
    path('' , include(router.urls) )
]
