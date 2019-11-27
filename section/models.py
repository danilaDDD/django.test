from django.db import models as mds
from slavanka.params import long_len,short_len


# Create your models here.


class TextSection(mds.Model):
    time = mds.TimeField(null=True, blank=True, verbose_name='Время')
    title = mds.CharField(max_length=short_len, default='' ,
                          blank=True, verbose_name='Заголовок'
                          )
    text = mds.TextField(default='', blank=True, verbose_name='Текст')
    day = mds.IntegerField(blank=True, verbose_name='День')

    parent: mds.ForeignKey = None
    db_manager: mds.Manager = None

    class Meta:
        abstract = True

    def __str__(self):
        if self.title == '':
            return str(self.text)[:short_len]
        else:
            return self.title

