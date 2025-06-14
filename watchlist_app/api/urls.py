from django.urls import path, include
#from watchlist_app.api.views import movies_list, 
from watchlist_app.api.views import WatchListAV, WatchListDetailAV, StreamPlatformAV,StreamPlatformDetailAV

urlpatterns = [
   path('list/',WatchListAV.as_view(), name='watch-list'),
   path('<int:pk>',WatchListDetailAV.as_view(), name='watchlist-detail'),
   path('stream/',StreamPlatformAV.as_view(), name='stream-platform'),
   path('stream/<int:pk>',StreamPlatformDetailAV.as_view(), name='stream-platform-detail'),
]
