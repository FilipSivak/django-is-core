from django.views.generic.base import TemplateView
from django.contrib import auth


class LogoutView(TemplateView):
    template_name = "registration/logout.html"

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated():
            auth.logout(self.request)
        return super(LogoutView, self).get(*args, **kwargs)
