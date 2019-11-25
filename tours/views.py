from django.shortcuts import render

from tours.models import Tour, Article, ArticleSection
from base.views import SvkBaseView, SvkListView, SvkDetailsView
from base.models import DataModel
from slavanka.params import DB_TIME_FORMAT
from tours.models import TourSection, Tour, Article


# Create your views here.


class ToursListView(SvkListView):
    model = Tour
    title = "Список туров"

    add_bread = [{
        'url_name': 'tour_list',
        'title': 'Туры',
        'args': []
    }]


class ArticleListView(SvkListView):
    model = Article
    title = "Список статей"
    add_bread = [{
        'url_name': 'article_list',
        'title': 'статьи',
        'args': []
    }]


class ToursDetailsView(SvkDetailsView):
    title = 'Тур'
    section_model = TourSection
    article_model = Tour

    def calc_bread(self,  id):
        add_bread = [
            {
                'url_name': 'tour_list',
                'title': 'Туры',
                'args': []
            },
            {
                'url_name': 'tour',
                'title': 'Тур',
                'args': [id]
            }
        ]

        return self.handed_bread_crumbs(self._root_bread+add_bread)


class ArticleDetailsView(SvkDetailsView):
    title = "Статья"
    section_model = ArticleSection
    article_model = Article

    def calc_bread(self, id):
        root_bread = self._root_bread
        add_bread = [{
            'url_name': 'article_list',
            'title': 'статьи',
            'args': []
        }, {
            'url_name': 'article',
            'title': 'статья',
            'args': [id]
        }]

        return self.handed_bread_crumbs(root_bread + add_bread)
