from django.shortcuts import render
from index.models import *
# Create your views here.

def rankingView(request):
    search_log = Dynamic.objects.select_related('song').order_by('-dynamic_search').all()[:4]
    All_list = Song.objects.values('song_type').distinct()
    song_type = request.GET.get('type','')
    if song_type:
        song_info = Dynamic.objects.select_related('song').filter(song__song_type).order_by('-dynamic_plays').all()[:10]
    else:
        song_info = Dynamic.objects.select_related('song').order_by('-dynamic_plays').all()[:10]
    return render(request,'ranking.html',locals())

class RankingList(ListView):
    context_object_name = 'song_info'
    template_name = 'ranking.html'
    def get_queryset(self):
        song_type = self.request.GET.get('type','')
        if song_type:
            song_info = Dynamic.objects.select_related('song').filter(song__song_type).order_by('-dynamic_plays').all()[:10]
        else:
            song_info = Dynamic.objects.select_related('song').order_by('-dynamic_plays').all()[:10]
        return song_info

    def get_context_data(self, **kwargs):
        context = super.get_context_data(**kwargs)
        context['search_song'] = Dynamic.objects.select_related('song').order_by('-dynamic_search').all()[:4]
        context['All_list'] = Song.objects.values('song_type').distinct()
        return context