# tests/test_cafe_tip_jar.py

import pytest
from exercises.cafe_tip_jar import total_with_tip

def test_total_with_tip_standard():
    # 18 + 12% of 18 = 18 + 2.16 = 20.16
    assert pytest.approx(total_with_tip(18.0, 12.0), rel=1e-3) == 20.16 