from django.db import models as mds
from easy_thumbnails.fields import ThumbnailerImageField

from slavanka.params import short_len, long_len, DB_TIME_FORMAT
from base.models import DataModel
from section.models import TextSection


class ToursBanner(mds.Model):
    @staticmethod
    def get_hierarchy_all(baner_id=None):

        baners = []
        if baner_id is None:
            for baner in ToursBanner.objects.all():
                baner.tour_types = [
                    tour_type
                    for tour_type in TourType.objects.filter(baner=baner)
                ]

                baners.append(baner)

        else:

            for baner in ToursBanner.objects.all():

                if baner.id == baner_id:
                    baner.tour_types = [
                        tour_type
                        for tour_type in TourType.objects.filter(baner=baner)
                    ]

                else:

                    baner.tour_types = []

                baners.append(baner)

        return baners

    title = mds.CharField(max_length=short_len, default='', verbose_name='Заголовок')
    photo = ThumbnailerImageField(upload_to='photos', verbose_name='Главное фото')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Банер'
        verbose_name_plural = 'Банеры'


class TourType(mds.Model):
    title = mds.CharField(max_length=short_len, default='Тур', verbose_name='Заголовок')
    baner = mds.ForeignKey(
        ToursBanner,
        on_delete=mds.CASCADE
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип тура'
        verbose_name_plural = 'Типы туров'


class Tour(DataModel):
    @staticmethod
    def get_short_list(size=4):
        all_tours = Tour.objects.all()
        if len(all_tours) > size:
            return all_tours[:size]
        else:
            return all_tours

    @staticmethod
    def get_response(baner_id=None, tour_type_id=None):
        data_list = []
        if tour_type_id is not None:
            data_list = Tour.objects.filter(tour_type__id=tour_type_id)
        elif baner_id is not None:
            data_list = Tour.objects.filter(tour_type__baner__id=baner_id)
        else:
            data_list = Tour.objects.all()

        data_list = list(data_list) + list(Article.get_response(baner_id,tour_type_id))

        return data_list

    title = mds.CharField(max_length=long_len, default='', verbose_name='Заголовок')
    photo = ThumbnailerImageField(upload_to='photos', verbose_name='Главное фото')
    path = mds.CharField(max_length=long_len, blank=True, default='', verbose_name='Путь прохождения')
    start_date = mds.DateTimeField(null=True, blank=True, verbose_name='Дата начала')
    end_date = mds.DateTimeField(null=True, blank=True, verbose_name='Дата конца')
    info = mds.TextField(blank=True, default='', verbose_name='Информация')
    logotip = ThumbnailerImageField(null=True, verbose_name='Логотип')
    tour_type = mds.ForeignKey(
        TourType,
        on_delete=mds.CASCADE
    )

    url_name = 'tour'

    def get_date(self):
        return self.get_days()

    def get_list_info(self):
        return self.path.split('-')

    def get_days(self):
        days = (self.end_date - self.start_date).days

        msg=''
        if days == 1:
            msg = ' день'
        elif days in range(2,4):
            msg = ' дня'
        else:
            msg = ' дней'

        return str(days) + msg

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тур'
        verbose_name_plural = 'Туры'


class Article(DataModel):
    @staticmethod
    def get_response(baner_id=None, tour_type_id=None):
        articls = []
        if tour_type_id is not None:
            articls = Article.objects.filter(tour_type__id=tour_type_id)
        elif baner_id is not None:
            articls = Article.objects.filter(tour_type__baner__id=baner_id)
        else:
            articls = Article.objects.all()

        return articls

    photo = ThumbnailerImageField(upload_to='photos', verbose_name='Главное фото')
    title = mds.CharField(max_length=long_len, verbose_name='Заголовок')
    subtitle = mds.CharField(max_length=short_len, default='',blank=True, verbose_name='Подзаголовок')
    tour_type = mds.ForeignKey(
        TourType,
        on_delete=mds.CASCADE
    )

    url_name = 'article'
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'


class ArticleSection(TextSection):
    parent = mds.ForeignKey(
        Article,
        on_delete=mds.CASCADE
    )

    db_manager = mds.Manager()




class TourSection(TextSection):
    parent = mds.ForeignKey(
        Tour,
        on_delete=mds.CASCADE
    )

    db_manager = mds.Manager()




