from django.db import models
from django.db.models import QuerySet
from django.utils.timezone import now


class PostQuerySet(QuerySet):
    def published(self):
        return self.filter(is_published=True)

    def with_published_category(self):
        return self.filter(category__is_published=True)

    def not_future(self):
        return self.filter(pub_date__lt=now())

    def with_related_data(self):
        return self.select_related()

    def recent(self, count):
        return self[:count]


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)
