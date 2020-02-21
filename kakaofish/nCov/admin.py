from django.contrib import admin
from .models import *

admin.site.register(News)
admin.site.register(Board)



class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'registered_date',)

admin.site.register(Tag, TagAdmin)