from rest_framework.response import Response
from rest_framework.decorators import api_view
from watchlist_app.models import WatchList,StreamPlatform
from watchlist_app.api.serializers import WatchListSerializer,StreamPlatformSerializer
from rest_framework import generics
from rest_framework.views import APIView

class WatchListAV(APIView):
    def get(self, request, format=None):
        watchlist = WatchList.objects.all()
        serializer = WatchListSerializer(watchlist, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400) 
    
class WatchListDetailAV(APIView):
    
    def get_object(self, pk):
        try:
            return WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return None
        
    def get(self,request, pk):
        try:
            watchlist = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({'Error':'watchlist not found'},status=404)
        serializer = WatchListSerializer(watchlist)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        watchlist = self.get_object(pk)
        serializer = WatchListSerializer(watchlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk, format=None):
        watchlist = self.get_object(pk)
        watchlist.delete()
        return Response(status=204)
    
        
class StreamPlatformAV(APIView):
    def get(self, request, format=None):
        platforms = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platforms, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
    
class StreamPlatformDetailAV(APIView):
    def get_object(self, pk):
        try:
            return StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return None
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'Platform not found'},status=404)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)
    def put(self, request, pk, format=None):
        platform = self.get_object(pk)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    def delete(self, request, pk, format=None):
        platform = self.get_object(pk)
        platform.delete()
        return Response(status=204)
    
class StreamPlatformDetailAv(APIView):
    def get_object(self, pk):
        try:
            return StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return None
        
    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response({'Error':'Platform not found'},status=404)
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        platform = self.get_object(pk)
        serializer = StreamPlatformSerializer(platform, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)
    
    def delete(self, request, pk, format=None):
        platform = self.get_object(pk)
        platform.delete()
        return Response(status=204)
    




# @api_view(['GET','POST'])
# def movies_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         serializer = MovieSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=201)
#         return Response(serializer.errors, status=400)

# @api_view(['GET','PUT','DELETE'])
# def movie_detail(request, pk):
#     if request.method == 'GET':
#         try:
#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({'Error':'Movie not found'},status=404)
        
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)    
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=400)
        
#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=204)