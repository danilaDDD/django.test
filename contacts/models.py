from django.db import models as mds

from slavanka.params import short_len, long_len


class UnitsContainer:
    container = True

    def __init__(self,units):
        self.offs = units


class Office(mds.Model):
    @staticmethod
    def get_hierarchy_all():
        offs_list = []

        offices = Office.objects.all()
        for office in (Office.objects.all()):
            office.contacts=OfficeContact.objects.filter(office=office)
            office.schedule_items = ScheduleItem.objects.filter(office=office)
            office.units = Unit.objects.filter(office=office)
            office.container = False
            offs_list.append(office)

            if len(office.units) > 0:
                for unit in office.units:
                    unit.contacts = UnitContact.objects.filter(unit=unit)

                container = UnitsContainer(office.units)
                offs_list.append(container)

        return offs_list

    title = mds.CharField(max_length=short_len, default='', verbose_name='Заголовок')
    address = mds.CharField(max_length=long_len, default='', blank=True, verbose_name='Адрес')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Офис'
        verbose_name_plural = 'Офисы'


class Unit(mds.Model):
    title = mds.CharField(max_length=short_len, default='', verbose_name='Заголовок')
    office = mds.ForeignKey(
        Office,
        on_delete=mds.CASCADE,
        null=True,
        verbose_name='Оффис'
    )

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'


class ScheduleItem(mds.Model):
    DAYS = (
        ('1', 'Пн'),
        ('2', 'Вт'),
        ('3', 'Ср'),
        ('4', 'Чт'),
        ('5', 'Пт'),
        ('6', 'Сб'),
        ('7', 'Вс'),
        ('1-5', 'Пн-Пт'),
        ('6,7', 'Сб-Вс'),
        ('8', 'Ежедневно')
    )

    def __init__(self, *args, **kwargs):
        super(ScheduleItem,self).__init__(*args, **kwargs)
        self.days_dict = {k: v for k, v in self.DAYS}

    days = mds.CharField(max_length=short_len, choices=DAYS, verbose_name='Дни работы')
    times = mds.CharField(max_length=short_len, default='Круглосуточно', verbose_name='Часы работы')

    office = mds.ForeignKey(
        Office,
        on_delete=mds.CASCADE
    )

    def pred_day(self):
        return self.days_dict[self.days]

    def __str__(self):
        return 'f{self.days}:{self.times}'

    class Meta:
        verbose_name = 'Строка рассписания'
        verbose_name_plural = 'Строки рассписания'


class Contact(mds.Model):
    TYPE = (
        ('P', 'Телефон'),
        ('E', 'Email')
    )

    value = mds.CharField(max_length=short_len,verbose_name='Значение')
    owner = mds.CharField(max_length=short_len, blank=True, default='', verbose_name='Владелец')
    contact_type = mds.CharField(max_length=short_len, choices=TYPE, verbose_name='Тип')

    def __str__(self):
        if self.owner == '':
            return self.value
        else:
            return self.owner

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        abstract = True


class OfficeContact(Contact):
    office = mds.ForeignKey(
        Office,
        on_delete=mds.CASCADE,
        null=True
    )


class UnitContact(Contact):
    unit = mds.ForeignKey(
        Unit,
        on_delete=mds.CASCADE,
        null=True
    )


