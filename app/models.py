from django.db import models


class Users(models.Model):
    username = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username


class Channel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    owner = models.OneToOneField(Users, on_delete=models.CASCADE, related_name='channel')


class Video(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    upload_date = models.DateTimeField(auto_now_add=True)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='videos')
    views = models.PositiveIntegerField(default=0)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, null=True)


class LikedList(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)


class ChannelSubscription(models.Model):
    subscriber = models.ForeignKey(Users, on_delete=models.CASCADE)
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE, related_name='subscribers')


class Like(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)


class Dislike(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)


class Comment(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)


class TopVideos(models.Model):
    video = models.OneToOneField(Video, on_delete=models.CASCADE)
    views = models.PositiveIntegerField(default=0)

    @staticmethod
    def top_videos(limit=10):
        return TopVideos.objects.order_by('-views')[:limit]


class History(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    watched_date = models.DateTimeField(auto_now_add=True)


class Premium(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE)
    subscription_end_date = models.DateTimeField()


class Playlist(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    videos = models.ManyToManyField(Video, through='PlaylistVideo')


class PlaylistVideo(models.Model):
    playlist = models.ForeignKey(Playlist, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    order = models.PositiveIntegerField()


class Post(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.pub_date}"
