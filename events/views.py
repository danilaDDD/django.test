from base.views import SvkBaseView,SvkListView
from events.models import Event

# Create your views here.


class EventListView(SvkListView):
     news = True
     model = Event
     site_title = "Список мероприятий"


class EventDetailsView(SvkBaseView):
    news = True

    def get(self, request, id, **kwargs):
        context = self.get_context_data(**kwargs)
        context['event'] = Event.objects.get(pk=id)

        return self.render_to_response(context)
