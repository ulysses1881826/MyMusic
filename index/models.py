from django.db import models

# Create your models here.
class Label(models.Model):
    label_id = models.AutoField('sequence number',primary_key=True)
    label_name = models.CharField('class label',max_length=20)
    def __str__(self):
        return self.label_name
    class Meta:
        verbose_name = 'song classify'
        verbose_name_plural = 'song classifies'

class Song(models.Model):
    song_id = models.AutoField('sequence number',primary_key=True)
    song_name = models.CharField('song name', max_length=50)
    song_singer = models.CharField('player',max_length=50)
    song_time = models.CharField('duration',max_length=10)
    song_album = models.CharField('album',max_length=50)
    song_languages = models.CharField('language', max_length=20)
    song_type = models.CharField('type', max_length=20)
    song_release = models.CharField('issue time', max_length=20)
    song_img = models.CharField('song image', max_length=20)
    song_lyrics = models.CharField('lyrics', max_length=50,default='no lyrics now')
    song_file = models.CharField('song file', max_length=50)
    label = models.ForeignKey(Label, on_delete=models.CASCADE,verbose_name='song name classify')
    def __str__(self):
        return self.song_name
    class Meta:
        verbose_name = 'song info'
        verbose_name_plural = 'song infos'

class Dynamic(models.Model):
    dynamic_id = models.AutoField('sequence number',primary_key=True)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name='song name')
    dynamic_plays = models.IntegerField('play times')
    dynamic_search = models.IntegerField('search times')
    dynamic_down = models.IntegerField('download times')
    class Meta:
        verbose_name = 'song dynamic'
        verbose_name_plural = 'song dynamics'

class Comment(models.Model):
    comment_id = models.AutoField('sequence number', primary_key=True)
    comment_text = models.CharField('content', max_length=500)
    comment_user = models.CharField('user', max_length=30)
    song = models.ForeignKey(Song, on_delete=models.CASCADE, verbose_name='song name')
    comment_date = models.CharField('date', max_length=50)
    class Meta:
        verbose_name = 'song comment'
        verbose_name_plural = 'song comments'