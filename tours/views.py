from django.shortcuts import render

from tours.models import Tour,ToursBaner
from base.views import BaseView
from slavanka.params import DB_TIME_FORMAT

# Create your views here.
class ToursListView(BaseView):
    template_name='tours_list.html'

    def get(self,request,*arg,**kwargs):
        context=super(ToursListView,self).get_context_data(**kwargs)

        baner_id=request.GET.get('baner_id',None)
        tour_type_id=request.GET.get('tour_type_id',None)

        context['tours']=Tour.get_filtreted_list(baner_id=baner_id,tour_type_id=tour_type_id)         
        
        cur_baner=None
        if not baner_id==None:
            cur_baner=ToursBaner.objects.get(pk=baner_id)
        elif not tour_type_id==None:
            cur_baner=ToursBaner.objects.filter(tourtype__id=tour_type_id)
        else:
            pass
        context['curr_baner']=cur_baner
        

        
        return self.render_to_response(context)


     
