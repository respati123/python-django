from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Album


class IndexViews(generic.ListView):
    template_name = 'music/index.html'

    def get_queryset(self):
        return Album.objects.all()


class DetailViews(generic.DetailView):
    model = Album
    template_name = 'music/detail.html'


class AlbumCreate(CreateView):
    template_name = 'music/parsing/album_form.html'
    model = Album
    fields =  ['artist', 'album_title', 'genre', 'album_logo', 'date']


