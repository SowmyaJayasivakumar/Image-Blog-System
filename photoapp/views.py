from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Photo
# Create your views here.

class PhotoListView(ListView):
    model = Photo
    template_name = 'photoapp/list.html'
    context_object_name = 'photos'

class PhotoTagListView(PhotoListView):
    template_name ='photoapp/taglist.html'

    def get_tag(self):
        return self.kwargs.get('tag')
    def get_queryset(self):
        return self.model.objects.filter(tags__slug = self.get_tag())
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["tag"] = self.get_tag
        return context
    
class PhotoDetailView(DetailView):
    model = Photo
    template_name = 'photoapp/detail.html'
    context_object_name = 'photo'

class PhotoCreateView(LoginRequiredMixin,CreateView):
    model = Photo
    fields = ['title', 'description', 'image','tags']
    template_name = 'photoapp/create.html'
    success_url = reverse_lazy('photo:list')
    def form_valid(self, form):
        form.instance.submitter = self.request.user
        return super().form_valid(form)
    
class UserIsSubmitter(UserPassesTestMixin):
    def get_photo(self):
        return get_object_or_404(Photo,pk = self.kwargs.get('pk'))
    def test_func(self):
        if self.request.user.is_authenticated:
            return self.request.user == self.get_photo().submitter
        else:
            raise PermissionDenied("Sorry You cannot enter here.Please login")

class PhotoUpdateView(UserIsSubmitter,UpdateView):
    template_name = 'photoapp/update.html'
    model = Photo
    fields = ['title','description','tags']
    success_url = reverse_lazy('photo:list')

class PhotoDeleteView(UserIsSubmitter,DeleteView):
    model = Photo
    template_name = "photoapp/delete.html"
    success_url = reverse_lazy("photo:list")
