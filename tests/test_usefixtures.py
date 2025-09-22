import pytest


@pytest.fixture
def clear_books_database():
    print("[FIXTURE] удаляем данные из базы данных")


@pytest.fixture
def fill_books_database():
    print("[FIXTURE] создаем данные в базе данных")


@pytest.mark.usefixtures('fill_books_database')
def test_read_all_book_in_library():
    print("read all books")


@pytest.mark.usefixtures(
    'clear_books_database',
    'fill_books_database'
)
class TestLibrary:
    def test_read_book_from_library(self):
        ...

    def test_delete_book_from_library(self):
        ...