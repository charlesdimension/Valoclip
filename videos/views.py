from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Video, Vote
from django.urls import reverse
from django.db.models import F
from django.http import JsonResponse


class HomePageView(ListView):
    model = Video
    template_name = 'home.html'


class UploadClipView(CreateView):
    model = Video
    fields = ['title', 'video', ]
    template_name = 'upload_clip.html'

    def get_success_url(self):
        return reverse('home')


def thumbs(request):

    if request.POST.get('action') == 'thumbs':
        id = int(request.POST.get('videoid'))
        button = request.POST.get('button')
        update = Video.objects.get(id=id)

        if button == 'thumbsup':
            update.cheating = F('thumbsup') + 1
            update.save()

            new = Vote(post_id=id, vote=True)
            new.save()
        else:
            update.not_cheating = F('thumbsdown') + 1
            update.save()

            new = Vote(post_id=id, vote=False)
            new.save()

        update.refresh_from_db()
        up = update.cheating
        down = update.not_cheating

        return JsonResponse({'cheating': up, 'clean': down})


