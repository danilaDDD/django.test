from django.views.generic import TemplateView
from django.shortcuts import reverse

from contacts.models import Office
from tours.models import ToursBanner, TourType
from base.utils import handed_banner_params
from events.models import Event


# Create your views here.





class SvkBaseView(TemplateView):
    title = "Page"
    _root_bread = [{'url_name': 'home', 'title': 'Главная', 'args': []}]
    add_bread = None

    def get_context_data(self, **kwards):
        context = super(SvkBaseView, self).get_context_data(**kwards)

        context['offices'] = Office.get_hierarchy_all()
        context['title'] = self.title
        context['baners'] = ToursBanner.get_hierarchy_all()

        return context

    def calc_bread(self, *args):
        if self.add_bread is not None:
            return self.handed_bread_crumbs(self._root_bread + self.add_bread)

        return self.handed_bread_crumbs(self._root_bread)

    def handed_bread_crumbs(self, bread_crumbs):
        return [
            {
                'title': brd['title'],
                'url': reverse(brd['url_name'], args=brd['args'])
            }
            for brd in bread_crumbs
        ]


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

        context['breadcrums'] = self.calc_bread()

        return self.render_to_response(context)


class SvkDetailsView(SvkBaseView):
    article_model = None
    section_model = None

    aside = True
    news = False

    template_name = "details.html"

    def get_context_data(self, **kwards):
        context = super(SvkDetailsView, self).get_context_data(**kwards)
        return context

    def get(self, request, id, **kwargs):
        context = super(SvkDetailsView, self).get_context_data(**kwargs)

        baner_id, tour_type_id = handed_banner_params(request)

        article = self.article_model.objects.get(pk=id)
        context['article'] = article.get_details(self.section_model)

        context['baner_id'] = baner_id
        context['tour_type_id'] = tour_type_id

        context['aside'] = self.aside
        context['news'] = self.news

        if self.news:
            context['events'] = Event.objects.order_by('date')

        context['breadcrums'] = self.calc_bread(id)

        return self.render_to_response(context)


class TestView(TemplateView):
    template_name = 'test.html'

    def get(self, request, id, **kwargs):
        context = super(TestView, self).get_context_data(**kwargs)
        context['id'] = id
        context['url'] = reverse('test', args=[id])
        return self.render_to_response(context)
