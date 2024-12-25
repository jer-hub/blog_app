from django import forms
from .models import Post
from django_ckeditor_5.widgets import CKEditor5Widget

class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["title"].widget.attrs.update({"class": "form-control"})
        self.fields["description"].widget.attrs.update({"class": "form-control"})

    title = forms.CharField(label="Title", max_length=200)
    image = forms.ImageField(label="Upload your thumbnail here")
    description = forms.CharField(label="Description", max_length=500)
    content = forms.CharField(
        widget=CKEditor5Widget(
            attrs={"class": "django_ckeditor_5"}, config_name="extends"
        ),
        label="Text",
    )

    class Meta:
        model = Post
        fields = ["title", "content", "description", "image"]
        labels = {"title": "Title", "content": "Text"}
