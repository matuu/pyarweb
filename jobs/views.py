from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import ListView, DetailView
from django.contrib.syndication.views import Feed
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from community.views import OwnedObject, FilterableList
from .models import Job, JobInactivated
from .forms import JobForm, JobInactivateForm
from pyarweb.settings import DEFAULT_FROM_EMAIL


class JobsFeed(Feed):
    title = "Feed de ofertas laborales de Pyar"
    link = reverse_lazy("jobs_list_all")
    description = "Todas las ofertas laborales con Python publicadas en Python Argentina"

    description_template = "jobs/job_detail_feed.html"

    def items(self):
        return Job.approved_jobs.order_by('-created')[0:10]

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.created

    def author_name(self, item):
        if item and item.company:
            return item.company.name
        return ''

    def author_email(self, item):
        if item:
            return item.email
        return ''

    def author_link(self, item):
        if item and item.company:
            return item.company.get_absolute_url()
        return ''

    def categories(self, item):
        if item:
            return item.tags.values_list('name', flat=True)
        return ()


class JobCreate(CreateView):
    model = Job
    form_class = JobForm

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.approved = False
        return super(JobCreate, self).form_valid(form)


class JobDetail(DetailView):
    model = Job

    def get(self, request, **kwargs):
        response = super(JobDetail, self).get(request, **kwargs)
        if not self.object.approved and self.object.owner != self.request.user:
            return HttpResponseRedirect(reverse_lazy("jobs_list_all"))
        return response


class JobList(ListView, FilterableList):
    model = Job
    paginate_by = 20

    def get_queryset(self):
        return Job.approved_jobs.all()


class JobUpdate(UpdateView, OwnedObject):
    """Edit jobs that use Python."""
    model = Job
    form_class = JobForm

    def form_valid(self, form):
        form.instance.approved = False
        form.user_moderate = None
        form.ts_moderate = None
        return super(JobUpdate, self).form_valid(form)


class JobDelete(DeleteView, OwnedObject):

    """Delete a Job."""
    model = Job
    success_url = reverse_lazy('jobs_list_all')

