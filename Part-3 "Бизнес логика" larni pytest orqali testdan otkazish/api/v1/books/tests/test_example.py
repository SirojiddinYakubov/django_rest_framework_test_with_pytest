import pytest
import unittest


def calc():
    return 10


def test_calc():
    return calc() == 10


class MyTestCase(unittest.TestCase):
    def test_equal(self):
        v1 = 'yakubov'
        v2 = 'yakubov+'

        self.assertEqual(v1, v2)
        assert v1 == v2

    def test_dictionary(self):
        v1 = {'name': 'Yakubov', 'year': 2022}
        v2 = {'name': 'Developer', 'year': 2022}

        self.assertDictEqual(v1, v2)
        assert v1 == v2

    def test_list(self):
        expected = ['Yakubov', 'Developer']
        returned = ['John', 'Smith']

        self.assertListEqual(expected, returned)
        assert expected == returned


my_list = [1, 2, 3, 4, '5']


def test_my_list1():
    for n in my_list:
        assert isinstance(n, int)


@pytest.mark.parametrize('n', [1, 2, 3, 4, '5'])
def test_my_list2(n):
    assert isinstance(n, int)


@pytest.mark.parametrize('items_list', [1, 2, 3])
def test_example1(items_list):
    print(items_list)
    assert True


@pytest.mark.parametrize('items_list', [
    (int, 5),
    (dict, {'foo': 'bar'}),
    (list, [1, 2, 3])
])
def test_example2(items_list):
    type_item, value = items_list
    assert isinstance(value, type_item)


@pytest.mark.parametrize('name, password', [('Yakubov', 'qwerty12345'), ('Developer', 'admin12345')])
def test_example_fixture3(name, password):
    print(name, password)
    assert True


@pytest.fixture
def example_fixture1(request):
    data = {
        'object1': 'John',
        'object2': 'Developer',
    }
    return data[request.param]


@pytest.fixture
def example_fixture2(request):
    data = {
        'name1': 'Smith',
        'name2': 'Yakubov',
    }
    return data[request.param]


@pytest.mark.parametrize('example_fixture1, example_fixture2, validity', [
    ('object1', 'name1', True),
    ('object2', 'name2', False)
], indirect=['example_fixture2'])
def test_example_fixture2(example_fixture1, example_fixture2, validity):
    print(example_fixture1, example_fixture2, validity)
    assert True


@pytest.fixture(params=None)
def digits(request):
    return request.param


my_list2 = [1, 2, 3, 4, '5', 6]


def pytest_generate_tests(metafunc):
    if 'digits' in metafunc.fixturenames:
        metafunc.parametrize('digits', my_list2)


def test_my_list(digits):
    print(digits)
    assert True


def test_factory(db, category_factory, user_factory, book_factory):
    category = category_factory.create()
    user = user_factory.create()
    book = book_factory.create()
    print(book.desc)
    books = book_factory.create_batch(10)
    assert 10 == len(books)
