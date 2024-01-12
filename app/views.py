from django.shortcuts import render
from .models import Users, Channel, Video, LikedList, ChannelSubscription, Like, Dislike, Comment, TopVideos, History

def home(request):
    # Get some sample data from your models
    channels = Channel.objects.all()
    videos = Video.objects.all()
    comments = Comment.objects.all()
    users = Users.objects.all()
    likes = Like.objects.all()
    dislikes = Dislike.objects.all()
    liked_lists = LikedList.objects.all()
    channel_subscriptions = ChannelSubscription.objects.all()
    top_videos = TopVideos.objects.all()
    history = History.objects.all()



    # Render the template with the sample data
    return render(request, 'home.html', {
        'users': users,
        'channels': channels,
        'videos': videos,
        'comments': comments,
        'likes': likes,
        'dislikes': dislikes,
        'liked_lists': liked_lists,
        'channel_subscriptions': channel_subscriptions,
        'top_videos': top_videos,
        'history': history,
    })
