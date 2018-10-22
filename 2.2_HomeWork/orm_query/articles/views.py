from django.views.generic import ListView

from .models import Article


class ArticleListView(ListView):
    template_name = 'articles/news.html'
    model = Article
    ordering = '-published_at'

    def get_queryset(self):
        """
        исключаем из запроса поля published_at в модели Article
        select_related получаем даные из связанных моделей по полям
        далее исключаем поле phone из связанной модели
        print(
        Article.objects.defer('published_at').select_related('author', 'genre').defer('author__phone').query
        )
        """
        return Article.objects\
            .defer('published_at')\
            .select_related('author', 'genre')\
            .defer('author__phone')
