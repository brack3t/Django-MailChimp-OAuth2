from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'common/index.html'

    def get(self, request):
        return self.render_to_response({})


class ProfileView(TemplateView):
    template_name = 'common/profile.html'

    def get(self, request):
        return self.render_to_response({})
