from django.db import models
from . import forms


class EditorJSField(models.JSONField):
    tools = None

    def __init__(self, *args, **kwargs):
        self.tools = kwargs.pop("tools", None)
        super().__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        return super().formfield(
            **{
                "form_class": forms.EditorJSField,
                "encoder": self.encoder,
                "decoder": self.decoder,
                "widget": forms.EditorJSWidget(tools=self.tools),
                **kwargs,
            }
        )
