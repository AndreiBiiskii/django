from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    ordering = 'title'
    articles = Article.objects.all()
    # for article in articles:
    #     for scope in article.scopes.filter(is_main = True):
    #         print(scope.tag.name)
    context = {
        'object_list': articles
    }

    # используйте этот параметр для упорядочивания результатов
    # https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by
    # for scope in articles.scopes.all():
    #     print(scope.name)
    return render(request, template, context)
