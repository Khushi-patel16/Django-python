from django.contrib import admin
from news.models import *


# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display=('title', 'description')
admin.site.register(News,NewsAdmin)