from django.db import models as mds
from slavanka.params import short_len,long_len

# Create your models here.
class Event(mds.Model):
    @staticmethod
    def get_short_list(size=4):
        all_events=Event.objects.all()
        if len(all_events)>size:
            return all_events[:size]
        else:
            return all_events


    title=mds.CharField(max_length=short_len)
    subtitle=mds.CharField(max_length=long_len)
    publish_date=mds.DateField()
    date=mds.DateTimeField()
    place=mds.CharField(max_length=short_len,null=True)
    text=mds.TextField(default='')
    photo=mds.ImageField()

    def __str__(self):
        return self.title
    
