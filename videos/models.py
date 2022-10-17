from django.db import models


class Video(models.Model):
    title = models.TextField(max_length=40)
    video = models.URLField()

    cheating = models.IntegerField(default='0')
    not_cheating = models.IntegerField(default='0')

    class Meta:
        ordering = ('-id',)


class Vote(models.Model):
    video = models.ForeignKey(Video, related_name='videoid',
                             on_delete=models.CASCADE, default=None, blank=True)


