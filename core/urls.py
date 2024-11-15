from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView, GenereRetrieveUpdateDestroyView
from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView

urlpatterns = [
    # admin routes
    path("admin/", admin.site.urls),
    # genre routes
    path("genres/", GenreCreateListView.as_view(), name="genre-create-list"),
    path(
        "genres/<int:pk>",
        GenereRetrieveUpdateDestroyView.as_view(),
        name="genre-detail-view",
    ),
    # actor routes
    path("actors/", ActorCreateListView.as_view(), name="actor-create-list"),
    path(
        "actors/<int:pk>",
        ActorRetrieveUpdateDestroyView.as_view(),
        name="actor-detail-view",
    ),
    # movies routes
    path("movies/", MovieCreateListView.as_view(), name="movie-create-list"),
    path(
        "movies/<int:pk>",
        MovieRetrieveUpdateDestroyView.as_view(),
        name="movie-detail-view",
    ),
]
