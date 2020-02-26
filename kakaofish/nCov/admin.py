from django.contrib import admin
from .models import *

admin.site.register(News)
# class TagAdmin(admin.ModelAdmin):
#     list_display = ('name', 'registered_date',)

# admin.site.register(Tag, TagAdmin)
# admin.site.register(Board)
