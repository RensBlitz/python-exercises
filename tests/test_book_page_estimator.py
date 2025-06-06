# tests/test_book_page_estimator.py

import pytest
from exercises.book_page_estimator import estimate_pages

def test_estimate_40pph_90min():
    # 40 × 90 / 60 = 60
    assert pytest.approx(estimate_pages(40, 90), rel=1e-3) == 60.0 