from django.forms import JSONField
from .widgets import EditorJSWidget


class EditorJSField(JSONField):
    widget = EditorJSWidget
