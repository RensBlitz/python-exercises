# exercises/library_catalogue.py

class LibraryCatalogue:
    """
    A simple library management system for storing and retrieving books.

    This class uses ISBN numbers as unique identifiers for books.
    Think about: How do you store key-value pairs? How do you add, find, and remove items?
    """

    def __init__(self) -> None:
        self.books = {}

    def add_book(self, isbn: str, title: str) -> None:
        """
        Add a new book to the library catalogue.

        :param isbn: the unique ISBN number for the book
        :param title: the title of the book

        TODO: Implement book addition to the catalogue
        """
        raise NotImplementedError()

    def lookup(self, isbn: str) -> str | None:
        """
        Find a book by its ISBN number.

        :param isbn: the ISBN to search for
        :return: the title of the book, or None if not found

        TODO: Implement book lookup by ISBN
        """
        raise NotImplementedError()

    def remove_book(self, isbn: str) -> bool:
        """
        Remove a book from the library catalogue.

        :param isbn: the ISBN of the book to remove
        :return: True if the book was found and removed, False otherwise

        TODO: Implement book removal from the catalogue
        """
        raise NotImplementedError()
