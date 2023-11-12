from django.views.generic import TemplateView


class TestPage(TemplateView):
    template_name = 'accounts/test.html'


class ThanksPage(TemplateView):
    template_name = 'accounts/thanks.html'


class HomeView(TemplateView):
    template_name = 'accounts/index.html'
