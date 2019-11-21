from django.shortcuts import render

from tours.models import Tour, Article
from base.views import SvkBaseView, SvkListView, SvkDetailsView
from base.models import DataModel
from slavanka.params import DB_TIME_FORMAT
from tours.models import TourSection, ArticleSection, Tour, Article


# Create your views here.


class ToursListView(SvkListView):
    model = Tour
    title = "Список туров"



class ArticleListView(SvkListView):
    model = Article
    title = "Список статей"


class ToursDetailsView(SvkDetailsView):
    title = 'Тур'
    section_model = TourSection
    article_model = Tour


class ArticleDetailsView(SvkDetailsView):
    title = "Статья"
    section_model = ArticleSection
    article_model = Article
