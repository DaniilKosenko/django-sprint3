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

    def valid_for_display(self):
        return (
            self.filter(is_published=True)
            .filter(category__is_published=True)
            .filter(pub_date__lt=now())
        )
