from django.conf import settings
from django.urls import reverse
from django.views.generic import ListView, UpdateView, DetailView, FormView, CreateView

from .forms import UEFieldForm, UEPostForm
from .models import UEPost

__all__ = (
    "UEPostListView",
    "UEPostCreateView",
    "UEPostDetailView",
    "UEPostUpdateView",
    "UEFieldFormView",
    "UEFieldFormHtmlInitialView",
    "UEFieldFormTextInitialView",
)

HTML_INITIAL = f"""
<h1><strong>django-ueditor-editor</strong></h1>
<br>
<p>django-ueditor-editor makes&nbsp;UE.js&nbsp;easy to use on Django Forms and admin sites</p>
<ul>
    <li><strong>No configuration required for static files!</strong></li>
    <li>The entire code for inserting WYSIWYG editor is less than 30 lines</li>
    <li>It can be used in both admin and Django views</li>
</ul>
<p>
<img src="{settings.TITLE_IMG}"></p>
<ul>
    <li><a href="https://django-ueditor-editor.readthedocs.io/en/latest/pages/using-in-admin.html" rel="noopener noreferrer" target="_blank" style="color: rgb(41, 128, 185);">Using in Django admin</a></li>
    <li><a href="https://django-ueditor-editor.readthedocs.io/en/latest/pages/using-as-form.html" rel="noopener noreferrer" target="_blank" style="color: rgb(41, 128, 185);">Using as Form</a></li>
    <li><a href="https://django-ueditor-editor.readthedocs.io/en/latest/pages/using-as-modelform.html" rel="noopener noreferrer" target="_blank" style="color: rgb(41, 128, 185);">Using as ModelForm</a></li>
    <li><a href="https://django-ueditor-editor.readthedocs.io/en/latest/pages/change-toolbar-configs.html" rel="noopener noreferrer" target="_blank" style="color: rgb(41, 128, 185);">Change toolbar config</a></li>
</ul>
<br>
<h2><strong>Installation</strong></h2>
<p>Use pip to install from PyPI:</p>
<pre class="ql-syntax" spellcheck="false">
    <span class="hljs-attribute">pip</span> install django-ueditor-editor
</pre>
<br>
<p>Add&nbsp;<strong>django_ueditor</strong>&nbsp;to&nbsp;<strong>INSTALLED_APPS</strong>&nbsp;in&nbsp;<strong>settings.py</strong>:</p>
<pre class="ql-syntax" spellcheck="false">
<span class="hljs-attr">INSTALLED_APPS</span> = [
    <span class="hljs-string">'django.contrib.admin'</span>,
    ...
    <span class="hljs-string">'django_ueditor'</span>,
]
</pre>
<br>
<h2><strong>Contributing</strong></h2>
<p>To contribute to&nbsp;<strong>django-ueditor-editor</strong>&nbsp;<a href="https://github.com/leehanyeong/django-ueditor-editor" rel="noopener noreferrer" target="_blank" style="color: rgb(41, 128, 185);">create a fork</a>&nbsp;on GitHub. Clone your fork, make some changes, and submit a pull request.</p>
<br>
<h2><strong>Issues</strong></h2>
<p>Use the GitHub&nbsp;<a href="https://github.com/leehanyeong/django-ueditor-editor/issues" rel="noopener noreferrer" target="_blank" style="color: rgb(41, 128, 185);">issue tracker</a>&nbsp;for&nbsp;<strong>django-ueditor-editor</strong>&nbsp;to submit bugs, issues, and feature requests.</p>"""


class UEPostListView(ListView):
    model = UEPost


class UEPostCreateView(CreateView):
    form_class = UEPostForm
    template_name = "posts/ueditorpost_create.html"


class UEPostDetailView(DetailView):
    model = UEPost


class UEPostUpdateView(UpdateView):
    model = UEPost
    fields = ["content"]


# NormalForm
class UEFieldFormView(FormView):
    form_class = UEFieldForm
    template_name = "posts/ueditorpost_normal_form.html"

    def form_valid(self, form):
        self.object = form.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("posts:ueditor-post-detail", args=(self.object.pk,))


class UEFieldFormHtmlInitialView(UEFieldFormView):
    initial = {
        "content": HTML_INITIAL,
    }


class UEFieldFormTextInitialView(UEFieldFormView):
    initial = {
        "content": "django-ueditor-editor makes UE.js easy to use on Django Forms and admin sites",
    }
