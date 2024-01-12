from django.contrib import admin
from .models import (
    AppUsers,
    AppChannel,
    AppVideo,
    AppLikedList,
    AppChannelSubscription,
    AppLike,
    AppDislike,
    AppComment,
    AppTopVideos,
    AppHistory,
    AppPremium,
    AppPlaylist,
    AppPlaylistVideo,
    AppPost,
)

@admin.register(AppUsers)
class AppUsersAdmin(admin.ModelAdmin):
    list_display = ['user_id', 'username', 'full_name', 'email']

@admin.register(AppChannel)
class AppChannelAdmin(admin.ModelAdmin):
    list_display = ['channel_id', 'name', 'description', 'owner_id']

@admin.register(AppVideo)
class AppVideoAdmin(admin.ModelAdmin):
    list_display = ['video_id', 'title', 'channel_id', 'upload_date', 'views', 'likes', 'dislikes']

@admin.register(AppLikedList)
class AppLikedListAdmin(admin.ModelAdmin):
    list_display = ['liked_list_id', 'user_id', 'video_id']

@admin.register(AppChannelSubscription)
class AppChannelSubscriptionAdmin(admin.ModelAdmin):
    list_display = ['channel_subscription_id', 'subscriber_id', 'channel_id']

@admin.register(AppLike)
class AppLikeAdmin(admin.ModelAdmin):
    list_display = ['like_id', 'user_id', 'video_id']

@admin.register(AppDislike)
class AppDislikeAdmin(admin.ModelAdmin):
    list_display = ['dislike_id', 'user_id', 'video_id']

@admin.register(AppComment)
class AppCommentAdmin(admin.ModelAdmin):
    list_display = ['comment_id', 'user_id', 'video_id', 'text', 'pub_date']

@admin.register(AppTopVideos)
class AppTopVideosAdmin(admin.ModelAdmin):
    list_display = ['top_videos_id', 'video_id', 'views']

@admin.register(AppHistory)
class AppHistoryAdmin(admin.ModelAdmin):
    list_display = ['history_id', 'user_id', 'video_id', 'watched_date']

@admin.register(AppPremium)
class AppPremiumAdmin(admin.ModelAdmin):
    list_display = ['premium_id', 'user_id', 'subscription_end_date']

@admin.register(AppPlaylist)
class AppPlaylistAdmin(admin.ModelAdmin):
    list_display = ['playlist_id', 'user_id', 'name']

@admin.register(AppPlaylistVideo)
class AppPlaylistVideoAdmin(admin.ModelAdmin):
    list_display = ['playlist_video_id', 'playlist_id', 'video_id', 'video_order']

@admin.register(AppPost)
class AppPostAdmin(admin.ModelAdmin):
    list_display = ['post_id', 'user_id', 'text', 'pub_date']
