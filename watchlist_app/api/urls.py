from django.urls import path, include
from watchlist_app.api.views import movies_list, movie_detail
urlpatterns = [
   path('list/',movies_list, name='movie-list'),
   path('<int:pk>',movie_detail, name='movie-detail'),
]
