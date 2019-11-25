from django.db import models as mds
from easy_thumbnails.fields import ThumbnailerImageField

from slavanka.params import short_len, long_len
from base.models import DataModel
from section.models import TextSection


# Create your models here.


class Event(DataModel):
    @staticmethod
    def get_short_list(size=4):
        all_events = Event.objects.all()
        if len(all_events) > size:
            return all_events[:size]
        else:
            return all_events

    @staticmethod
    def get_response(baner_id=None, tour_type_id=None):
        return Event.objects.order_by('date')

    photo = ThumbnailerImageField(upload_to='photos', verbose_name='Главное фото', null=True)
    title = mds.CharField(max_length=short_len, verbose_name='Заголовок')
    subtitle = mds.CharField(max_length=long_len, verbose_name='Подзаголовок')
    publish_date = mds.DateField(verbose_name='Дата публикации')
    date = mds.DateTimeField(verbose_name='')
    place = mds.CharField(max_length=short_len, null=True, verbose_name='Место')
    url_name = 'event'

    def get_list_info(self):
        return [self.subtitle]

    def get_date(self):
        return self.publish_date

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'


class EventSection(TextSection):
    parent = mds.ForeignKey(
        Event,
        on_delete=mds.CASCADE
    )

    db_manager = mds.Manager()

    class Meta:
        verbose_name = 'Параграф события'
        verbose_name_plural = 'Параграфы события'
