from base.views import BaseView
from events.models import Event

# Create your views here.
class EventListView(BaseView):
    template_name='event_list.html'
    
    def get_context_data(self,**kwargs):
        context=super(EventListView,self).get_context_data(**kwargs)

        context['events']=Event.objects.order_by('date')

        return context

class EventDetails(BaseView):
    template_name='event.html'

    def get(self,request,id,**kwargs):         
        context=self.get_context_data(**kwargs)
        context['event']=Event.objects.get(pk=id)

        return self.render_to_response(context)

