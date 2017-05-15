from django.http import HttpResponse
from django.views.generic import TemplateView

class HelloView(TemplateView):
    template_name = "linkitos/index.html"
