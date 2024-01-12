from django.db import models

class AppUsers(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class AppChannel(models.Model):
    channel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner_id = models.ForeignKey(AppUsers, on_delete=models.CASCADE)

class AppVideo(models.Model):
    video_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    upload_date = models.DateTimeField(default=models.DateTimeField)
    channel_id = models.ForeignKey(AppChannel, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    thumbnail = models.CharField(max_length=100, null=True)

class AppLikedList(models.Model):
    liked_list_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(AppUsers, on_delete=models.CASCADE)
    video_id = models.ForeignKey(AppVideo, on_delete=models.CASCADE)

class AppChannelSubscription(models.Model):
    channel_subscription_id = models.AutoField(primary_key=True)
    subscriber_id = models.ForeignKey(AppUsers, on_delete=models.CASCADE)
    channel_id = models.ForeignKey(AppChannel, on_delete=models.CASCADE)

class AppLike(models.Model):
    like_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(AppUsers, on_delete=models.CASCADE)
    video_id = models.ForeignKey(AppVideo, on_delete=models.CASCADE)

class AppDislike(models.Model):
    dislike_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(AppUsers, on_delete=models.CASCADE)
    video_id = models.ForeignKey(AppVideo, on_delete=models.CASCADE)

class AppComment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(AppUsers, on_delete=models.CASCADE)
    video_id = models.ForeignKey(AppVideo, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(default=models.DateTimeField)

class AppTopVideos(models.Model):
    top_videos_id = models.AutoField(primary_key=True)
    video_id = models.ForeignKey(AppVideo, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)

class AppHistory(models.Model):
    history_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(AppUsers, on_delete=models.CASCADE)
    video_id = models.ForeignKey(AppVideo, on_delete=models.CASCADE)
    watched_date = models.DateTimeField(default=models.DateTimeField)

class AppPremium(models.Model):
    premium_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(AppUsers, on_delete=models.CASCADE)
    subscription_end_date = models.DateTimeField()

class AppPlaylist(models.Model):
    playlist_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(AppUsers, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class AppPlaylistVideo(models.Model):
    playlist_video_id = models.AutoField(primary_key=True)
    playlist_id = models.ForeignKey(AppPlaylist, on_delete=models.CASCADE)
    video_id = models.ForeignKey(AppVideo, on_delete=models.CASCADE)
    video_order = models.IntegerField()

class AppPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(AppUsers, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(default=models.DateTimeField)
