import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from base.models import TimestampedModel, UUIDModel
from editorjs.models import EditorJSField


# Create your models here.
class Content(UUIDModel, TimestampedModel):
    class Meta:
        db_table = "contents"

    title = models.CharField(max_length=200)
    creator = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    price = models.IntegerField(null=True)
    raw_data = EditorJSField(null=True, blank=True, tools={"header": "Header"})

    def __str__(self):
        return self.title
    def get_absolute_url(self): # new
        return reverse("content_detail", args=[str(self.uuid)])


class Review(models.Model):
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name="reviews")
    review = models.CharField(max_length=1000)
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.review
