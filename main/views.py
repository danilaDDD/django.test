from django.views.generic import TemplateView

from contacts.models import Office
from tours.models import ToursBaner,TourType,Tour
from events.models import Event
from base.views import BaseView

# Create your views here.
class HomeView(BaseView):
    template_name='index.html'

    def get_context_data(self,**kwards):
        context=super(HomeView,self).get_context_data(**kwards)
         
        context['baners']=ToursBaner.get_hierarch_all()
        context['tours']=Tour.get_short_list()
        context['events']=Event.get_short_list()

        return context
        
    
     
    
    
        
        
            
             
            

        