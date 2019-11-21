from django.db import models as mds
from django.shortcuts import reverse


class DataModel(mds.Model):

    @staticmethod
    def get_response(baner_id=None, tour_type_id=None):
        return []

    def get_details(self, section_class):
        all_sections = section_class.db_manager.filter(parent=self).order_by('day', 'id')

        count = 1
        days = [{"count": count, "sections": []}]
        for section in all_sections:
            if section.day != count:
                count += 1
                days.append({'count': count, 'sections': []})

            days[-1]['sections'].append(section)

        self.days = days
        return self

    url_name = None

    def get_title(self):
        return self.title

    def get_date(self):
        return ''

    def get_list_info(self):
        return []

    def get_photo(self):
        return self.photo

    def get_url(self):
        return reverse(self.url_name, args=[self.id])

    class Meta:
        abstract = True
