from django.contrib import admin

from .models import Posts, Users

# Register your models here.

#class PostAdmin(admin.ModelAdmin):
#    list_display = ("id", "title", "post")

admin.site.register(Posts)
admin.site.register(Users)