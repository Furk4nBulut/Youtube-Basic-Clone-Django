from django.contrib import admin
from .models import Users, Channel, Video, LikedList, ChannelSubscription, Like, Dislike, Comment, TopVideos

# Register your models here.

admin.site.register(Users)
admin.site.register(Channel)
admin.site.register(Video)
admin.site.register(LikedList)
admin.site.register(ChannelSubscription)
admin.site.register(Like)
admin.site.register(Dislike)
admin.site.register(Comment)
admin.site.register(TopVideos)

class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'full_name', 'email', 'password')
    search_fields = ('username', 'full_name', 'email', 'password')
    list_filter = ('username', 'full_name', 'email', 'password')
    ordering = ('username', 'full_name', 'email', 'password')
    filter_horizontal = ()
    fieldsets = ()
class ChannelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'owner')
    search_fields = ('name', 'description', 'owner')
    list_filter = ('name', 'description', 'owner')
    ordering = ('name', 'description', 'owner')
    filter_horizontal = ()
    fieldsets = ()
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'upload_date', 'channel', 'views', 'likes', 'dislikes', 'thumbnail')
    search_fields = ('title', 'description', 'upload_date', 'channel', 'views', 'likes', 'dislikes', 'thumbnail')
    list_filter = ('title', 'description', 'upload_date', 'channel', 'views', 'likes', 'dislikes', 'thumbnail')
    ordering = ('title', 'description', 'upload_date', 'channel', 'views', 'likes', 'dislikes', 'thumbnail')
    filter_horizontal = ()
    fieldsets = ()
class LikedListAdmin(admin.ModelAdmin):
    list_display = ('user', 'video')
    search_fields = ('user', 'video')
    list_filter = ('user', 'video')
    ordering = ('user', 'video')
    filter_horizontal = ()
    fieldsets = ()
class ChannelSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('subscriber', 'channel')
    search_fields = ('subscriber', 'channel')
    list_filter = ('subscriber', 'channel')
    ordering = ('subscriber', 'channel')
    filter_horizontal = ()
    fieldsets = ()
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'video')
    search_fields = ('user', 'video')
    list_filter = ('user', 'video')
    ordering = ('user', 'video')
    filter_horizontal = ()
    fieldsets = ()
class DislikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'video')
    search_fields = ('user', 'video')
    list_filter = ('user', 'video')
    ordering = ('user', 'video')
    filter_horizontal = ()
    fieldsets = ()
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'video', 'text', 'pub_date')
    search_fields = ('user', 'video', 'text', 'pub_date')
    list_filter = ('user', 'video', 'text', 'pub_date')
    ordering = ('user', 'video', 'text', 'pub_date')
    filter_horizontal = ()
    fieldsets = ()
class TopVideosAdmin(admin.ModelAdmin):
    list_display = ('video', 'views')
    search_fields = ('video', 'views')
    list_filter = ('video', 'views')
    ordering = ('video', 'views')
    filter_horizontal = ()
    fieldsets = ()
