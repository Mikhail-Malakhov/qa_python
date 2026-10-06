import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book(self):
        collector = BooksCollector()

        collector.add_new_book('Марсианин')

        assert collector.books_genre == {'Марсианин': ''}

    def test_add_new_book_with_long_name(self):
        collector = BooksCollector()

        collector.add_new_book('А' * 41)

        assert collector.books_genre == {}

    def test_set_book_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Марсианин')
        collector.set_book_genre('Марсианин', 'Фантастика')

        assert collector.books_genre['Марсианин'] == 'Фантастика'

    @pytest.mark.parametrize(
        'book, genre',
        [
            ('Марсианин', 'Фантастика'),
            ('Шрек', 'Мультфильмы'),
            ('1+1', 'Комедии')
        ]
    )
    def test_get_book_genre(self, book, genre):
        collector = BooksCollector()

        collector.add_new_book(book)
        collector.set_book_genre(book, genre)

        assert collector.get_book_genre(book) == genre

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Марсианин')
        collector.set_book_genre('Марсианин', 'Фантастика')

        assert collector.get_books_with_specific_genre('Фантастика') == ['Марсианин']

    def test_get_books_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Шрек')

        assert collector.get_books_genre() == {'Шрек': ''}

    def test_get_books_for_children(self):
        collector = BooksCollector()

        collector.add_new_book('Шрек')
        collector.set_book_genre('Шрек', 'Мультфильмы')

        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')

        assert collector.get_books_for_children() == ['Шрек']

    def test_add_book_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Интерстеллар')
        collector.add_book_in_favorites('Интерстеллар')

        assert collector.favorites == ['Интерстеллар']

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Дюна')
        collector.add_book_in_favorites('Дюна')

        collector.delete_book_from_favorites('Дюна')

        assert collector.favorites == []

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()

        collector.add_new_book('Аватар')
        collector.add_book_in_favorites('Аватар')

        assert collector.get_list_of_favorites_books() == ['Аватар']