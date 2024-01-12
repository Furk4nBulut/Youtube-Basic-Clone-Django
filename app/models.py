from django.db import models

class Users(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=255, unique=True)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

class Channel(models.Model):
    channel_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.ForeignKey(Users, on_delete=models.CASCADE)

class Video(models.Model):
    video_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    upload_date = models.DateTimeField(default=models.DateTimeField(auto_now=True), null=True)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    views = models.IntegerField(default=0, null=True)
    likes = models.IntegerField(default=0, null=True)
    dislikes = models.IntegerField(default=0, null=True)
    thumbnail = models.CharField(max_length=100, null=True)

class LikedList(models.Model):
    liked_list_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

class ChannelSubscription(models.Model):
    channel_subscription_id = models.AutoField(primary_key=True)
    subscriber = models.ForeignKey(Users, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)

class Like(models.Model):
    like_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

class Dislike(models.Model):
    dislike_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)

class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(default=models.DateTimeField(auto_now=True), null=True)

class TopVideos(models.Model):
    top_videos_id = models.AutoField(primary_key=True)
    video = models.OneToOneField(Video, on_delete=models.CASCADE, unique=True)
    views = models.IntegerField(default=0, null=True)

class History(models.Model):
    history_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    watched_date = models.DateTimeField(default=models.DateTimeField(auto_now=True), null=True)

class Premium(models.Model):
    premium_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(Users, on_delete=models.CASCADE, unique=True)
    subscription_end_date = models.DateTimeField()

class Playlist(models.Model):
    playlist_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class PlaylistVideo(models.Model):
    playlist_video_id = models.AutoField(primary_key=True)
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    video_order = models.IntegerField()

class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(default=models.DateTimeField(auto_now=True), null=True)
