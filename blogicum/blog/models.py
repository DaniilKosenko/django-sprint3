from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class BaseModel(models.Model):
    is_published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Location(BaseModel):
    name = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'Географическая метка'
        verbose_name_plural = 'Географические метки'


class Category(BaseModel):
    title = models.CharField(max_length=256)
    description = models.TextField()
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Тематическая категория'
        verbose_name_plural = 'Тематические категории'


class Post(BaseModel):
    title = models.CharField(max_length=256)
    text = models.TextField()
    pub_date = models.DateTimeField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL,
                                 null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 null=True)

