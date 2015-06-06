from models import HeatTemplate, VM
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class TemplatesList(ListView, LoginRequiredMixin):
    queryset = HeatTemplate.objects.order_by('-create_date')


class TemplateCreate(CreateView, LoginRequiredMixin):
    model = HeatTemplate


class TemplateUpdate(UpdateView, LoginRequiredMixin):
    model = HeatTemplate


class TemplateDetail(DetailView, LoginRequiredMixin):
    model = HeatTemplate


class TemplateDelete(DeleteView, LoginRequiredMixin):
    model = HeatTemplate
    success_url = reverse_lazy('template-list')