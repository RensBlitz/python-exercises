# tests/test_file_statistics.py

import pytest
import os
from exercises.file_statistics import lines_and_words

def test_basic(tmp_path):
    temp_file = tmp_path / "test.txt"
    temp_file.write_text("Hello\nworld\n")
    lines, words = lines_and_words(str(temp_file))
    assert lines == 2
    # "Hello" and "world" → 2 words
    assert words == 2 