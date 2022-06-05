from typing import Union

from django.contrib.auth.models import User

from common.models import Category


class CategoryService(object):
    """ Бизнес логики для категория """

    @classmethod
    def create_category(cls, data: dict) -> Category:
        category = Category.objects.create(**data)
        return category

    @classmethod
    def update_category(cls, instance: Category, data: dict) -> Category:
        for key, value in data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    @classmethod
    def get_detail(cls, id: int) -> Union[Category, bool]:
        try:
            category = Category.objects.get(is_active=True, id=id)
            return category
        except Category.DoesNotExist:
            return False


class UserService(object):
    """ Бизнес логики для ползователя """

    @classmethod
    def create_user(cls, data: dict) -> User:
        user = User.objects.create(**data)
        return user

    @classmethod
    def update_user(cls, instance: User, data: dict) -> User:
        for key, value in data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    @classmethod
    def get_detail(cls, id: int) -> Union[User, bool]:
        try:
            user = User.objects.get(is_active=True, id=id)
            return user
        except User.DoesNotExist:
            return False
