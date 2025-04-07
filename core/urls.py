from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # admin routes
    path("admin/", admin.site.urls),
    
    # authentication urls
    path("api/v1/", include("authentication.urls")),
    # api routes 
    path("api/v1/", include("actors.urls")),
    path("api/v1/", include("genres.urls")),
    path("api/v1/", include("movies.urls")),
    path("api/v1/", include("reviews.urls")),
    
]
