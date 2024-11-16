from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView, GenereRetrieveUpdateDestroyView
from actors.views import ActorCreateListView, ActorRetrieveUpdateDestroyView
from movies.views import MovieCreateListView, MovieRetrieveUpdateDestroyView
from reviews.views import ReviewCreateListView, ReviewRetrieveUpdateDestroyView

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
    # reviews routes
    path("reviews/", ReviewCreateListView.as_view(), name="review-create-list"),
    path(
        "reviews/<int:pk>", ReviewRetrieveUpdateDestroyView.as_view(), name="review-detail-view"
    ),
]
