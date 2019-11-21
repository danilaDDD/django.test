from django.views.generic import TemplateView

from contacts.models import Office
from tours.models import ToursBanner, TourType
from base.utils import handed_banner_params
from events.models import Event


# Create your views here.


class SvkBaseView(TemplateView):
    title = "Page"
    path = None

    def get_context_data(self, **kwards):
        context = super(SvkBaseView, self).get_context_data(**kwards)

        context['offices'] = Office.get_hierarchy_all()
        context['title'] = self.title
        context['baners'] = ToursBanner.get_hierarchy_all()

        return context


class SvkListView(SvkBaseView):
    template_name = 'list.html'
    model = None
    aside = True
    news = False

    def get(self, request, *arg, **kwargs):
        context = super(SvkListView, self).get_context_data(**kwargs)

        baner_id, tour_type_id = handed_banner_params(request)

        context['objects'] = self.model.get_response(baner_id, tour_type_id)
        context['title'] = self.title

        context['baner_id'] = baner_id
        context['tour_type_id'] = tour_type_id

        context['aside'] = self.aside
        context['news'] = self.news

        return self.render_to_response(context)


class SvkDetailsView(SvkBaseView):
    article_model = None
    section_model = None
    aside = True
    news = False

    template_name = "details.html"

    def get(self, request, id, **kwargs):
        context = super(SvkDetailsView, self).get_context_data(**kwargs)

        baner_id, tour_type_id = handed_banner_params(request)

        article = self.article_model.objects.get(pk=id)
        context['article'] = article.get_details(self.section_model)

        context['baner_id'] = baner_id
        context['tour_type_id'] = tour_type_id

        context['aside'] = self.aside
        context['new'] = self.new

        context['events'] = Event.objects.order_by('date')

        return self.render_to_response(context)


