from base.views import SvkDetailsView, SvkListView
from .models import Event,EventSection


# Create your views here.


class EventListView(SvkListView):
    model = Event
    title = "Список мероприятий"
    add_bread = [{
        'url_name': 'event_list',
        'title': 'мероприятия',
        'args': []
    }]


class EventDetailsView(SvkDetailsView):
    article_model = Event
    section_model = EventSection

    news = True
    title = 'Событие'

    def get_(self, request, id, **kwargs):
        context = super(EventDetailsView, self).get_context_data(**kwargs)
        context['events'] = Event.objects.order_by('date')
        context['news'] = True

        return self.render_to_response(context)

    def calc_bread(self, id):
        root_bread = self._root_bread
        add_bread = [{
            'url_name': 'event_list',
            'title': 'мероприятия',
            'args': []
        }, {
            'url_name': 'event',
            'title': 'мероприятие',
            'args': [id]
        }]

        return self.handed_bread_crumbs(root_bread + add_bread)

