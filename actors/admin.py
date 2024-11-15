from django.contrib import admin
from actors.models import Actor


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('name', 'birthday', 'nationality')
    list_filter = ('birthday','nationality')
    search_fields = ('name','nationality')