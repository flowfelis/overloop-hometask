from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    regions = models.ManyToManyField(
        'regions.Region', related_name='articles', blank=True
    )

    # In the case of an article's author gets deleted,
    # don't remove the article, just set the author FK column = null.
    author = models.ForeignKey(
        'authors.Author', on_delete=models.SET_NULL, blank=True, null=True
    )
