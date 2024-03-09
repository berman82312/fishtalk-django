from django.urls import path

from .views import ContentListView, ContentDetailView

urlpatterns = [
    path("", ContentListView.as_view(), name="content_list"),
    path("<uuid:pk>/", ContentDetailView.as_view(), name="content_detail"),
]
