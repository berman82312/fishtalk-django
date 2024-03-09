import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from base.models import TimestampedModel
from editorjs.models import EditorJSField


User = get_user_model()


# Create your models here.
class Content(TimestampedModel):
    class Meta:
        db_table = "contents"

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    creator = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    price = models.IntegerField(null=True)
    raw_data = EditorJSField(null=True, blank=True, tools={"header": "Header"})

    def __str__(self):
        return self.title

    def get_absolute_url(self): # new
        return reverse("content_detail", args=[str(self.id)])
