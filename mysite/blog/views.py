from django.shortcuts import render
from django.views import generic
from .models import post

# Create your views here.
class postlist(generic.ListView):
    queryset  = post.objects.filter(status=1).order_by('-created_on')
    template_name  = 'index.html'

class postdetail(generic.DeleteView):
    model  = post 
    template_name = 'post_detail.html'
