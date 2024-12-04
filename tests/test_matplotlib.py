import pytest

from tinyvdiff_demo.matplotlib import generate_plot


@pytest.fixture
def temp_pdf(tmp_path):
    """Fixture to create a temporary PDF file path"""
    return tmp_path / "test.pdf"


def test_matplotlib_visual(tinyvdiff, temp_pdf):
    """Test visual regression with single-page PDF generated with matplotlib"""
    pdf_path = generate_plot(temp_pdf)
    tinyvdiff.assert_pdf_snapshot(pdf_path, "snapshot_matplotlib.svg")
