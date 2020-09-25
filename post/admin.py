from django.contrib import admin
from post.models import Post
# Register your models here.
from django.db import models
from django.conf import settings
from django.apps import apps
from django.contrib.auth import get_user_model
from django.core.signals import setting_changed
from django.dispatch import receiver

class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'content', 'up_file' , 'status','created_on')
    list_filter = ("status",)
    search_fields = ['author']

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'author':
            kwargs['queryset'] = get_user_model().objects.filter(username=request.user.username)
        return super(PostAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(Post, PostAdmin)