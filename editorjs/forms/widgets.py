from django.forms import Media
from django.forms.widgets import Textarea


ToolsSourceMap = {
    "header": "https://cdn.jsdelivr.net/npm/@editorjs/header@latest",
    "image": "https://cdn.jsdelivr.net/npm/@editorjs/image@latest",
}

DefaultJsSource = [
    "https://cdn.jsdelivr.net/npm/@editorjs/editorjs@latest",
    "editor/js/editor.js",
]


# Create your models here.
class EditorJSWidget(Textarea):
    tools = None
    # class Media:
    #     css = {"all": ["editor/css/editor.css"]}
    #     js = ["https://cdn.jsdelivr.net/npm/@editorjs/editorjs@latest", "js/editor.js"]

    def __init__(self, *args, **kwargs):
        self.tools = kwargs.pop("tools", None)
        attrs = None
        if self.tools:
            attrs = {"tools": self.tools}
        super().__init__(attrs, *args, **kwargs)

    @property
    def media(self):
        jsfiles = DefaultJsSource
        if self.tools:
            for tool in self.tools:
                if bool(tool) and tool in ToolsSourceMap:
                    jsfiles.append(ToolsSourceMap[tool])
        return Media(css={"all": ["editor/css/editor.css"]}, js=jsfiles)

    template_name = "editor/forms/widgets/editorjs.html"
