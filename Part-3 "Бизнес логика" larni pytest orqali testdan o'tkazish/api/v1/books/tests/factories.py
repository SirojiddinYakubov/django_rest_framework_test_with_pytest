from django.contrib.auth.models import User
from faker import Faker
import factory
from books.models import Book
from common.models import Category

fake = Faker()


class CategoryFactory(factory.django.DjangoModelFactory):
    """ этот класс создает поддельные данные категория для тестирования """

    class Meta:
        model = Category

    title = fake.job()


class UserFactory(factory.django.DjangoModelFactory):
    """ этот класс создает поддельные данные категория для тестирования """

    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = fake.email()
    first_name = fake.first_name()
    last_name = fake.last_name()
    password = fake.password()


class BookFactory(factory.django.DjangoModelFactory):
    """ этот класс создает поддельные данные книга для тестирования """

    class Meta:
        model = Book

    title = fake.bothify(text='????????')
    category = factory.SubFactory(CategoryFactory)
    desc = fake.text()
    pub_date = fake.date()

    @factory.post_generation
    def author(self, create, extracted, **kwargs):
        if not create:
            return
        self.author.add(UserFactory())
