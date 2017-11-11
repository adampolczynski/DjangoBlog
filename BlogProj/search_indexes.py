from django.utils import timezone
from haystack import indexes

from blog.models import Entry
from articles.models import Article
from comments.models import Comment

class EntryIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    #body = indexes.CharField(model_attr='body')
    body = indexes.EdgeNgramField(model_attr='body')

    def get_model(self):
        return Entry

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()#filter(published__lte=timezone.now())

class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    title = indexes.CharField(model_attr='title')
    body = indexes.EdgeNgramField(model_attr='body')

    def get_model(self):
        return Article

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()#filter(published__lte=timezone.now())

class CommentsIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    body = indexes.EdgeNgramField(model_attr='body')

    def get_model(self):
    	return Comment

    def index_queryset(self, using=None):

    	return self.get_model().objects.all()