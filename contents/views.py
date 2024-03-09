from django.views.generic import ListView, DetailView

from .models import Content


class ContentListView(ListView):
    model = Content
    context_object_name = 'content_list'
    template_name = "contents/content_list.html"


class ContentDetailView(DetailView):
    model = Content
    context_object_name= "content"
    template_name = "contents/content_detail.html"
