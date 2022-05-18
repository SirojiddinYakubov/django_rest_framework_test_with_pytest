from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from common.models import BaseModel, Category


class Book(BaseModel):
    """ Книга """
    title = models.CharField(verbose_name=_('Название'), max_length=100)
    category = models.ForeignKey(Category, verbose_name=_('Категория'), on_delete=models.CASCADE)
    desc = models.CharField(verbose_name=_('Описание'), max_length=255)
    author = models.ManyToManyField(User, verbose_name=_('Автор'))
    pub_date = models.DateField(verbose_name=_('Дата публикации'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
