from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # admin routes
    path("admin/", admin.site.urls),
    
    # authentication urls
    path("api/v1/", include("authentication.urls")),
    # actors urls
    path("api/v1/", include("actors.urls")),
    # genre routes
    path("api/v1/", include("genres.urls")),
    # movies routes
    path("api/v1/", include("movies.urls")),
    # reviews routes
    path("api/v1/", include("reviews.urls")),
    
]
