from django.shortcuts import render
from rest_framework import viewsets
from .models import Video,Rating
from .serializers import VideoSerializer,RatingSerializer,UserSerializer
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication

# Create your views here.
class VideoViewset(viewsets.ModelViewSet):
 queryset = Video
 serializer_class = VideoSerializer
 authentication_class = TokenAuthentication
 permission_class = {AllowAny,}

 @action(methods = ['post'] , detail=True)
 def RateVideo(self,request , pk=None):
  if 'stars' in request.data:
   video = Video.objects.get(id=pk)
   stars = request.data['stars']
   comments = request.data['comments']
   user = request.user

   try:
    rating = Rating.objects.get(user=user.id , video=video.id)
    rating.stars = stars
    rating.comments = comments
    rating.save()

    serializer = RatingSerializer(rating , many=False)

    response =  {'message' : 'Rating has been updated' , 'data' : serializer.data}

    Response(response , status=status.HTTP_200_OK)

   except:
    rating = Rating.objects.create(user=user,comments=comments,stars=stars,video=video) 
    serializer = RatingSerializer(rating , many=False)
    response =  {'message' : 'Rating has been updated' , 'data' : serializer.data}
    Response(response , status=status.HTTP_200_OK)
  
  else:
   response =  {'message' : 'Rating can not be given without giving stars'}
   Response(response , status=status.HTTP_400_BAD_REQUEST)

class RatingViewset(viewsets.ModelViewSet):
 queryset = Rating
 serializer_class = Rating
 authentication_class = TokenAuthentication
 permission_class = {IsAuthenticated,}

 def delete(self,request,*args):
  response = 'This request cannot be made on ratings'
  Response(response , status.HTTP_100_CONTINUE)


class UserViewset(viewsets.ModelViewSet):
 queryset = User
 serializer_class = UserSerializer
 permission_class = {AllowAny,}  