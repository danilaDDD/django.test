from django.db import models as mds
from slavanka.params import short_len,long_len,DB_TIME_FORMAT

from datetime import timedelta
from datetime import datetime as dt

# Create your models here.
class ToursBaner(mds.Model):
    @staticmethod
    def get_hierarch_all():
        baners=[]

        for baner in ToursBaner.objects.all():
            baner.tour_types=[
                tour_type 
                for tour_type in TourType.objects.filter(baner=baner)
            ]

            baners.append(baner)
        
        return baners

    title=mds.CharField(max_length=short_len,default='')
    photo=mds.ImageField(null=True)

    def __str__(self):
        return self.title
    

class TourType(mds.Model):
    title=mds.CharField(max_length=short_len,default='Тур')
    baner=mds.ForeignKey(
        ToursBaner,
        on_delete=mds.CASCADE
    )

    def __str__(self):
        return self.title
    

class Tour(mds.Model):
    @staticmethod
    def get_short_list(size=4):
        all_tours=Tour.objects.all()
        if len(all_tours)>size:
            return all_tours[:size]
        else:
            return all_tours
    
    @staticmethod
    def get_filtreted_list(baner_id=None,tour_type_id=None):
        tours=[]

        if not tour_type_id==None:
            tours=Tour.objects.filter(tour_type__id=tour_type_id)
        elif not baner_id==None:
            tours=Tour.objects.filter(tour_type__baner__id=baner_id)
        else:
            tours=Tour.objects.all()
                 
        for tour in tours:            
            tour.duration=(tour.end_date-tour.start_date).days

            path=tour.path
            towns=[]
            if not path=='':
                try:
                    towns=path.split('-')
                except Exception:
                    pass
            tour.towns=towns

        return tours


    title=mds.CharField(max_length=long_len,default='')     
    path=mds.CharField(max_length=long_len,blank=True,default='')
    start_date=mds.DateTimeField(null=True,blank=True)
    end_date=mds.DateTimeField(null=True,blank=True)
    info=mds.TextField(blank=True,default='')
    photo=mds.ImageField(null=True)
    logotip=mds.ImageField(null=True)

    tour_type=mds.ForeignKey(
        TourType,
        on_delete=mds.CASCADE
    )

    def __str__(self):
        return self.title
         

class TourSection(mds.Model):
    time=mds.TimeField(null=True)
    title=mds.CharField(max_length=short_len,null=True)
    text=mds.TextField(default='',blank=True)
    day=mds.IntegerField(blank=True) 
    tour=mds.ForeignKey(
        Tour,
        on_delete=mds.CASCADE
    )

    def __str__(self):
        return self.title
    
