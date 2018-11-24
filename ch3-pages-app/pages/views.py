from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):
    template_name = 'about.html'

class FilmsPageView(TemplateView):
    template_name = 'films.html'

class BasePageView(TemplateView):
    template_name = 'base.html'
