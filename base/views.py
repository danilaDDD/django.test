from django.views.generic import TemplateView

from contacts.models import Office
from tours.models import ToursBaner

# Create your views here.
class BaseView(TemplateView): 

    def get_context_data(self,**kwards):
        context=super(BaseView,self).get_context_data(**kwards)
        #data for header
        context['offices']=Office.get_hierarch_all()
        #data for footer
        context['baners']=ToursBaner.get_hierarch_all()
        return context
