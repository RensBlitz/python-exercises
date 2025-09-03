# tests/test_library_catalogue.py

from exercises.library_catalogue import LibraryCatalogue


def test_add_lookup_remove_cycle():
    lib = LibraryCatalogue()
    lib.add_book("123", "Dune")
    assert lib.lookup("123") == "Dune"
    assert lib.remove_book("123") is True
    assert lib.lookup("123") is None
