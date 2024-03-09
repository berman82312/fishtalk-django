from django.views.generic import ListView, DetailView

from .models import Content


class ContentListView(ListView):
    model = Content
    context_object_name = 'content_list'
    template_name = "contents/content_list.html"


class ContentDetailView(DetailView):
    model = Content
    slug_field = "uuid"
    slug_url_kwarg = "uuid"
    context_object_name= "content"
    template_name = "contents/content_detail.html"
