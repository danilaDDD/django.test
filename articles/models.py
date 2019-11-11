from django.db import models as mds
from slavanka.params import long_len,short_len

# Create your models here.
class Article(mds.Model):
    title=mds.CharField(max_length=long_len,)
    subtitle=mds.CharField(max_length=short_len,default='')


class ArticleSection(mds.Model):
    time=mds.TimeField(null=True)
    title=mds.CharField(max_length=short_len,null=True)
    text=mds.TextField(default='')
    day=mds.IntegerField(null=True) 

    article=mds.ForeignKey(
        Article,
        on_delete=mds.CASCADE
    )